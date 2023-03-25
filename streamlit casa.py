#import streamlit as st
import psycopg2
from dotenv import load_dotenv
import os
import pandas as pd

def BancoPostgres():
    # Carregar as variáveis de ambiente do arquivo .env
    load_dotenv('E:\PROJETO STREAMLIT\PROJETO-STREAMLIT/banco.env')

    # Obter os valores das variáveis de ambiente
    DB_HOST = os.getenv("DB_HOST")
    DB_DATABASE = os.getenv("DB_DATABASE")
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")

    # Usar as variáveis de ambiente para conectar ao banco de dados
    conn = psycopg2.connect(
    host=DB_HOST,
    database=DB_DATABASE,
    user=DB_USER,
    password=DB_PASSWORD)
    return conn

conn = BancoPostgres()
#CONSULTA NO BANCO
cur = conn.cursor()
cur.execute("select * from erp_sistema.clientes")
rows = cur.fetchall()

# Mostrar o resultado da consulta em uma tabela
df = pd.DataFrame(rows, columns=[desc[0] for desc in cur.description])
print(df)

# # Fechar a conexão e o cursor
cur.close()
conn.close()
