from database_handler import *

class Client:
    def __init__(self, id, prenom, nom, telephone):
        self._id = id
        self._prenom = prenom
        self._nom = nom
        self._telephone = telephone


    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        raise AttributeError("L'ID ne peut pas être modifié!")

    @property
    def prenom(self):
        return self._prenom


    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, value):
        self._nom = value

    @property
    def telephone(self):
        return self._telephone


    def __str__(self):
        return f"{self._id}: {self._prenom} {self._nom}, Téléphone: {self._telephone}"

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