#!/usr/bin/python3
"""Connects to MySQL and lists all states from the database hbtn_0e_6_usa"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Replace with your real credentials
    user = "root"
    password = "louis"
    db_name = "hbtn_0e_6_usa"

    # Connect to MySQL
    db = MySQLdb.connect(host="localhost", user=user, passwd=password, db=db_name)
    cur = db.cursor()

    # Execute query
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch and print results
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Clean up
    cur.close()
    db.close()
