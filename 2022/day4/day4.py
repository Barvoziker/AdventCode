# Ouvre le fichier d'entrée en mode lecture
with open("input.txt", "r") as input_file:
    # Initialise un compteur de paires en conflit à 0
    conflict_pairs = 0

    # Initialise un compteur de paires qui se chevauchent à 0
    overlap_pairs = 0

    # Pour chaque ligne du fichier
    for line in input_file:
        # Décompose la ligne en deux plages d'ID de section
        range1, range2 = line.strip().split(",")

        # Convertit les deux plages en tuples de deux valeurs (début, fin)
        range1 = tuple(map(int, range1.split("-")))
        range2 = tuple(map(int, range2.split("-")))

        # Si l'une des plages contient entièrement l'autre
        if (range1[0] <= range2[0] <= range1[1] and range1[1] >= range2[1]) or (range2[0] <= range1[0] <= range2[1] and range2[1] >= range1[1]):
            # Incrémente le compteur de paires en conflit
            conflict_pairs += 1

        # Si les deux plages se chevauchent
        if range1[0] <= range2[1] and range1[1] >= range2[0]:
            # Incrémente le compteur de paires qui se chevauchent
            overlap_pairs += 1

    # Affiche le nombre de paires en conflit
    print("Conflict pairs:", conflict_pairs)

    # Affiche le nombre de paires qui se chevauchent
    print("Overlap pairs:", overlap_pairs)