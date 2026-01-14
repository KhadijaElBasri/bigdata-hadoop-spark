#!/usr/bin/env python3
import sys

current_word = None
current_count = 0

# Lire chaque ligne de l'entrée standard
for line in sys.stdin:
    line = line.strip()
    word, count = line.split('\t', 1)
    count = int(count)

    if current_word == word:
        current_count += count
    else:
        if current_word:
            # Afficher le total pour le mot précédent
            print(f"{current_word}\t{current_count}")
        current_word = word
        current_count = count

# Afficher le dernier mot
if current_word == word:
    print(f"{current_word}\t{current_count}")

