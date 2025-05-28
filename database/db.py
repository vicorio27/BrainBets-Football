import sqlite3

con = sqlite3.connect("tutorial.db")


def create_team_standing_table():
    cur = con.cursor()
    cur.execute("CREATE TABLE team_standing(title, year, score)")
