import psycopg2

conn = psycopg2.connect('postgresql://dfdfd@localhost/test')
conn.autocommit = True
