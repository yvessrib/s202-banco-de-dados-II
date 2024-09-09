import pymongo # pip install pymongo
from database.seed.seed import dataset
from database.validator.validate import schema

class Database:
    def __init__(self, database, collection):
        self.connect(database, collection)

    def connect(self, database, collection):
        try:
            connection_string = "localhost:27017"
            self.cluster_connection = pymongo.MongoClient(
                connection_string,
                tlsAllowInvalidCertificates=True
            )
            self.db = self.cluster_connection[database]
            self.collection = self.db[collection]
            self.db.create_collection(collection, validator=schema)
            print("Conectado ao banco de dados com sucesso!")
        except Exception as e:
            print(e)

    def reset_database(self):
        try: 
            self.db.drop_collection(self.collection)
            self.db.create_collection(self.collection.name, validator=schema)
            self.collection.insert_many(dataset)
            print("Banco de dados resetado com sucesso!")
        except Exception as e:
            print(e)