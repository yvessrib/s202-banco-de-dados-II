# Função para executar as questões
from Exercicio_avaliativo_02.database import Database

def run_queries():
    uri = "bolt://54.164.92.72"
    user = "neo4j"
    password = "requisitions-presentation-afternoon"

    db = Database(uri, user, password)

    # Questão 01
    Q1_a = "MATCH (t:Teacher {name: 'Renzo'}) RETURN t.ano_nasc AS ano_nasc, t.cpf AS CPF"
    Q1_a = db.execute_query(Q1_a)

    Q1_b = "MATCH (t:Teacher) WHERE t.name STARTS WITH 'M' RETURN t.name AS name, t.cpf AS CPF"
    Q1_b = db.execute_query(Q1_b)

    Q1_c = "MATCH (c:City) RETURN c.name AS city_name"
    Q1_c = db.execute_query(Q1_c)

    Q1_d = """
    MATCH (s:School)
    WHERE s.number >= 150 AND s.number <= 550
    RETURN s.name AS school_name, s.address AS address, s.number AS number
    """
    Q1_d = db.execute_query(Q1_d)

    # Questão 02
    Q2_a = """
    MATCH (t:Teacher)
    RETURN max(t.ano_nasc) AS ano_mais_jovem, min(t.ano_nasc) AS ano_mais_velho
    """
    Q2_a = db.execute_query(Q2_a)

    Q2_b = "MATCH (c:City) RETURN avg(c.population) AS media_populacao"
    Q2_b = db.execute_query(Q2_b)

    Q2_c = """
    MATCH (c:City {cep: '37540-000'})
    RETURN replace(c.name, 'a', 'A') AS nome_formatado
    """
    Q2_c = db.execute_query(Q2_c)

    Q2_d = "MATCH (t:Teacher) RETURN substring(t.name, 2, 1) AS terceira_letra"
    Q2_d = db.execute_query(Q2_d)

    print("Resultado da Questão 01:")
    print("1.a", Q1_a)
    print("1.b", Q1_b)
    print("1.c", Q1_c)
    print("1.d", Q1_d)

    print("\nResultado da Questão 02:")
    print("2.a", Q2_a)
    print("2.b", Q2_b)
    print("2.c", Q2_c)
    print("2.d", Q2_d)

    db.close()

if __name__ == "__main__":
    run_queries()