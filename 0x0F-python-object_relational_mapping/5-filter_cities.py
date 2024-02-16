#!/usr/bin/python3
"""
This script connects to a MySQL database and fetches all rows from
the 'states' table,ordered by the 'id' column. The script expects
the database credentials as command-line
arguments: the username, password, and database name.
"""
if __name__ == "__main__":
    import MySQLdb
    import sys

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT name"
                " FROM cities"
                " WHERE state_id IN ("
                " SELECT id"
                " FROM states"
                ")"
                " ORDER BY id")
    rows = cur.fetchall()
    ls = ", ".join([x for x in rows])
    print(ls)
    cur.close()
    db.close()
