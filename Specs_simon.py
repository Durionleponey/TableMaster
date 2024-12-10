from datetime import date


class Client:
    """
    Classe représentant un client.
    """

    def __init__(self, nom: str, prenom: str, numero_telephone: int):
        """
        Initialise un client.

        PRE:
            nom (str): Le nom de famille du client.
            prenom (str): Le prénom du client.
            numero_telephone (int): Le numéro de téléphone du client.

        POST:
            Une instance de Client est créée avec les attributs.
        """
        self.nom = nom
        self.prenom = prenom
        self.numero_telephone = numeroTelephone

    def creer_reserv(self, reservation):
        """
        Permet de créer une réservation pour le client.

        PRE:
            reservation (Reservation): Une instance de la classe Reservation associée à ce client.

        POST:
            La réservation est associée au client.
        """
        self.reservation = reservation

    def supprimer_reserv(self):
        """
        Permet de supprimer une réservation existante.

        POST:
            La réservation associée au client est supprimée.
        RAISES : 
            Lance une erreur si il n'y a pas de réservation. 
        """
        self.reservation = None

    def modifier_reserv(self, nouvelle_reservation):
        """
        Permet de modifier une réservation existante.

        PRE:
            nouvelle_reservation (Reservation): Une nouvelle instance de réservation pour remplacer l'existante.

        POST:
            La réservation associée au client est mise à jour.

        Raises ; 
            Lance une erreur s'il n'y a pas de réservation
        """
        self.reservation = nouvelle_reservation


class Reservation:
    """
    Classe représentant une réservation.
    """

    def __init__(self, date: date, nbre_personne: int, heure: int, statut: str):
        """
        Initialise une réservation.

        PRE:
            date (date): La date de la réservation.
            nbre_personne (int): un nombre entier.
            heure (int): un nombre entier.
            statut (str): une chaine de caractère : ("confirmée", "annulée", "supprimé").

        POST:
            Une instance de Reservation est créée avec les attributs spécifiés.
        """
        self.date = date
        self.nbre_personne = nbre_personne
        self.heure = heure
        self.statut = statut

    def confirmer(self):
        """
        Confirme la réservation.

        POST:
            Le statut de la réservation est mis à jour à "réservée".
        Raises : 
            Lance une erreur si aucune réservation n'est faite.
        """
        self.statut = "réservée"

    def annuler(self):
        """
        Annule la réservation.

        POST:
            Le statut de la réservation est mis à jour à "annulée".
        Raises : 
            Lance une erreur si aucune réservation n'est faite.
        """
        self.statut = "annulée"

    def modifier(self, date: date, nbre_personne: int, heure: int, statut: str):
        """
        Modifie les détails de la réservation.

        PRE:
            date (date): Date pour modifier une réservation.
            nbre_personne (int): un entier positif.
            heure (int): un entier positif.
            statut (str): chaine de caractère.

        POST:
            Les attributs de la réservation sont mis à jour en fonction des paramètres fournis.
        """
        if date:
            self.date = date
        if nbrePersonne:
            self.nbre_personne = nbre_personne
        if heure:
            self.heure = heure
        if statut:
            self.statut = statut
