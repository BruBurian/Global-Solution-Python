def imports():
    import json
    import oracledb
    import pandas as pd
    from sqlalchemy import create_engine

def conexao():
    data = pd.read.csv('arquivo.csv')

with open('secret.txt') as file:
    secret = json.load(file)

usuario = secret['user']
senha = secret['password']
oracle = secret['dsn']

with oracledb.connect(user=usuario, password=senha, dsn=oracle) as connection:
    engine = create_engine('oracle+oracledb://', creator=lambda: connection)
    data.to_sql('gs', engine, if_exists='replace', index=False)