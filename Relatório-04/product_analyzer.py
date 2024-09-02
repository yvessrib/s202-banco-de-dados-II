from helper.writeAJson import write_a_json

class ProductAnalyzer:

    def __init__(self, database):
        self.db = database

    def total_sales_per_day(self):
        pipeline = [
            {"$group": {"_id": "$data_compra", "total_sales": {"$sum": {"$size": "$produtos"}}}}
        ]
        result = list(self.db.collection.aggregate(pipeline))
        write_a_json(result, "total_sales_per_day")
        return result
    
    def most_sold_product(self):
        pipeline = [
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$produtos.descricao", "total_sold": {"$sum": "$produtos.quantidade"}}},
            {"$sort": {"total_sold": -1}},
            {"$limit": 1}
        ]
        result = list(self.db.collection.aggregate(pipeline))
        write_a_json(result, "most_sold_product")
        return result[0] if result else None
    
    def highest_spending_customer(self):
        pipeline = [
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$cliente_id", "total_spent": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
            {"$sort": {"total_spent": -1}},
            {"$limit": 1}
        ]
        result = list(self.db.collection.aggregate(pipeline))
        write_a_json(result, "highest_spending_customer")
        return result[0] if result else None
    
    def products_above_quantity_1(self):
        pipeline = [
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$produtos.descricao", "total_quantity": {"$sum": "$produtos.quantidade"}}},
            {"$match": {"total_quantity": {"$gt": 1}}}
        ]
        result = list(self.db.collection.aggregate(pipeline))
        write_a_json(result, "products_above_quantity_1")
        return [item['_id'] for item in result] if result else []
    