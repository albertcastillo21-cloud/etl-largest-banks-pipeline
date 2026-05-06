from banks_project import log_progress, extract, transform, load_to_csv, load_to_db,run_query
import sqlite3

URL = "https://web.archive.org/web/20230908091635/https://en.wikipedia.org/wiki/List_of_largest_banks"
table_attribs = ["Name", "MC_USD_Billion"]
csv_path = "./Largest_banks_data.csv"
name_table = "Largest_banks"
db_name = "Banks_db"


log_progress("Preliminaries complete. Initiating ETL function in process")
df = extract(URL, table_attribs)
# print(df)

log_progress("Data extraction complete. Initiating transformation in process")
df = transform(df)
# print(df)


log_progress("Data transform complete. Initialing loading to CSV")
load_to_csv(df, csv_path)


log_progress("SQL Connection initialing")
sql_connection = sqlite3.connect("Banks_db.db")

log_progress("Database create complete")
load_to_db(df,sql_connection, name_table)

log_progress("Running query")
query_statement = f'SELECT * FROM Largest_banks'
run_query(query_statement,sql_connection)

query_statement = f'SELECT AVG(MC_GBP_Billion) FROM Largest_banks'
run_query(query_statement, sql_connection)

query_statement = f'SELECT Name FROM Largest_banks  LIMIT 5'
run_query(query_statement, sql_connection)

log_progress('Proccesing complete')

sql_connection.close()