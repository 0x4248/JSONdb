# JSONdb
# Create databases using JSON files
# Github: https://www.github.com/0x4248/JSONdb
# Licence: GNU General Public License v3.0
# By: 0x4248

try:
    from JSONdb import JSONdb
except ImportError:
    print("JSONdb module not found. Please install JSONdb module before running this script.")

db = JSONdb("demo.json")

db.init("Products", "A demo database for products")
db.createColumn("product", "STRING", "The name of the product")
db.createColumn("price", "FLOAT", "The price of the product")
db.createColumn("stock", "INTEGER", "The stock of the product")
db.insertItems(0, ["Apple", "Banana", "Orange", "Pineapple", "Grapes", "Watermelon"])
db.insertItems(1, [1.99, 0.99, 2.99, 3.99, 4.99, 5.99])
db.insertItems(2, [100, 200, 50, 25, 10, 5])
db.saveDatabase()