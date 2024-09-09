from database.database import Database
from bson.objectid import ObjectId

class LibraryModel:
    def __init__(self, database: Database):
        _database = database
        db = _database
        self.collection = db.collection

    def create_book(self, _id: int, title: str, author: str, year: int, price: float):
        try:
            res = self.collection.insert_one({"_id": _id, "titulo": title, "autor": author, "ano": year, "preco": price})
            print(f"Book created with id: {res.inserted_id}")
            return res.inserted_id
        except Exception as e:
            print(f"An error occurred while creating book: {e}")
            return None

    def read_book_by_id(self, id: str):
        try:
            res = self.collection.find_one({"_id": (id)})
            print(f"Book found: {res}")
            return res
        except Exception as e:
            print(f"An error occurred while reading book: {e}")
            return None

    def update_book(self, id: str, title: str, author: str, year: int, price: float):
        try:
            res = self.collection.update_one({"_id": (id)}, {"$set": {"titulo": title, "autor": author, "ano": year, "preco": price}})
            print(f"Book updated: {res.modified_count} document(s) modified")
            return res.modified_count
        except Exception as e:
            print(f"An error occurred while updating book: {e}")
            return None

    def delete_book(self, id: str):
        try:
            res = self.collection.delete_one({"_id": (id)})
            print(f"Book deleted: {res.deleted_count} document(s) deleted")
            return res.deleted_count
        except Exception as e:
            print(f"An error occurred while deleting book: {e}")
            return None
