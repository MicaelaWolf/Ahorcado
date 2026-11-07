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


def display_game_state(game):
    """Muestra el estado actual del juego."""
    print(f"Letras intentadas: {', '.join(game.guessed_letters)}")
    print(f"Progreso: {game.display_progress()}")
    attempts_left = game.max_errors - game.errors
    print(f"Intentos restantes: {attempts_left}")


def main():
    """Ejecuta el bucle principal del juego."""
    word = get_random_word()
    if word is None:
        print("No se pudo cargar una palabra.")
        return
    
    game = HangmanGame(word)
    
    # Bucle simple para probar (el bucle completo será la Actividad 6)
    while game.errors < game.max_errors:
        display_game_state(game)
        letter = get_valid_guess(game.guessed_letters)
        result = game.process_guess(letter)
        
        if result:
            print(f"¡Correcto! La letra '{letter}' está en la palabra.")
        else:
            print(f"Incorrecto. La letra '{letter}' no está en la palabra.")
        
        # Verificar si ganó
        if "_" not in game.display_progress():
            display_game_state(game)
            print("¡Ganaste!")
            break
    
    if game.errors >= game.max_errors:
        display_game_state(game)
        print(f"Perdiste. La palabra era: {game.word}")


if __name__ == "__main__":
    main()
