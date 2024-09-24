from database import Database

class MotoristaDAO:
    def __init__(self):
        self.database = Database(database="uber", collection="motoristas")

    def criar_motorista(self, motorista):
        self.database.collection.insert_one(motorista)

    def buscar_motorista(self, filtro):
        return self.database.collection.find_one(filtro)

    def atualizar_motorista(self, filtro, novos_dados):
        self.database.collection.update_one(filtro, {'$set': novos_dados})

    def deletar_motorista(self, filtro):
        self.database.collection.delete_one(filtro)