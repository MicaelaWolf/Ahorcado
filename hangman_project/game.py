
#!/usr/bin/env python3

class HangmanGame:
    def __init__(self, word):
        self.word = word.lower()
        self.guessed_letters = []
        self.max_errors = 6
        self.errors = 0

    def display_progress(self):
        progress = []

        for letter in self.word:
            if not letter.isalpha():
                progress.append(letter)
            elif letter in self.guessed_letters:
                progress.append(letter)
            else:
                progress.append("_")

        return " ".join(progress)
