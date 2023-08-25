"""
Guess_it_Win_it - A number guessing game
"""

import random


class Game:
    """ Manage the number guessing game"""

    def __init__(self):
        self.original = self.random_generator()
        self.tries = 0

    def random_generator(self):
        """ This function generate a random number between 1000 and 9999 for the players to guess """
        return random.randint(1000, 9999)

    def verify_entry(self, user_input):
        """This function checks the input number has 4 digits and also checks whether the input is a number"""
        return len(user_input) == 4 and user_input.isdigit()

    def hint_out(self, user_input):
        """This function gives hints to the player for guessing the number"""
        hints = []
        for i in range(4):
            if str(user_input)[i] == str(self.original)[i]:
                hints.append('o')
            elif str(user_input)[i] in str(self.original):
                hints.append('x')
        return hints

    def start(self):
        """This function is where the executions take place"""
        print("Guess it Win It -\n"
              "Guess a 4 digit number\n"
              "* if the number guessed has a digit in the correct place then it displays - O\n"
              "* if the number guessed has a digit in the wrong place but correct number then it displays - X ")

        retry = True
        while retry:
            self.original = self.random_generator()
            self.tries = 0
            while True:
                user_input = input("Guess a 4 digit number, or type 'exit' to exit the game: ")
                if user_input.lower() == 'exit':
                    print(f"Original number was {self.original}.")
                    break
                if not self.verify_entry(user_input):
                    print("Wrong Entry")
                    continue

                self.tries += 1
                tip = self.hint_out(user_input)

                if user_input == str(self.original):
                    print(f"Winner! You guessed {self.original} from {self.tries} tries.")
                    break
                else:
                    print("HINTS:", ' '.join(tip))

            retry = input("Continue game? (y/n): ").lower() == 'y'


if __name__ == "__main__":
    game = Game()
    game.start()
