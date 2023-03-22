import streamlit as st
import psycopg2

#CONECTOR COM BANCO
conn = psycopg2.connect(
    host="localhost",
    database="db_streamlit",
    user="postgres",
    password=";Plansul2021"
)
#st.title("USUÁRIOS")

#CONSULTA NO BANCO
cur = conn.cursor()
cur.execute("SELECT * FROM public.usuarios")
rows = cur.fetchall()
for row in rows:
    print(row)
    