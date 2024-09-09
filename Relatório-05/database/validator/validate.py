schema = {
    "$jsonSchema": {
      "bsonType": "object",
      "required": ["_id", "titulo", "autor", "ano", "preco"],
      "properties": {
          "_id": {
              "bsonType": ["string", "int"],
              "description": "'_id' deve ser uma string ou um inteiro e é obrigatório"
          },
          "titulo": {
              "bsonType": "string",
              "description": "'titulo' deve ser uma string e é obrigatório"
          },
          "autor": {
              "bsonType": "string",
              "description": "'autor' deve ser uma string e é obrigatório"
          },
          "ano": {
              "bsonType": "int",
              "minimum": 1000,
              "maximum": 9999,
              "description": "'ano' deve ser um inteiro entre 1000 e 9999 e é obrigatório"
          },
          "preco": {
              "bsonType": "double",
              "description": "'preco' deve ser um número de ponto flutuante e é obrigatório"
          }
      }
    }
}
