import random

from .phrase import Phrase

class Game(list):
    def __init__(self, *args):
    """ starts the main variables in the game and initialize itself to a list of phrases """
        super().__init__()
        for phrs in args:
            self.append(Phrase(phrs))
        self.active = random.choice(self)
        self.life = 5
        self.choices_made = set()

    def reset(self):
    """ reset itself to its initial state """
        self.life = 5
        self.active.reset()
        self.active = random.choice(self)
        self.choices_made = set()

    def main_loop(self):    
        """ The main loop of the game """
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
                        print("You choose wrong. You have {} out of 5 lives remaining!".format(self.life))
                        if 0 == self.life:
                            again = input("You lose!, want to play agai? [y/n]: ")
                            if again.lower() == "y":
                                self.reset()
                else:
                    print("You can't repeat your choices.")


    

        

