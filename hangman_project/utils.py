#!/usr/bin/env python3

import random


def get_random_word():
    try:
        with open("wordlist.txt", "r", encoding="utf-8") as file:
            words = [word.strip() for word in file if word.strip().isalpha()]

        if not words:
            print("No hay palabras disponibles")
            return None

        return random.choice(words)

    except FileNotFoundError:
        print("No se encontró el archivo")
        return None
