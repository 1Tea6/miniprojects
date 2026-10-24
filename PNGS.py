import random


class simulator:
    def __init__(self, min=1, max=100, max_guesses=10):
        self.min = min
        self.max = max
        self.max_guesses = max_guesses

        self.guesses_taken = 0

        self.secret_number = random.randint(self.min, self.max)
        self.won = False

    def check_guess(self, guess):
        self.guesses_taken += 1

        diff = abs(self.secret_number - guess)

        if diff == 0 and self.guesses_taken == 1:
            self.won = True
            return "holy shit first try ur goated"
        elif diff == 0:
            self.won = True
        elif diff <= 3:
            return "boiling, within 3 numbers"
        elif diff <= 10:
            return "warm, within 10 numbers"
        elif diff <= 25:
            return "cold, within 25 numbers"
        else:
            return "freezing, ur way off brodie"

    def guesses_left(self):
        return self.max_guesses - self.guesses_taken
