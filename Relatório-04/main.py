from database import Database
from product_analyzer import ProductAnalyzer

db = Database(database="mercado", collection="produtos")
db.reset_database()

analyzer = ProductAnalyzer(db)

total_sales_per_day_result = analyzer.total_sales_per_day()

print("Total de vendas por dia:")
for result in total_sales_per_day_result:
    print(f"Data: {result['_id']}, Total de vendas: {result['total_vendas']}")

most_sold_product_result = analyzer.most_sold_product()

print("\nProduto mais vendido:")
for result in most_sold_product_result:
    print(f"Produto: {'Nome não registrado' if result['_id'] is None else result['_id']}, Total vendido: {result['total_vendido']}")

top_spending_customer_result = analyzer.top_spending_customer()

print("\nCliente que mais gastou em uma única compra:")
for result in top_spending_customer_result:
    print(f"Cliente ID: {result['_id']}, Total gasto: {result['total_gasto']}")

products_sold_above_quantity_result = analyzer.products_sold_above_quantity(3)

print("\nProdutos vendidos acima de uma determinada quantidade:")
for result in products_sold_above_quantity_result:
    print(f"Produto: {'Nome não registrado' if result['_id'] is None else result['_id']}, Total vendido: {result['total_vendido']}")


