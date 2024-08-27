from database.database import Database
import helper as json

class Pokedex:
    def __init__(self, database: Database):
        _database = database
        self.db = _database

    def find_all_pokemons(self):
        response = self.db.collection.find()
        json(response, 'all-pokemons')
        return response

    def get_pokemon_by_name(self, name: str):
        response = self.db.collection.find({"name": name})
        json(response, name)
        return response

    def get_pokemon_by_type(self, types: list):
        response = self.db.collection.find({"type": {"$in": types}})
        json(response, types)
        return response

    def get_pokemon_by_weakness(self, weakness: list):
        response = self.db.collection.find({"weakness": {"$in": weakness}})
        json(response, weakness)
        return response

    def does_pokemon_has_evolution(self, types: list):
        response = self.db.collection.find({"type": {"$in": types}, "next_evolution": {"$exists": True}})
        json(response, types)
        return response