from database.database import Database
from model.library import LibraryModel

def main_menu():
    print("\nMenu Principal:")
    print("1. Visualizar todos os livros")
    print("2. Criar um novo livro")
    print("3. Atualizar informações de um livro")
    print("4. Deletar um livro")
    print("5. Sair")

def create_book(library):
    print("\nCriar um novo livro:")
    book_id = input("ID do livro: ")
    title = input("Título: ")
    author = input("Autor: ")
    year = int(input("Ano: "))
    price = float(input("Preço: "))
    new_book = library.create_book(book_id, title, author, year, price)
    print("Livro criado com sucesso!")

def update_book(library):
    print("\nAtualizar informações de um livro:")
    book_id = input("ID do livro a ser atualizado: ")
    title = input("Novo título (pressione Enter para manter o mesmo): ")
    author = input("Novo autor (pressione Enter para manter o mesmo): ")
    year = input("Novo ano (pressione Enter para manter o mesmo): ")
    price = input("Novo preço (pressione Enter para manter o mesmo): ")
    updated_fields = {}
    if title:
        updated_fields['title'] = title
    if author:
        updated_fields['author'] = author
    if year:
        updated_fields['year'] = int(year)
    if price:
        updated_fields['price'] = float(price)
    library.update_book_by_id(book_id, **updated_fields)
    print("Informações do livro atualizadas com sucesso!")

def delete_book(library):
    print("\nDeletar um livro:")
    book_id = input("ID do livro a ser deletado: ")
    library.delete_book_by_id(book_id)
    print("Livro deletado com sucesso!")

def print_books(books):
    print("Livros na Biblioteca:")
    for book in books:
        print(f"ID: {book['_id']}, Título: {book['titulo']}, Autor: {book['autor']}, Ano: {book['ano']}, Preço: R${book['preco']}")


db = Database(database="biblioteca", collection="livros")
db.reset_database()
library = LibraryModel(db)

while True:
    main_menu()
    choice = input("Escolha uma opção: ")

    if choice == "1":
        books = library.collection.find()
        print_books(books)
    elif choice == "2":
        _id = int(input("ID do livro: "))
        title = input("Título: ")
        author = input("Autor: ")
        year = int(input("Ano: "))
        price = float(input("Preço: "))
        library.create_book(_id, title, author, year, price)
    elif choice == "3":
        id = input("ID do livro a ser atualizado: ")
        title = input("Novo título (pressione Enter para manter o mesmo): ")
        author = input("Novo autor (pressione Enter para manter o mesmo): ")
        year = input("Novo ano (pressione Enter para manter o mesmo): ")
        price = input("Novo preço (pressione Enter para manter o mesmo): ")
        library.update_book(id, title, author, int(year), float(price))
    elif choice == "4":
        id = input("ID do livro a ser deletado: ")
        library.delete_book(id)
    elif choice == "5":
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")