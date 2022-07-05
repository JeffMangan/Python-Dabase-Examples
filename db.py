import psycopg2

conn = psycopg2.connect('postgresql://mangan@localhost/test')
conn.autocommit = True
