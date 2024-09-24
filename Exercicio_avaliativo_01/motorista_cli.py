from corrida import Corrida
from motorista import Motorista
from passageiro import Passageiro


class MotoristaCLI:
    def __init__(self, motorista_dao):
        self.motorista_dao = motorista_dao

    def criar_motorista(self):
        nome_motorista = input("Digite o nome do motorista: ")
        motorista = Motorista(nome_motorista)

        nome_passageiro = input("Digite o nome do passageiro: ")
        documento_passageiro = input("Digite o documento do passageiro: ")
        passageiro = Passageiro(nome_passageiro, documento_passageiro)

        qtd_corridas = int(input("Digite a quantidade de corridas: "))
        for _ in range(qtd_corridas):
            distancia_corrida = float(input("Digite a distância da corrida: "))
            valor_corrida = float(input("Digite o valor da corrida: "))
            nota_corrida = float(input("Digite a nota da corrida: "))
            corrida = Corrida(nota_corrida, distancia_corrida, valor_corrida, passageiro)
            motorista.adicionar_corrida(corrida)

        motorista.nota = motorista.calcular_nota()
        self.motorista_dao.criar_motorista(motorista.to_dict())
        print("Motorista criado com sucesso!")

    def buscar_motorista(self):
        nome = input("Digite o nome do motorista a ser buscado: ")
        motorista = self.motorista_dao.buscar_motorista({"nome": nome})
        if motorista:
            print(f"Nome: {motorista['nome']}")
            print(f"Corridas: {motorista['corridas']}")
            print(f"Nota: {motorista['nota']}")
        else:
            print("Motorista não encontrado.")

    def atualizar_motorista(self):
        nome = input("Digite o nome do motorista a ser atualizado: ")
        nota = float(input("Digite a nova nota do motorista: "))
        self.motorista_dao.atualizar_motorista({"nome": nome}, {"nota": nota})
        print("Nota do motorista atualizada com sucesso!")

    def deletar_motorista(self):
        nome = input("Digite o nome do motorista a ser deletado: ")
        self.motorista_dao.deletar_motorista({"nome": nome})
        print("Motorista deletado com sucesso!")

    def run(self):
        print("Bem-vindo ao CLI de motoristas!")
        print("Comandos disponíveis: create, read, update, delete, quit")
        while True:
            command = input("Digite um comando: ")
            if command == "quit":
                break
            elif command == "create":
                self.criar_motorista()
            elif command == "read":
                self.buscar_motorista()
            elif command == "update":
                self.atualizar_motorista()
            elif command == "delete":
                self.deletar_motorista()
            else:
                print("Comando inválido. Tente novamente.")
