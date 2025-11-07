import os


HAUPTORDNER = os.path.dirname(os.path.abspath(__file__))
SPIELER_PFAD = os.path.join(HAUPTORDNER, "player.json")
WELT_PFAD = os.path.join(HAUPTORDNER, "world.json")


def menue():
    while True:
        try:
            spiel_auswahl = int(
                input(
                    """
                1: Neues Spiel
                2: Lade letzten Spielstand
                3: Beenden
                                 """
                )
            )
        except ValueError:
            print("Fehler! Das ist keine gültige Zahl!")


menue(SPIELER_PFAD, WELT_PFAD)
