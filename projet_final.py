# -*- coding: utf-8 -*-
import sqlite3 as sql

DATABASE = 'restaurant.db'


def fetch_data(query):
    """Exécute une requête SQL et retourne les résultats."""

    try:
        # Établit une connexion à la base de données en utilisant 'with' pour une gestion automatique de la connexion
        with sql.connect(DATABASE) as con:
            # Crée un curseur qui permet d'interagir avec la base de données
            cur = con.cursor()
            
            con.text_factory = lambda x: str(x, "utf-8")

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
    #Tables
    table = fetch_data("Select * from tables") #requête sql
    for i in table:
        if i[2] == 1:
            dispo = "disponible"
            print(f"Table numéro : {i[1]} est {dispo}")
        else:
            print(f"La table numéro : {i[1]} n'est pas disponible ! ")
    return "\n"

def watch_reservation():
    """Affiche les réservations en cour"""
    print("\n-----Réservation en cour-----")
    reserv = fetch_data(" SELECT T.numero, T.disponible, R.id, R.date, R.heure, R.client_id, R.table_id,C.prenom, C.nom, C.telephone, C.id, R.nombre_personne "
                        " FROM tables AS T "
                        " JOIN reservations AS R on T.id = R.table_id "
                        " JOIN clients AS C on C.id = R.client_id ")
    ecrit = ""
    for i in reserv:
        if i[1] == 0:
            ecrit += (f"La réservation : {i[2]}. le numéro de la table est : {i[0]} le : {i[3]} à {i[4]} par {i[7]} {i[8]} son numéro de téléphone est : {i[9]} pour {i[11]} personnes\n")
        else:
            return ("Pas de réservation en cour")
    return ecrit
            
def watch_reser_date():
    """Affiche les réservations en cours en fonction de la date et de l'heure"""
    print("----Affichage en fonction de l'heure----")
    ask_date = input("Entrer la date souhaitée : ")
    reserv = fetch_data(" SELECT T.numero, T.disponible, R.id, R.date, R.heure, R.client_id, R.table_id, C.nom, C.telephone, C.id "
                        " FROM tables AS T "
                        " JOIN reservations AS R on T.id = R.table_id "
                        " JOIN clients AS C on C.id = R.client_id ")
    for i in reserv:
        if ask_date == i[2]:
            print(f"le numéro de la table est : {i[0]} à : {i[3]} par {i[6]} son numéro de téléphone est : {i[7]}")
        else:
            print("Pas de reservation à cette date / heure ci")


def watch_client():
    """Affiche les clients"""
    client = fetch_data("SELECT id, prenom, nom, telephone from clients ")
    ecrit = ''
    for i in client:
        ecrit += (f"{i[0]}-{i[1]}-{i[2]}-{i[3]} \n")

    return ecrit


def add_reservation():
    conn = sql.connect("restaurant.db")
    cur = conn.cursor()
    """Ajouter une réservation."""
    print("--- Ajout d'une nouvelle réservation ---")
    client_ids = watch_client()
    print(client_ids)
    table = watch_table()
    print(table)
    client_id = int(input("Entrer l'id du client pour la réservation : "))
    num_table = int(input("Entrez le numéro de la table : "))
    nombre_personne = int(input("Entrez le nombre de personnes : "))
    heure = input("Entrez l'heure (format HH:MM) : ")
    date = input("Entrez la date (format DD/MM/YYYY) : ")

    # Insérer la réservation dans la base de données
    cur.execute(
        "INSERT INTO reservations (client_id, table_id, nombre_personne, heure, date) VALUES (?, ?, ?, ?, ?)",
            (client_id, num_table, nombre_personne, heure, date)
            )
    cur.execute("UPDATE tables set disponible = 0 WHERE id = ?", (num_table,))
    print("Réservation ajoutée avec succès.")
    conn.commit()
    conn.close()

def add_client():
    conn = sql.connect("restaurant.db")
    cursor = conn.cursor()
    prenom = input("Prénom: ")
    nom = input('Nom: ')
    num_telephone = input('Téléphone: ')
    cursor.execute("INSERT OR IGNORE INTO clients (prenom, nom, telephone) VALUES (?, ?, ?)", (prenom, nom, num_telephone))
    conn.commit()
    conn.close()

def delete_reservation():
    """Supprimer réservation"""
    conn = sql.connect("restaurant.db")
    cur = conn.cursor()
    supp = watch_reservation()
    print(supp)
    id_supp = int(input("Entrer l'id de la réservation que vous voulez supprimer : "))
    id_table = cur.execute("SELECT table_id FROM reservations WHERE id = ?", (id_supp,)).fetchone()[0]
    cur.execute("DELETE FROM reservations WHERE id = ?", (id_supp,))
    cur.execute("UPDATE tables set disponible = 1 WHERE id = ?", (id_table,))
    print(f'La réservation à bien été supprimée : {id_supp}')
    conn.commit()
    conn.close()


def delete_client():
    """Supprimer un client"""
    conn = sql.connect("restaurant.db")
    cur = conn.cursor()
    supp = watch_client()
    print(supp)
    id_supp = int(input("Entrer l'id du client que vous voulez supprimer : "))
    id_reserv = cur.execute("SELECT id FROM reservations WHERE client_id = ?", (id_supp,)).fetchone()[0]
    id_table = cur.execute("SELECT table_id FROM reservations WHERE id = ?", (id_reserv,)).fetchone()[0]
    cur.execute("DELETE FROM reservations WHERE id = ?", (id_reserv,))
    # Supprimer le client de la table clients
    cur.execute("DELETE FROM clients WHERE id = ?", (id_supp,))
    cur.execute("Update tables set disponible = 1 where id = ?", (id_table,))
    conn.commit()
    conn.close()
    print(f"Le client avec l'ID {id_supp} a bien été supprimé.")


def modify_reservation():
    """Modifier une réservation"""
    conn = sql.connect("restaurant.db")
    cur = conn.cursor()
    affichage = watch_reservation()
    print(affichage)
    modif_reserv = int(input("Entrer l'id de la réservation à modifier : "))
    nouvelle_date = input("Entrez la nouvelle date (format DD/MM/YYYY) : ")
    nouvelle_heure = input("Entrez la nouvelle heure (format HH:MM) : ")
    nouveau_nombre_personne = input("Entrez le nombre de personnes : ")

    cur.execute("UPDATE reservations SET date = ?, heure = ?, nombre_personne = ? WHERE id = ?",(nouvelle_date, nouvelle_heure, nouveau_nombre_personne, modif_reserv))
    conn.commit()

    print(f"La réservation avec l'ID {modif_reserv} a été modifiée avec succès.")
    conn.commit()
    conn.close()

def modif_client():
    """Modifier une client"""
    conn = sql.connect("restaurant.db")
    cur = conn.cursor()
    affichage = watch_client()
    print(affichage)
    modif_id_client = int(input("Entrer l'id du client à modifier : "))
    nouveau_prenom = input("Entrez le nouvelle prenom : ")
    nouveau_nom = input("Entrez le nouvelle nom : ")
    nouveau_telephone = input("Entrez le telephone : ")
    cur.execute("UPDATE clients SET prenom = ?, nom = ?, telephone = ? WHERE id = ?", (nouveau_prenom, nouveau_nom, nouveau_telephone, modif_id_client))
    print(f"Ancienne version : {affichage}")
    print(f"Version modifier : {nouveau_prenom}, {nouveau_nom}, {nouveau_telephone}")
    conn.commit()
    conn.close()

if __name__ == "__main__":
