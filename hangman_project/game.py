#!/usr/bin/env python3
"""Módulo que contiene la lógica del juego del ahorcado."""

MAX_ERRORS = 6


class HangmanGame:
    """Representa una partida del juego del ahorcado."""

    def __init__(self, word):
        """Inicializa una nueva partida con la palabra objetivo."""
        if not word or not isinstance(word, str):
            raise ValueError("word must be a non-empty string")
        self.word = word.lower()
        self.guessed_letters = []
        self.max_errors = MAX_ERRORS
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
        letter = letter.lower()
        if not letter.isalpha():
            return False
        if letter in self.guessed_letters:
            return letter in self.word
        self.guessed_letters.append(letter)
        if letter in self.word:
            return True
        self.errors += 1
        return False
    
    def is_won(self):
        """Comprueba si todas las letras fueron adivinadas."""
        for letter in self.word:
            if letter.isalpha() and letter not in self.guessed_letters:
                return False
        return True

    def is_lost(self):
        """Comprueba si se alcanzó el máximo de errores."""
        return self.errors >= self.max_errors

    def __str__(self):
        """Devuelve una representación legible del estado del juego."""
        return (
            f"HangmanGame(word={self.word!r}, "
            f"errors={self.errors}/{self.max_errors}, "
            f"guessed={self.guessed_letters})"
        )
