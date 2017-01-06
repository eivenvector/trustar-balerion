from .TrustarConnections import Neo4jConnection

neo4j_connection = Neo4jConnection()


class QueriesRepository(object):
    """
    This class contains all the queries
    """

    def __init__(self):
        self.cypher = neo4j_connection.cypher

    def query_records_number(self):
        query_string = "MATCH (n:RECORD {index: 'barncat'}) " + \
                       "RETURN COUNT(DISTINCT n) as NUMBER "
        return self.cypher.execute(query_string)

    def query_class_values(self, class_type):
        query_string = "MATCH (n:RECORD {index: 'barncat'})-[:CONTAINS]-(j:INDICATOR {type: '" + class_type + "'}) " + \
                       "RETURN DISTINCT j.value AS VALUE "
        return self.cypher.execute(query_string)

    def get_class_frequencies(self, class_type):
        query_string = "MATCH (n:RECORD {index: 'barncat'})-[:CONTAINS]-(j:INDICATOR {type: '" + class_type + "'}) " + \
                       "RETURN DISTINCT j.value AS VALUE, COUNT(DISTINCT n) AS NUMBER " + \
                       "ORDER BY NUMBER DESC "
        return self.cypher.execute(query_string)

    def get_indicator_frequency(self, input_value):
        query_string = "MATCH (n:RECORD {index: 'barncat'})-[:CONTAINS]-" + \
                       "      (j:INDICATOR {value: '" + input_value + "'}) " + \
                       "RETURN COUNT(DISTINCT n) AS NUMBER "
        return self.cypher.execute(query_string)

    def get_indicator_class_frequency(self, input_value, class_value):
        query_string = "MATCH (n:RECORD {index: 'barncat'})-[:CONTAINS]-" + \
                       "      (i:INDICATOR {value: '" + input_value + "'}) " + \
                       "MATCH (n:RECORD {index: 'barncat'})-[:CONTAINS]-" \
                       "      (j:INDICATOR {value: '" + class_value + "'}) " + \
                       "RETURN COUNT(DISTINCT n) AS NUMBER " + \
                       "ORDER BY NUMBER DESC "
        return self.cypher.execute(query_string)
