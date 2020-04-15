import random

from .phrase import Phrase

# Create your Game class logic in here.
class Game(list):
    # starts the main variables in the game and initialize itself to a list of phrases
    def __init__(self, *args):
        super().__init__()
        for phrs in args:
            self.append(Phrase(phrs))
        self.active = random.choice(self)
        self.life = 5
        self.choices_made = set()

    # reset itself to its initial state
    def reset(self):
        self.life = 5
        self.active.reset()
        self.active = random.choice(self)
        self.choices_made = set()

    # The main loop of the game
    def main_loop(self):    
        while self.life:    
            print(self.active)
            choise = input("Choose a character for the phrase: ")
            if choise.upper() not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                print("The choice must ve a letter (a-z)")
            elif len(choise) > 1:
                print("The choice must be a single character")
            else:
                if choise not in self.choices_made:
                    self.choices_made.add(choise)
                    if self.active.guess(choise):
                        print("You guessed right!")
                        if self.active.all_guessed:
                            print(self.active)
                            again = input("You win!, want to play agai? [y/n]: ")
                            if again.lower() == "y":
                                self.reset()
                            else:
                                exit()
                    else:
                        self.life -= 1
                        if 0 == self.life:
                            again = input("You lose!, want to play agai? [y/n]: ")
                            if again.lower() == "y":
                                self.reset()
                else:
                    print("You can't repeat your choices.")


    

        

