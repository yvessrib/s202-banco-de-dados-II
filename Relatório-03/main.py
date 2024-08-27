from database.database import Database
from pokedex import Pokedex

db = Database(database="pokedex", collection="pokemons")
db.reset_database()

pokedex = Pokedex(db)
pokedex.find_all_pokemons()
pokedex.get_pokemon_by_name("Pikachu")
pokedex.get_pokemon_by_type(["Electric"])
pokedex.get_pokemon_by_weakness(["Ground"])
pokedex.does_pokemon_has_evolution(["Electric", "Fire"])