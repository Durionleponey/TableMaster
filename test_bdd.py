import sqlite3 as sql

DATABASE = "TableMaster.db"

def fetch_data(query):
    """Exécute une requête SQL et retourne les résultats."""
    try:
        with sql.connect(DATABASE) as con:
            cur = con.cursor()
            cur.execute(query)
            return cur.fetchall()
    except sql.Error as e:
        print(f"Erreur lors de l'exécution de la requête : {e}")
        return []

def display_all_data():
    """Affiche les données des trois tables."""
    # Tables
    print("\n--- Tables ---")
    tables = fetch_data("SELECT idtable, statut FROM tables")
    for table in tables:
        print(f"Table ID: {table[0]}, Statut: {'Libre' if table[1] else 'Occupée'}")

    # Réservations
    print("\n--- Réservations ---")
    reservations = fetch_data("""
        SELECT 
            Reservations.id, Reservations.idtable, Reservations.nom, 
            Reservations.prenom, Reservations.nombre_personnes, 
            Reservations.numero_de_telephone, Reservations.heure_arrivee, 
            Reservations.commande, tables.statut
        FROM Reservations
        JOIN tables ON Reservations.idtable = tables.idtable
    """)
    for res in reservations:
        print(f"Réservation ID: {res[0]}, Table ID: {res[1]}, Nom: {res[2]}, Prénom: {res[3]}, "
              f"Personnes: {res[4]}, Téléphone: {res[5]}, Heure d'arrivée: {res[6]}, "
              f"Commande: {res[7]}, Statut: {'Libre' if res[8] else 'Occupée'}")

    # Commandes
    print("\n--- Commandes ---")
    commandes = fetch_data("SELECT platId, labelplat, priceplat FROM Commandes")
    for cmd in commandes:
        print(f"Plat ID: {cmd[0]}, Nom: {cmd[1]}, Prix: {cmd[2]} €")

if __name__ == "__main__":
    display_all_data()
