import streamlit as st
import psycopg2

#CONECTOR COM BANCO
conn = psycopg2.connect(
    host= st.secrets['host'],
    database= st.secrets['database'],
    user= st.secrets['user'],
    password=st.secrets['senha']
)
#st.title("USUÁRIOS")

#CONSULTA NO BANCO
cur = conn.cursor()
cur.execute("SELECT * FROM public.usuarios")
rows = cur.fetchall()
for row in rows:
    print(row)
    