#!/usr/bin/env python3
"""Punto de entrada del juego del ahorcado."""

from utils import get_random_word
from game import HangmanGame


def get_valid_guess(guessed_letters):
    """Solicita al usuario una letra válida y la devuelve en minúsculas."""
    while True:
        guess = input("Ingresa una letra: ")
        if len(guess) != 1:
            print("Por favor, ingresa una sola letra.")
            continue
        if not guess.isalpha():
            print("Por favor, ingresa solo caracteres alfabéticos.")
            continue
        guess = guess.lower()
        if guess in guessed_letters:
            print("Ya has intentado esa letra. Intenta con otra.")
            continue
        return guess


def main():
    """Ejecuta el bucle principal del juego."""
    word = get_random_word()
    if word is None:
        print("No se pudo cargar una palabra.")
        return
    
    game = HangmanGame(word)
    
    # Actividad 3: Obtener una entrada válida del usuario
    letter = get_valid_guess(game.guessed_letters)
    game.guessed_letters.append(letter)
    
    print(f"Letra válida: {letter}")
    print(f"Progreso: {game.display_progress()}")


if __name__ == "__main__":
    main()
