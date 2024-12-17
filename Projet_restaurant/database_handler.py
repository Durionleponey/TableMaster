import sqlite3

class DatabaseHandler:
    def __init__(self, database):
        self.database = database

    def execute_query(self, query, params=()):
        try:
            with sqlite3.connect(self.database) as conn:
                cur = conn.cursor()
                cur.execute(query, params)
                conn.commit()
                return cur.fetchall()
        except sqlite3.Error as e:
            print(f"Erreur SQL : {e}")
            return []


def get_client(database, prenom, nom, telephone) :
    database.execute_query("INSERT INTO clients (prenom, nom, telephone) VALUES (?, ?, ?)", (prenom, nom, telephone))