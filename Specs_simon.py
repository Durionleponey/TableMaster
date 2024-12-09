from datetime import date


class Client:
    """
    Classe représentant un client.
    """

    def __init__(self, nom: str, prenom: str, numeroTelephone: int):
        """
        Initialise un client.

        PRE:
            nom (str): Le nom de famille du client.
            prenom (str): Le prénom du client.
            numeroTelephone (int): Le numéro de téléphone du client.

        POST:
            Une instance de Client est créée avec les attributs.
        """
        self.nom = nom
        self.prenom = prenom
        self.numeroTelephone = numeroTelephone

    def creerReserv(self, reservation) -> None:
        """
        Permet de créer une réservation pour le client.

        PRE:
            reservation (Reservation): Une instance de la classe Reservation associée à ce client.

        POST:
            La réservation est associée au client.
        """
        self.reservation = reservation

    def supprimerReserv(self) -> None:
        """
        Permet de supprimer une réservation existante.

        POST:
            La réservation associée au client est supprimée.
        """
        self.reservation = None

    def modifierReserv(self, nouvelle_reservation) -> None:
        """
        Permet de modifier une réservation existante.

        PRE:
            nouvelle_reservation (Reservation): Une nouvelle instance de réservation pour remplacer l'existante.

        POST:
            La réservation associée au client est mise à jour.
        """
        self.reservation = nouvelle_reservation


class Reservation:
    """
    Classe représentant une réservation.
    """

    def __init__(self, date: date, nbrePersonne: int, heure: int, statut: str):
        """
        Initialise une réservation.

        PRE:
            date (date): La date de la réservation.
            nbrePersonne (int): Le nombre de personnes pour la réservation.
            heure (int): L'heure de la réservation.
            statut (str): Le statut de la réservation ("confirmée", "annulée", "supprimé").

        POST:
            Une instance de Reservation est créée avec les attributs spécifiés.
        """
        self.date = date
        self.nbrePersonne = nbrePersonne
        self.heure = heure
        self.statut = statut

    def confirmer(self) -> None:
        """
        Confirme la réservation.

        POST:
            Le statut de la réservation est mis à jour à "réservée".
        """
        self.statut = "réservée"

    def annuler(self) -> None:
        """
        Annule la réservation.

        POST:
            Le statut de la réservation est mis à jour à "annulée".
        """
        self.statut = "annulée"

    def modifier(self, date: date = None, nbrePersonne: int = None, heure: int = None, statut: str = None) -> None:
        """
        Modifie les détails de la réservation.

        PRE:
            date (date, optionnel): La nouvelle date de la réservation.
            nbrePersonne (int, optionnel): Le nouveau nombre de personnes.
            heure (int, optionnel): La nouvelle heure de réservation.
            statut (str, optionnel): Le nouveau statut de la réservation.

        POST:
            Les attributs de la réservation sont mis à jour en fonction des paramètres fournis.
        """
        if date:
            self.date = date
        if nbrePersonne:
            self.nbrePersonne = nbrePersonne
        if heure:
            self.heure = heure
        if statut:
            self.statut = statut
