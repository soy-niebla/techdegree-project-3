import random

from .phrase import Phrase

# Create your Game class logic in here.
class Game(list):
    def __init__(self, *args):
        for phrs in args:
            self.append(Phrase(phrs))
        self.active = random.choice(self)
        self.life = 5
        self.choices_made = set()

    def reset(self):
        self.life = 5
        self.active.reset()
        self.active = random.choice(self)
        self.choices_made = set()

    def main_loop(self):
        while self.life:    
            print(self.active)
            choise = input("Choose a character for the phrase: ")
            if choise.upper() not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                print("The choise must ve a letter (a-z)")
            elif len(choise) > 1:
                print("The chose must be a single character")
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
                    print("no se pueden repetir las opcioones")


    

        

