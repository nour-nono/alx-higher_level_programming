"""
This script connects to a MySQL database and fetches all rows from
the 'states' table,ordered by the 'id' column. The script expects
the database credentials as command-line
arguments: the username, password, and database name.
"""
#!/usr/bin/python3
if __name__ == "__main__":
    import MySQLdb
    import sys

    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC;")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
