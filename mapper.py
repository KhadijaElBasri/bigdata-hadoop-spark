#!/usr/bin/env python3
import sys
import re

# Lire chaque ligne de l'entrée standard
for line in sys.stdin:
    # Nettoyage : suppression des espaces et mise en minuscules
    line = line.strip().lower()

    # Extraction des mots (lettres et chiffres seulement)
    words = re.findall(r'\b\w+\b', line)

    # Sortie pour le reducer : mot \t 1
    for word in words:
        print(f"{word}\t1")

