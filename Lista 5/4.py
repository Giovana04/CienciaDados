import sqlalchemy as sqla

engine = sqla.create_engine("sqlite:///novo_banco.sqlite")
with engine.connect() as conn: conn.execute(sqla.text(""" 
                          create table if not exists usuarios (
                              id integer primary key, 
                              nome TEXT, 
                              idade integer)
                          """))
with engine.connect() as conn:
    conn.execute(sqla.text("""
                           insert into usuarios (nome,idade)
                           values ('ana',25), ('bruno',30), ('carla',22)"""))
    conn.commit()

import pandas as pd
df = pd.read_sql(sqla.text("select * from usuarios"), engine)
print(df)