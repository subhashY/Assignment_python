import sqlite3

__all__ = ('get_connection')


def get_connection():
    try:
        con = sqlite3.connect('assignment.db')
        cur = con.cursor()
        cur.execute("create table IF NOT EXISTS exceltojson (id, data)")
        return con
    except BaseException as excep:
        return excep
