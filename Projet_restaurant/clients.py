from database_handler import *

class Client:
    def __init__(self, id, prenom, nom, telephone):
        self.id = id
        self.prenom = prenom
        self.nom = nom
        self.telephone = telephone

    def __str__(self):
        return f"{self.id}: {self.prenom} {self.nom}, Téléphone: {self.telephone}"

    @staticmethod
    def ajouter_client(database, prenom, nom, telephone):
        try:
            get_client(database, prenom, nom, telephone)
            print(f"Client ajouté : {prenom} {nom}")
        except sqlite3.Error as e:
            print(f"Erreur SQL : {e}")

    @staticmethod
    def afficher_clients(database):
        try:
            clients_data = select_client(database)
            clients = [Client(*data) for data in clients_data]
            for client in clients:
                print(client)
        except sqlite3.Error as e:
            print(f"Erreur SQL : {e}")

    @staticmethod
    def supprimer_client(database, client_id):
        from reservations import Reservation
        reservations = select_id_reserv_client(database, client_id)
        for reserv in reservations:
            Reservation.supprimer_reservation(database, reserv[0])
        delete_client_by_id(database, client_id)
        print(f"Client {client_id} supprimé.")

    @staticmethod
    def modifier_client(database, client_id, nouveau_prenom, nouveau_nom, nouveau_telephone):
        try:
            update_client(database,nouveau_prenom, nouveau_nom, nouveau_telephone, client_id)
            print(f"Client {client_id} modifié : {nouveau_prenom} {nouveau_nom}, Téléphone: {nouveau_telephone}")
        except sqlite3.Error as e:
            print(f"Erreur SQL : {e}")