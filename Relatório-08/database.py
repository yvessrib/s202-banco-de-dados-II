from neo4j import GraphDatabase

class GameDatabase:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    # Create a new player
    def create_player(self, player_id, name):
        with self.driver.session() as session:
            session.run(
                "CREATE (p:Player {id: $player_id, name: $name})",
                player_id=player_id, name=name
            )

    # Update player details
    def update_player(self, player_id, name=None):
        with self.driver.session() as session:
            if name:
                session.run(
                    "MATCH (p:Player {id: $player_id}) "
                    "SET p.name = $name",
                    player_id=player_id, name=name
                )

    # Delete a player
    def delete_player(self, player_id):
        with self.driver.session() as session:
            session.run(
                "MATCH (p:Player {id: $player_id}) "
                "DETACH DELETE p",
                player_id=player_id
            )

    # Retrieve all players
    def get_all_players(self):
        with self.driver.session() as session:
            result = session.run("MATCH (p:Player) RETURN p.id, p.name")
            return [(record["p.id"], record["p.name"]) for record in result]

    # Create a new match
    def create_match(self, match_id, player_ids, result):
        with self.driver.session() as session:
            session.run(
                "CREATE (m:Match {id: $match_id, result: $result}) "
                "WITH m "
                "MATCH (p:Player) WHERE p.id IN $player_ids "
                "CREATE (p)-[:PARTICIPATED_IN]->(m)",
                match_id=match_id, player_ids=player_ids, result=result
            )

    # Retrieve match information
    def get_match(self, match_id):
        with self.driver.session() as session:
            result = session.run(
                "MATCH (p:Player)-[:PARTICIPATED_IN]->(m:Match {id: $match_id}) "
                "RETURN m.id AS match_id, m.result AS result, collect(p.name) AS players",
                match_id=match_id
            )
            record = result.single()
            if record:
                return {
                    "match_id": record["match_id"],
                    "result": record["result"],
                    "players": record["players"]
                }
            return None

    # Update match result
    def update_match(self, match_id, result):
        with self.driver.session() as session:
            session.run(
                "MATCH (m:Match {id: $match_id}) "
                "SET m.result = $result",
                match_id=match_id, result=result
            )

    # Delete a match
    def delete_match(self, match_id):
        with self.driver.session() as session:
            session.run(
                "MATCH (m:Match {id: $match_id}) "
                "DETACH DELETE m",
                match_id=match_id
            )

    # Get match history for a specific player
    def get_player_history(self, player_id):
        with self.driver.session() as session:
            result = session.run(
                "MATCH (p:Player {id: $player_id})-[:PARTICIPATED_IN]->(m:Match) "
                "RETURN m.id AS match_id, m.result AS result",
                player_id=player_id
            )
            return [(record["match_id"], record["result"]) for record in result]
