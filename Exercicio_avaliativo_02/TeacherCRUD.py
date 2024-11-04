# Classe TeacherCRUD com funções de CRUD para a entidade Teacher
from Exercicio_avaliativo_02.database import Database


class TeacherCRUD:
    def __init__(self, database):
        self.db = database

    def create(self, name, ano_nasc, cpf):
        query = """
        CREATE (t:Teacher {name: $name, ano_nasc: $ano_nasc, cpf: $cpf})
        RETURN t
        """
        return self.db.execute_query(query, {"name": name, "ano_nasc": ano_nasc, "cpf": cpf})

    def read(self, name):
        query = """
        MATCH (t:Teacher {name: $name})
        RETURN t.name AS name, t.ano_nasc AS ano_nasc, t.cpf AS cpf
        """
        result = self.db.execute_query(query, {"name": name})
        return result[0] if result else None

    def update(self, name, newCpf):
        query = """
        MATCH (t:Teacher {name: $name})
        SET t.cpf = $newCpf
        RETURN t
        """
        return self.db.execute_query(query, {"name": name, "newCpf": newCpf})

    def delete(self, name):
        query = """
        MATCH (t:Teacher {name: $name})
        DETACH DELETE t
        """
        self.db.execute_query(query, {"name": name})

class TeacherCLI:
    def __init__(self, teacher_crud):
        self.teacher_crud = teacher_crud

    def menu(self):
        print("\n-- Teacher CRUD CLI --")
        print("1. Create Teacher")
        print("2. Read Teacher")
        print("3. Update Teacher CPF")
        print("4. Delete Teacher")
        print("5. Exit")

    def run(self):
        while True:
            self.menu()
            choice = input("Enter your choice: ")

            if choice == "1":
                name = input("Enter teacher's name: ")
                ano_nasc = int(input("Enter teacher's year of birth: "))
                cpf = input("Enter teacher's CPF: ")
                self.teacher_crud.create(name, ano_nasc, cpf)
                print(f"Teacher '{name}' created successfully.")

            elif choice == "2":
                name = input("Enter teacher's name to read: ")
                teacher = self.teacher_crud.read(name)
                if teacher:
                    print(f"Name: {teacher['name']}, Year of Birth: {teacher['ano_nasc']}, CPF: {teacher['cpf']}")
                else:
                    print(f"Teacher '{name}' not found.")

            elif choice == "3":
                name = input("Enter teacher's name to update CPF: ")
                new_cpf = input("Enter new CPF: ")
                self.teacher_crud.update(name, new_cpf)
                print(f"Teacher '{name}' CPF updated successfully.")

            elif choice == "4":
                name = input("Enter teacher's name to delete: ")
                self.teacher_crud.delete(name)
                print(f"Teacher '{name}' deleted successfully.")

            elif choice == "5":
                print("Exiting CLI.")
                break

            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    
    uri = "bolt://54.164.92.72"
    user = "neo4j"
    password = "requisitions-presentation-afternoon"

    db = Database(uri, user, password)
    teacher_crud = TeacherCRUD(db)
    
    cli = TeacherCLI(teacher_crud)

    cli.run()
    
    db.close()