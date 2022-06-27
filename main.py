from app.database_operations import Database_operations as db
from app.api_operations import Api_operations as api

logging_filename = 'log.txt'
mydb = db(logging_filename=logging_filename)
mydb.db_connect(host="localhost", user="root", password="",
                database="mydb")

myapi = api(logging_filename=logging_filename)
rates = myapi.get_rates(currencies=['eur', 'usd'])
mydb.db_update(rates=rates)
mydb.from_db_to_excel()
