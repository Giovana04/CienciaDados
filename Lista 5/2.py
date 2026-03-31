import sqlite3 
import pandas as pd

con = sqlite3.connect("mydata.sqlite")
con.execute("""
            CREATE TABLE IF NOT EXISTS test (id INTEGER, nome TEXT)""")
con.execute("INSERT INTO test (id,nome) VALUES (1, 'ana')")
con.execute("INSERT INTO test (id,nome) VALUES (2, 'maria')")
con.commit()
cursor = con.execute("SELECT * FROM test")
rowa = cursor.fetchall()
df = pd.DataFrame((rowa), columns=[x[0] for x in cursor.description])

print(df)
con.close()