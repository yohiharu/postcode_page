#!/usr/bin/python3

import sqlite3

def create_table(name):
    con = sqlite3.connect(name)
    con.execute("CREATE TABLE IF NOT EXISTS codes (code)")
    con.close()
