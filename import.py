import csv
import multiprocessing
import time

import psycopg2.extras
import requests

from db import conn

cur = conn.cursor()

cur.execute("TRUNCATE TABLE index_values;")


def load_index(symbol):
    response = requests.get(
        "https://fred.stlouisfed.org/graph/fredgraph.csv?id={}".format(symbol)
    )
    response.raise_for_status()
    rows = csv.reader(response.text.splitlines())
    # skip the headers
    next(rows)

    values = []

    for row in rows:
        if row[1] == '.':
            continue
        values.append([symbol, row[0], row[1]])

    psycopg2.extras.execute_values(
        cur,
        """
        INSERT INTO index_values (symbol, date, value)
        VALUES %s;
        """,
        values,
    )


t = time.time()
indexes = ['SP500', 'DJIA', 'NASDAQCOM']
with multiprocessing.Pool(5) as p:
    p.map(load_index, indexes)
print('elapsed', time.time() - t)

cur.close()
conn.close()
