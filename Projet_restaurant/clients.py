from restaurant import *

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
            database.execute_query("INSERT INTO clients (prenom, nom, telephone) VALUES (?, ?, ?)", (prenom, nom, telephone))
            print(f"Client ajouté : {prenom} {nom}")
        except sqlite3.Error as e:
            print(f"Erreur SQL : {e}")

    @staticmethod
    def afficher_clients(database):
        try:
            clients_data = database.execute_query("SELECT id, prenom, nom, telephone FROM clients")
            clients = [Client(*data) for data in clients_data]
            for client in clients:
                print(client)
        except sqlite3.Error as e:
            print(f"Erreur SQL : {e}")

    @staticmethod
    def supprimer_client(database, client_id):
        reservations = database.execute_query("SELECT id FROM reservations WHERE client_id = ?", (client_id,))
        for reserv in reservations:
            Reservation.supprimer_reservation(database, reserv[0])
        database.execute_query("DELETE FROM clients WHERE id = ?", (client_id,))
        print(f"Client {client_id} supprimé.")

    @staticmethod
    def modifier_client(database, client_id, nouveau_prenom, nouveau_nom, nouveau_telephone):
        try:
            database.execute_query(
                "UPDATE clients SET prenom = ?, nom = ?, telephone = ? WHERE id = ?",
                (nouveau_prenom, nouveau_nom, nouveau_telephone, client_id)
            )
            print(f"Client {client_id} modifié : {nouveau_prenom} {nouveau_nom}, Téléphone: {nouveau_telephone}")
        except sqlite3.Error as e:
            print(f"Erreur SQL : {e}")