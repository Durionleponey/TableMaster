import json

def prise_de_commande_line():

    # Charger les fichiers JSON
    with open("Plats.json", "r", encoding="UTF-8") as list_plats:
        plats = json.load(list_plats)

    with open("Tables.json", "r", encoding="UTF-8") as list_tables:
        tables = json.load(list_tables)

    # Afficher les tables réservées avec leurs informations
    print("Tables réservées :")
    for key, table in tables.items():
        if not table["statut"]:
            print(
                f'Table {table["numero"]} réservée par {table["reservation"]["prenom"]} {table["reservation"]["nom"]} à {table["reservation"]["heure_arrivee"]}')

    # Demander à l'utilisateur de choisir une table
    choose_table = input("Choisissez votre table : ")

    # Vérifier si la table est disponible
    table_trouvee = None
    for key, table in tables.items():
        if choose_table == str(table["numero"]) and table["statut"] == False:
            table_trouvee = table
            break

    if table_trouvee is None:
        print("Erreur : la table n'est pas réservée ou n'existe pas !")
    else:
        # Afficher la liste des plats
        print("\nListe des plats disponibles :")
        for plat in plats["Plats"]:
            print(f"{plat['Numéro']} - {plat['Nom']}")

        # Initialiser la commande
        commande = []

        # Boucle pour ajouter des plats
        while True:
            # Demander le numéro du plat
            num_plat = input("\nEntrez le numéro du plat à ajouter (ou 'fin' pour terminer) : ")

            # Vérifier si l'utilisateur a fini de commander
            if num_plat.lower() == 'fin':
                break

            # Rechercher le plat dans la liste
            plat_trouve = None
            for plat in plats["Plats"]:
                if num_plat == str(plat['Numéro']):
                    plat_trouve = plat
                    break

            # Ajouter le plat à la commande
            if plat_trouve:
                commande.append(plat_trouve['Nom'])
                print(f"{plat_trouve['Nom']} ajouté à la commande.")
            else:
                print("Numéro de plat invalide.")

        # Mettre à jour la commande dans le fichier Tables.json
        for key, table in tables.items():
            if str(table['numero']) == choose_table:
                table['reservation']['commande'] = ', '.join(commande)

        # Sauvegarder les modifications
        with open("Tables.json", "w", encoding="UTF-8") as f:
            json.dump(tables, f, ensure_ascii=False, indent=2)

        print("\nCommande enregistrée avec succès !")
        print(f"Commande de la table {choose_table} : {', '.join(commande)}")