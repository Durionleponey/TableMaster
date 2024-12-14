import sqlite3 as sql
from main import *
DATABASE = 'restaurant.db'


def fetch_data(query):
    """Exécute une requête SQL et retourne les résultats."""

    try:
        # Établit une connexion à la base de données en utilisant 'with' pour une gestion automatique de la connexion
        with sql.connect(DATABASE) as con:
            # Crée un curseur qui permet d'interagir avec la base de données
            cur = con.cursor()

            # Exécute la requête SQL passée en paramètre
            cur.execute(query)

            # Récupère toutes les lignes résultantes de la requête exécutée
            return cur.fetchall()

    except sql.Error as e:
        # En cas d'erreur SQL, affiche un message d'erreur dans le terminal
        print(f"Erreur lors de l'exécution de la requête : {e}")

        # Si une erreur survient, retourne une liste vide
        return []


def watch_table():
    """Affiche les valeurs des tables"""
    # Tables
    print("\n--------Tables----------")
    table = fetch_data("Select * from tables")  # requête sql
    for i in table:
        if i[2] == 0:
            dispo = "disponible"
        else:
            dispo = "non disponible"
        print(f"Table numéro : {i[1]} est {dispo}")


def watch_reservation():
    """Affiche les réservations en cour"""
    print("\n-----Réservation en cour-----")
    reserv = fetch_data(
        " SELECT T.numero, T.disponible, R.date_heure, R.client_id, R.table_id, C.nom, C.telephone, C.id "
        " FROM tables AS T "
        " JOIN reservations AS R on T.id = R.table_id "
        " JOIN clients AS C on C.id = R.client_id ")
    for i in reserv:
        if i[1] == 0:
            print(f"le numéro de la table est : {i[0]} à : {i[2]} par {i[5]} son numéro de téléphone est : {i[6]}")
        else:
            print("Pas de réservation en cour")
def client():
    conn = sqlite3.connect("restaurant.db")
    cursor = conn.cursor()
    prenom = input("Prénom: ")
    nom = input('Nom: ')
    num_telephone = input('Téléphone: ')
    client1 = Client(prenom, nom, num_telephone)
    cursor.execute("INSERT OR IGNORE INTO clients (prenom, nom, telephone) VALUES (?, ?, ?)", (client1.prenom, client1.nom, client1.telephone))
    conn.commit()
    conn.close()


