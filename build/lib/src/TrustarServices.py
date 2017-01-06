from .TrustarQueries import QueriesRepository

COUNT = "NUMBER"
VALUE = "VALUE"

queries_repository = QueriesRepository()


class Metrics(object):
    """
    This class takes a Connect object that allows us to query the Neo4j DB and determine the required metrics to
    compute the empirical probability
    """

    def __init__(self, **kwargs):
        self.type = ""
        for key, value in kwargs.items():
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
        result_query = queries_repository.get_class_frequencies(class_type)
        for row in result_query:
                result[row[VALUE]] = row[COUNT]
        return result

    @staticmethod
    def get_indicator_frequency(input_value):
        """

        :param input_value:
        :return:
        """

        result = queries_repository.get_indicator_frequency(input_value)
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
            result_query = queries_repository.get_indicator_class_frequency(input_value, class_value)
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
