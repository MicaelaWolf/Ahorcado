#!/usr/bin/env python3
"""Modulo que contiene la logica del juego del ahorcado."""


class HangmanGame:
    """Representa una partida del juego del ahorcado."""

    def __init__(self, word):
        """Inicializa una nueva partida con la palabra objetivo."""
        self.word = word.lower()
        self.guessed_letters = []
        self.max_errors = 6
        self.errors = 0

    def display_progress(self):
        """Devuelve el estado actual de la palabra."""
        progress = []

        for letter in self.word:
            if not letter.isalpha():
                progress.append(letter)
            elif letter in self.guessed_letters:
                progress.append(letter)
            else:
                progress.append("_")

        return " ".join(progress)

    def process_guess(self, letter):
        """Procesa una letra adivinada y devuelve si fue correcta."""
        self.guessed_letters.append(letter)
        if letter in self.word:
            return True
        self.errors += 1
        return False
