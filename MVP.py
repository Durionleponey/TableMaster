import json

#Test lecture de fichier :

with open('Tables.json', 'r') as file2:
    tables = json.load(file2)

for key, table in tables.items():
    statut = "Disponible" if table["statut"] else "Indisponible"
    print(f'La table {table["numero"]} est {statut}')

def configuration_table():
    # Saisie et vérification de la table choisie
    what_table = input('Quelle table voulez-vous ? (1-5) : ')
    while not what_table.isdigit() or int(what_table) < 1 or int(what_table) > 5:
        print("Erreur, la table n'existe pas !")
        what_table = input('Quelle table voulez-vous ? (1-5) : ')
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
                add_hour = input("Veuillez entrer l'heure d'arrivée (format HH:MM) : ")

                # Ajout des informations de réservation et marquage de la table
                details["statut"] = False
                details["reservation"] = {
                    "nom": add_name,
                    "prenom": add_lname,
                    "nombre_personnes": add_number_of_person,
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

"""def supp_last_table_add(what_table): #Récupération du dernier numéro de table
    with open('Tables.json', 'r') as file:
        tables = json.load(file)
        for key, i in tables.items():
            if what_table == i["numero"]:
               del i["reservation"]
               i["statut"] = True
    #Mise à jour du fichier :
    with open('Tables.json', 'w') as file:
        json.dump(tables, file, indent=4)
        print("La table est bien supprimée ! ")"""




# Appel des fonctions
what_table, reservation = configuration_table()

"""if __name__ == '__main__':
    supp_last_table_add(what_table)"""
