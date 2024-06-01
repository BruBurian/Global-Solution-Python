import oracledb
import json

def conectar():
    return oracledb.connect("rm552863/050305@oracle.fiap.com.br:1521/orcl")

def cadastrar_usuario(nome_empresa, email, senha):
    conn = conectar()
    cursor = conn.cursor()
    try:
        cursor.execute("""
        INSERT INTO usuarios (nome_empresa, email, senha)
        VALUES (:1, :2, :3)
        """, (nome_empresa, email, senha))
        conn.commit()
    except oracledb.DatabaseError as e:
        print(f"Erro ao cadastrar usuário: {e}")
    finally:
        cursor.close()
        conn.close()
