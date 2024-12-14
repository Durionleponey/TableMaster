import sqlite3
from tkinter import messagebox


class Client:
    def __init__(self, prenom,  nom, telephone):
        self.prenom = prenom
        self.nom = nom
        self.telephone = telephone

    def __str__(self):
        return f"Client: {self.prenom} {self.nom}, Téléphone: {self.telephone}"

class Reservation:
    def __init__(self, client, nombre_personnes, heure):
        self.client = client
        self.nombre_personnes = nombre_personnes
        self.heure = heure


    def __str__(self):
        return f"Réservation pour {self.client.prenom} {self.client.nom} le {self.heure} pour {self.nombre_personnes} personnes."

class Table:
    def __init__(self, numero_table, nombre_places):
        self.numero_table = numero_table
        self.nombre_places = nombre_places

    def __str__(self):
        return f"Table: {self.numero_table} possède {self.nombre_places} places."
class Plat:
    def __init__(self, nom, prix):
        self.nom = nom
        self.prix = prix

    def __str__(self):
        return f"{self.nom} : {self.prix}€"

class Menu:
    def __init__(self):
        self.plats = []

    def ajouter_plat(self, plat):
        self.plats.append(plat)

    def afficher_menu(self):
        print("Menu :")
        for plat in self.plats:
            print(f"- {plat}")

class Commande:
    def __init__(self, client):
        self.client = client
        self.plats_commandes = []

    def ajouter_plat(self, plat):
        self.plats_commandes.append(plat)

    def calculer_total(self):
        return sum(plat.prix for plat in self.plats_commandes)

    def __str__(self):
        plats = ", ".join(plat.nom for plat in self.plats_commandes)
        return f"{plats}. Total: {self.calculer_total()}€ \n"

class Restaurant:
    def __init__(self, nom):
        self.nom = nom
        self.menu = Menu()
        self.reservations = []
        self.commandes = []

    def ajouter_reservation(self, reservation):
        self.reservations.append(reservation)

    def ajouter_commande(self, commande):
        self.commandes.append(commande)

    def afficher_reservations(self):
        print("Réservations :")
        for reservation in self.reservations:
            print(reservation)

    def afficher_commandes(self):
        print("Commandes :")
        for commande in self.commandes:
            print(commande)



def mainLine():

    # Créer un restaurant
    mon_restaurant = Restaurant("Gaston Gourmet")

    # Ajouter des plats au menu
    plat1 = Plat("Spaghetti Bolognese", 12)
    plat2 = Plat("Pizza Margherita", 10)
    mon_restaurant.menu.ajouter_plat(plat1)
    mon_restaurant.menu.ajouter_plat(plat2)

    # Créer une table
    table1 = Table(1, 5)

    # Afficher le menu
    mon_restaurant.menu.afficher_menu()

    # Ajouter une réservation
    client1 = Client("Tiago", "Carmo Silveirinha", "0483437772")
    reservation1 = Reservation(client1, 2, "19:00")
    mon_restaurant.ajouter_reservation(reservation1)

    # Créer une commande
    commande1 = Commande(client1)
    commande1.ajouter_plat(plat1)
    commande1.ajouter_plat(plat2)
    mon_restaurant.ajouter_commande(commande1)

    # Afficher les réservations et les commandes
    mon_restaurant.afficher_reservations()
    mon_restaurant.afficher_commandes()
