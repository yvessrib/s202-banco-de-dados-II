from Relatório_8.database import GameDatabase

db = GameDatabase("bolt://174.129.77.209", "neo4j", "orange-performance-flood")

# Criar jogadores
db.create_player("1", "Jogador 1")
db.create_player("2", "Jogador 2")

# Criar uma partida entre dois jogadores
db.create_match("match1", ["1", "2"], "Jogador 1 venceu")

# Recuperar informações da partida
print(db.get_match("match1"))

# Atualizar o resultado da partida
db.update_match("match1", "Jogador 2 venceu")

# Ver histórico de partidas de um jogador
print(db.get_player_history("1"))

# Fechar a conexão
db.close()
