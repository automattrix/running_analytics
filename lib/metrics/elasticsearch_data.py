from elasticsearch import Elasticsearch


class ElasticHelper:
    def __init__(self, params):
        self.host_address = params['HOST']
        self.username = params['USER']
        self.password = params['PASSWORD']
        self.port = params['PORT']

    def connect_es(self):
        es = Elasticsearch(
            [self.host_address],
            http_auth=(self.username, self.password),
            scheme="http",
            port=self.port
        )
        return es


