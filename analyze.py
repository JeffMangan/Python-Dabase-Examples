import sys

from db import conn


def main():
    if len(sys.argv) != 2:
        print(
            "Usage: {} SYMBOL".format(sys.argv[0]),
            file=sys.stderr
        )
        sys.exit(1)

    symbol = sys.argv[1]

    cur = conn.cursor()
    cur.execute(
        """
        SELECT max(value) FROM index_values WHERE symbol = %s;
        """,
        [sys.argv[1]]
    )

    row = cur.fetchone()

    if row[0] is None:
        print("No such symbol {}".format(symbol))
    else:
        print("Max for {} is {}".format(symbol, row[0]))


if __name__ == '__main__':
    main()
