#import streamlit as st
import psycopg2
from dotenv import load_dotenv
import os
import pandas as pd

def BancoPostgres():
    # Carregar as variáveis de ambiente do arquivo .env
    load_dotenv('PROJETO-STREAMLIT/bancoemp.env')

    # Obter os valores das variáveis de ambiente
    DB_HOST = os.getenv("DB_HOST")
    DB_DATABASE = os.getenv("DB_DATABASE")
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")

    # Usar as variáveis de ambiente para conectar ao banco de dados
    conn = psycopg2.connect(
    host=DB_HOST,
    port=5432,
    database=DB_DATABASE,
    user=DB_USER,
    password=DB_PASSWORD)
    return conn

conn = BancoPostgres()
#CONSULTA NO BANCO
cur = conn.cursor()
cur.execute("SELECT DISTINCT nome, no_funcao FROM public.usuarios")
rows = cur.fetchall()

# Mostrar o resultado da consulta em uma tabela
df = pd.DataFrame(rows, columns=[desc[0] for desc in cur.description])
print(df)

# # Fechar a conexão e o cursor
cur.close()
conn.close()
