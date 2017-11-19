def carte_to_string(carte):
    """Cree la chaine de caracteres correspondant a la carte."""
    symboles = [str(i+1) for i in range(10)] + ["V", "D", "R"]
    couleurs = ["♥", "♦", "♣", "♠"]
    res = symboles[carte[0] - 1] + couleurs[carte[1] - 1]
    return res

def creer_jeu():
    """Cree un jeu de cartes."""
    jeu = []
    for i in range(1,  14):
        for j in range(1, 5):
            jeu.append((i, j))
    return jeu
