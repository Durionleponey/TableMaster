from restaurant import *

class Commande:

    @staticmethod
    def ajouter_commande(database, reservation_id, table_id, plat_id, quantite):
        try:
            database.execute_query(
                "INSERT INTO commandes (reserv_id, table_id, plat_id, quantite) VALUES (?, ?, ?, ?)",
                (reservation_id, table_id, plat_id, quantite)
            )
            print(f"Commande ajoutée pour la réservation {reservation_id}.")
        except sqlite3.Error as e:
            print(f"Erreur SQL : {e}")

    @staticmethod
    def afficher_commandes(database, reservation_id):
        try:
            commandes_data = database.execute_query(
                """
                SELECT C.id, M.nom, C.quantite, M.prix
                FROM commandes AS C
                JOIN menu AS M ON C.plat_id = M.id
                WHERE C.reserv_id = ?
                """,
                (reservation_id,)
            )
            total = 0
            for commande in commandes_data:
                id_commande, nom, quantite, prix = commande
                total += quantite * prix
                print(f"Commande {id_commande}: {nom}, Quantité: {quantite}, Prix: {prix}€, Total: {quantite * prix}€")
            print(f"Total: {total}€")
        except sqlite3.Error as e:
            print(f"Erreur SQL : {e}")

    @staticmethod
    def modifier_commande(database, commande_id, nouveau_plat_id, nouvelle_quantite):
        try:
            database.execute_query(
                "UPDATE commandes SET plat_id = ?, quantite = ? WHERE id = ?",
                (nouveau_plat_id, nouvelle_quantite, commande_id)
            )
            print(f"Commande {commande_id} modifiée avec succès.")
        except sqlite3.Error as e:
            print(f"Erreur SQL : {e}")

    @staticmethod
    def supprimer_commande(database, commande_id):
        try:
            database.execute_query("DELETE FROM commandes WHERE id = ?", (commande_id,))
            print(f"Commande {commande_id} supprimée.")
        except sqlite3.Error as e:
            print(f"Erreur SQL : {e}")

    @staticmethod
    def table_id_via_reservation_id(database, reservation_id):
        try:
            table_id = database.execute_query("SELECT table_id FROM reservations WHERE id = ?", (reservation_id,))
            return table_id[0][0]
        except sqlite3.Error as e:
            print(f"Erreur SQL : {e}")