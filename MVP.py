import json

# Test lecture de fichier :
with open('Tables.json', 'r') as file2:
    tables = json.load(file2)

for key, table in tables.items():
    statut = "Disponible" if table["statut"] else "Indisponible"
    print(f'La table {table["numero"]} est {statut}')


def configuration_table():
    what_table = input('Quelle table voulez-vous ? : ')
    if what_table == "":
        print("Vous n'avez entrer aucune donnée : ")
        what_table = input("Quelle table voulez-vous ? : ")
    else:
        while not what_table.isdigit() or int(what_table) < 1 or int(what_table) > 5:
            print("Erreur, la table n'existe pas !")
            what_table = input('Quelle table voulez-vous ? : ')
        what_table = int(what_table)

        print(f"Vous avez sélectionné la table : {what_table}")

    with open('Tables.json', 'r') as file2:
        tables = json.load(file2)

    found = False
    for key, details in tables.items():
        if what_table == details["numero"]:
            found = True
            if details["statut"]:
                # La table est disponible, donc on peut faire la réservation
                add_name = input("Veuillez entrer votre nom : ")
                add_lname = input("Veuillez entrer votre prénom : ")
                add_number_of_person = int(input("Veuillez entrer le nombre de personnes présentes : "))
                add_phone_number = int(input("Veuillez entrer votre numéro de téléphone : "))
                add_hour = input("Veuillez entrer l'heure d'arrivée (format HH:MM) : ")

                # Ajout des informations de réservation
                details["statut"] = False
                details["reservation"] = {
                    "nom": add_name,
                    "prenom": add_lname,
                    "nombre_personnes": add_number_of_person,
                    "numero de telephone": add_phone_number,
                    "heure_arrivee": add_hour
                }

                # Sauvegarde des modifications dans le fichier JSON
                with open('Tables.json', 'w') as file3:
                    json.dump(tables, file3, indent=4)

                print(f"La réservation a été effectuée avec succès : {details['reservation']}")
                return what_table, details["reservation"]

            else:
                print(f"Cette table est déjà réservée ! Veuillez en choisir une autre !")
                return what_table, None

    if not found:
        print("La table sélectionnée n'existe pas.")
        return what_table, None


def supp_last_table_add(what_table):

    with open('Tables.json', 'r') as file:
        tables = json.load(file)
        for key, i in tables.items():
            if what_table == i["numero"]:
                del i["reservation"]
                i["statut"] = True
    # Mise à jour du fichier :
    with open('Tables.json', 'w') as file:
        json.dump(tables, file, indent=4)
        print("La table est bien supprimée !")


def supp_choice_table():
    table_for_supp = int(input("Veuillez entrer la table que vous désirez supprimer : "))
    if table_for_supp == " ":
        print("Vous n'avez rentrer aucune données !")
        return

    with open('Tables.json', 'r') as file:
        tables = json.load(file)
        for key, i in tables.items():
            if table_for_supp == i["numero"]:
                i["statut"] = True
                del i["reservation"]
                print(f"Vous avez bien supprimé la table ! {i['numero']}")
    with open('Tables.json', 'w') as file:
        json.dump(tables, file, indent=4)

#AJouter une nouvelle table
def add_new_table():
    ask_add = input("Voulez-vous créer une nouvelle table (O/N) : ").strip().lower()
    if ask_add == "o":
        num_table = int(input("Entrez le numéro de la nouvelle table : "))

        with open('Tables.json', 'r') as file:
            tables = json.load(file)

        # Vérifier si le numéro de table existe déjà
        for table in tables.values():
            if num_table == table["numero"]:
                print('La table existe déjà ! Choisissez un nouveau numéro !')
                return

        # Ajouter la nouvelle table avec un statut dispo
        new_table_key = f"table_{num_table}"
        tables[new_table_key] = {
            "numero": num_table,
            "statut": True
        }

        with open('Tables.json', 'w') as file:
            json.dump(tables, file, indent=4)

        print(f"La nouvelle table {num_table} a été ajoutée avec succès !")

#Voir les réservations :

def look_reservation():
    with open('Tables.json', 'r') as file:
        tables = json.load(file)
        for key, i in tables.items():
            if not i["statut"]:  # Afficher uniquement si la table est réservée (statut False)
                reservation = i.get("reservation")
                if reservation:
                    print(f"La table {i['numero']} est réservée par : {reservation['nom']} {reservation['prenom']}, "
                          f"pour {reservation['nombre_personnes']} personnes à {reservation['heure_arrivee']}.")
                else:
                    print(f"La table {i['numero']} est réservée, mais les détails de la réservation sont manquants.")

def afficher_menu():
    print("\nMenu :")
    print("1 : Configurer une table")
    print("2 : Supprimer la dernière réservation")
    print("3 : Supprimer une réservation spécifique")
    print("4 : Ajouter une table")
    print("5 : Voir les réservations en cour")
    print("6 : Quitter")


# Boucle pour choisir l'action à effectuer
while True:
    afficher_menu()
    choix = input("Choisissez une option : ")

    if choix == "1":
        # Configurer une table
        what_table, reservation = configuration_table()
    elif choix == "2":
        # Supprimer la dernière réservation
        if 'what_table' in locals():  #Permet de vérifier si 'what_table' existe bien
            supp_last_table_add(what_table)
        else:
            print("Aucune table à supprimer. Faites une réservation d'abord.")
    elif choix == "3":
        # Supprimer une réservation spécifique
        supp_choice_table()
    elif choix == "4":
        add_new_table()
    elif choix == "5":
        look_reservation()
    elif choix == "6":
        print("Programme terminé")
        break
    else:
        print("Option non valide")
