from TrustarQueries import QueriesRepository
import datetime
import json
import math
import pandas as pd

COUNT = "NUMBER"
VALUE = "VALUE"

MAPPING = {"md5": "MD5",
           "Campaign": "CAMPAIGN",
           "sha1": "SHA1",
           "sha256": "SHA256",
           "ip-dst": "IP",
           "Domain": "URL",
           "rat_name": "MALWARE",
           "imphash": "IMPHASH_MD5",
           "section_.BSS": "BSS_MD5",
           "section_.DATA": "DATA_MD5",
           "section_.IDATA": "IDATA_MD5",
           "section_.ITEXT": "ITEXT_MD5",
           "section_.RDATA": "RDATA_MD5",
           "section_.RELOC": "RELOC_MD5",
           "section_.RSRC": "RSRC_MD5",
           "section_.TEXT": "TEXT_MD5",
           "section_.TLS": "TLS_MD5",
           "Mutex": "MUTEX"}

queries_repository = QueriesRepository()


class Metrics(object):
    """
    This class allows us to query the Neo4j DB and determine the required metrics to
    compute the empirical probabilities
    """

    def __init__(self, **kwargs):
        self.type = ""
        for key, value in kwargs.iteritems():
            if key == 'type':
                self.type = value
            elif key == 'time_service':
                self.time_service = value

    @staticmethod
    def get_records_number():
        """

        :return:
        """

        result = queries_repository.query_records_number()
        return result[0][COUNT]

    @staticmethod
    def get_class_values(class_type):
        """
        Method to determine the frequency of occurence of a specific class type

        :param class_type:
        """

        result_query = queries_repository.query_class_values(class_type)

        result = []
        for row in result_query:
            result.append(row[VALUE])
        return result

    @staticmethod
    def get_class_distribution(class_type):
        """

        :param class_type:
        :return:
        """

        result = {}
        result_query = queries_repository.query_class_frequencies(class_type)
        for row in result_query:
                result[row[VALUE]] = row[COUNT]
        return result

    @staticmethod
    def get_indicator_frequency(input_value):
        """

        :param input_value:
        :return:
        """

        result = queries_repository.query_indicator_frequency(input_value)
        return result[0][COUNT]

    @staticmethod
    def get_indicator_class_frequency(input_value, class_values):
        """

        :param input_value:
        :param class_values:
        :return:
        """
        result = {}
        for class_value in class_values:
            result_query = queries_repository.query_indicator_class_frequency(input_value, class_value)
            if result_query[0][COUNT] != 0:
                result[class_value] = result_query[0][COUNT]
        return result

    @staticmethod
    def get_non_uniform_odds(n_x_y):
        """

        :param n_x_y:
        :return:
        """

        summation = sum(n_x_y.values())
        result = {}
        for class_value in n_x_y:
            result[class_value] = float(n_x_y[class_value])/float(summation)*100
        return result

    @staticmethod
    def get_uniform_odds(n_x_y, n_y):
        """
        :param n_x_y:
        :param n_y:
        :return:
        """

        ratio = {}
        for class_value in n_x_y:
            ratio[class_value] = float(n_x_y[class_value])/float(n_y[class_value])

        result = {}
        summation = sum(ratio.values())
        for class_value in ratio:
            result[class_value] = float(ratio[class_value])/float(summation)
        return result


class Store(object):
    """
    This class is used to store a data set to a Neo4j database
    """

    def __init__(self, **kwargs):
        self.type = ""
        for key, value in kwargs.iteritems():
            if key == 'type':
                self.type = value
            elif key == 'time_service':
                self.time_service = value

    @staticmethod
    def process_file(source_file):
            df = pd.read_csv(source_file)
            return df

    @staticmethod
    def store_file(record):
        """

        :param record:
        :return:
        """

        json_in_comment = record.comment == 'JSON config'
        json_config = {}

        if True in json_in_comment.values:
            try:
                json_config = json.loads(record[record.comment == 'JSON config']['value'].values[0]
                                         .encode('ascii', 'ignore'))
            except:
                pass

            if 'Date' in json_config:
                time = json_config['Date'].split(" ")[0].split("-")
                timestamp = '{0:f}'.format((datetime.datetime(int(time[0]), int(time[1]), int(time[2][0:2])) -
                                            datetime.datetime(1970, 1, 1)).total_seconds()*1000)
            else:
                timestamp = '{0:f}'.format((datetime.datetime(2016, 8, 12) -
                                            datetime.datetime(1970, 1, 1)).total_seconds()*1000)
            doc_id = str(record.event_id.values[0])

            if 'Campaign' in json_config:
                title = json_config['Campaign'].encode('ascii', 'ignore') + " " + doc_id
            else:
                title = 'NO_CAMPAIGN' + " " + doc_id

            for key in MAPPING:
                if key in json_config:
                    indicator_value = json_config[key]
                    indicator_type = MAPPING[key]
                    queries_repository.store_object(doc_id,
                                                    title,
                                                    str(int(math.floor(float(timestamp)))),
                                                    indicator_type,
                                                    indicator_value)
