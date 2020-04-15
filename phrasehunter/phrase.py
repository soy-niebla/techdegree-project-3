# Create your Phrase class logic here.
from .character import Character

class Phrase(list):
    # creates itself as a list of Character
    def __init__(self, phrs):
        super().__init__()
        if type(phrs) != str:
            raise TypeError("The phrase should be a string")
        else:
            for i in phrs:
                self.append(Character(i))

    def __repr__(self):
        return " ".join([str(i) for i in self])

    # returns True if a character is guessed
    def guess(self, char):
        return True in [i.guess(char) for i in self]

    # Returns True if all characters are guessed
    @property
    def all_guessed(self):
        g = [i.guessed for i in self]
        g = False if False in g else True
        return g

    # resets all the guessed properties in the characters
    def reset(self):
        for i in self:
            i.guessed = False