from database_handler import *
from tables import Table
from clients import Client


class Reservation:
    def __init__(self, id, client, table, nombre_personnes, date, heure):
        self.id = id
        self.client = client
        self.table = table
        self.nombre_personnes = nombre_personnes
        self.date = date
        self.heure = heure

    def __str__(self):
        return (f"Réservation {self.id}: Client {self.client.prenom} {self.client.nom}, "
                f"Table {self.table.numero}, {self.date} à {self.heure}, "
                f"pour {self.nombre_personnes} personnes")

    @staticmethod
    def afficher_reservations(database):
        try:
            reservations_data = get_reservations(database)
            reservations = [
                Reservation(res[0], Client(res[4], res[5], res[6], None), Table(res[7], res[8]), res[3], res[1], res[2])
                for res in reservations_data
            ]
            for reservation in reservations:
                print(reservation)
        except sqlite3.Error as e:
            print(f"Erreur SQL : {e}")

    @staticmethod
    def ajouter_reservation(database, client_id, table_id, nombre_personne, date, heure):
        from clients import Client
        try:
            tables_disponibles = Table.get_tables_disponibles(database, date, heure)
            if table_id not in [table.id for table in tables_disponibles]:
                print(f"Table {table_id} non disponible.")
                return
            add_reservation(database, client_id, date, heure, table_id, nombre_personne)
            print(f"Réservation ajoutée pour le client {client_id}.")
        except sqlite3.Error as e:
            print(f"Erreur SQL : {e}")

    @staticmethod
    def supprimer_reservation(database, reservation_id):
        try:
            delete_commande_of_reservation(database, reservation_id)
            delete_reservation(database, reservation_id)
            print(f"Réservation {reservation_id} supprimée.")
        except sqlite3.Error as e:
            print(f"Erreur SQL : {e}")

    @staticmethod
    def modifier_reservation(database, reservation_id, nouvelle_date, nouvelle_heure, table_id, nombre_personnes):
        try:
            tables_disponibles = Table.get_tables_disponibles(database, nouvelle_date, nouvelle_heure)
            if table_id not in [table.id for table in tables_disponibles]:
                print(f"Table {table_id} non disponible pour {nouvelle_date} à {nouvelle_heure}.")
                return

            modify_reservation(database, table_id, nombre_personnes, nouvelle_date, nouvelle_heure, reservation_id)
            print(f"Réservation {reservation_id} modifiée avec succès.")
        except sqlite3.Error as e:
            print(f"Erreur SQL : {e}")