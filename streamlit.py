import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="db_streamlit",
    user="postgres",
    password=";Plansul2021"
)

cur = conn.cursor()

cur.execute("SELECT * FROM public.usuarios")

rows = cur.fetchall()

for row in rows:
    print(row)