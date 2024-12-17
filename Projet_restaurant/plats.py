from database_handler import *

class Plat:
    def __init__(self, id, nom, prix):
        self.id = id
        self.nom = nom
        self.prix = prix

    def __str__(self):
        return f"{self.id}: {self.nom} - {self.prix}€"

    @staticmethod
    def afficher_menu(database):
        try:
            plats_data = database.execute_query("SELECT id, nom, prix FROM menu")
            plats = [Plat(*data) for data in plats_data]
            for plat in plats:
                print(plat)
        except sqlite3.Error as e:
            print(f"Erreur SQL : {e}")

    @staticmethod
    def ajouter_plat(database, nom, prix):
        try:
            database.execute_query("INSERT INTO menu (nom, prix) VALUES (?, ?)", (nom, prix))
            print(f"Plat ajouté : {nom} - {prix}€")
        except sqlite3.Error as e:
            print(f"Erreur SQL : {e}")

    @staticmethod
    def supprimer_plat(database, plat_id):
        try:
            database.execute_query("DELETE FROM menu WHERE id = ?", (plat_id,))
            print(f"Plat {plat_id} supprimé.")
        except sqlite3.Error as e:
            print(f"Erreur SQL : {e}")

    @staticmethod
    def modifier_plat(database, plat_id, nouveau_nom, nouveau_prix):
        try:
            database.execute_query(
                "UPDATE menu SET nom = ?, prix = ? WHERE id = ?",
                (nouveau_nom, nouveau_prix, plat_id)
            )
            print(f"Plat {plat_id} modifié en {nouveau_nom} - {nouveau_prix}€.")
        except sqlite3.Error as e:
            print(f"Erreur SQL : {e}")