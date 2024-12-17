from database_handler import *

class Table:
    def __init__(self, id, numero):
        self.id = id
        self.numero = numero

    def __str__(self):
        return f"Table {self.numero}"

    @staticmethod
    def afficher_tables(database):
        try:
            tables_data = database.execute_query("SELECT id, numero FROM tables")
            tables = [Table(*data) for data in tables_data]
            for table in tables:
                print(f"Id : {table.id} -- {table}")
        except sqlite3.Error as e:
            print(f"Erreur SQL : {e}")

    @staticmethod
    def ajouter_table(database, numero):
        try:
            database.execute_query("INSERT INTO tables (numero) VALUES (?)", (numero,))
            print(f"Table {numero} ajoutée.")
        except sqlite3.Error as e:
            print(f"La table {numero} existe déjà.")

    @staticmethod
    def supprimer_table(database, table_id):
        try:
            reservations = database.execute_query("SELECT id FROM reservations WHERE table_id = ?", (table_id,))
            if reservations:
                print(f"La table {table_id} est associée à des réservations et ne peut pas être supprimée.")
                return

            database.execute_query("DELETE FROM tables WHERE id = ?", (table_id,))
            print(f"Table {table_id} supprimée.")
        except sqlite3.Error as e:
            print(f"Erreur SQL : {e}")

    @staticmethod
    def get_tables_disponibles(database, date, heure):
        tables_data = database.execute_query(
            """
            SELECT T.id, T.numero
            FROM tables AS T
            WHERE NOT EXISTS (
                SELECT 1 FROM reservations AS R
                WHERE R.table_id = T.id AND R.date = ? AND (
                    (R.heure BETWEEN ? AND TIME(?, '+2 hours')) OR
                    (TIME(R.heure, '+2 hours') > ? AND R.heure < ?)
                )
            )
            """,
            (date, heure, heure, heure, heure)
        )
        return [Table(*data) for data in tables_data]

    @staticmethod
    def afficher_tables_disponibles(database, date, heure):
        try:
            tables_disponibles = Table.get_tables_disponibles(database, date, heure)
            if not tables_disponibles:
                print("Aucune table disponible pour cette date et heure.")
            else:
                print(f"Tables disponibles pour le {date} à {heure}:")
                for table in tables_disponibles:
                    print(table)
        except sqlite3.Error as e:
            print(f"Erreur SQL : {e}")