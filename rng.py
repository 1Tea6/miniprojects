import random


class simulator:
    def __init__(self, min=1, max=100, max_guesses=10):
        self.min = min
        self.high = max
        self.max_guesses = max_guesses
        self.guesses_taken = 0

        # Grab from the library: generate the secret pseudorandom number
        self.secret_number = random.randint(self.low, self.high)
        self.won = False

    def check_guess(self, guess):
        self.guesses_taken += 1

        # Calculate distance from target (absolute difference)
        diff = abs(self.secret_number - guess)

        if diff == 0 and self.guesses_taken == 0:
            self.won = True
            return "Holy shit firsst try ur goated"
        elif diff == 0:
            self.won = True
        elif diff <= 3:
            return "BOILING HOT! You're within 3 numbers!"
        elif diff <= 10:
            return "Warm! You're getting very close."
        elif diff <= 25:
            return "Cold! Still a bit far away."
        else:
            return "FREEZING! Way off target."

    def guesses_left(self):
        return self.max_guesses - self.guesses_taken
