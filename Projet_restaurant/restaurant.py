import sqlite3
from database_handler import DatabaseHandler  # Nouveau fichier pour la gestion DB
from plats import Plat
from tables import Table
from clients import Client
from commandes import Commande
from reservations import Reservation


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

database = DatabaseHandler("restaurant.db")
