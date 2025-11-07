import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PLAYER_PATH = os.path.join(BASE_DIR, "player.json")
WORLD_PATH = os.path.join(BASE_DIR, "world.json")


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


menue(PLAYER_PATH, WORLD_PATH)
