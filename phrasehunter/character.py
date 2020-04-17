class Character:
    def __init__(self, char):
        try:
            if len(char) != 1:
                raise ValueError("The value should be a single character.")
        except TypeError as err:
            print("{}: You should input a character.".format(err))
        else:
            self.char = str(char)
            self.reset()

    def __repr__(self):
        return str(self)

    def __str__(self):
        """ returns the value if the character is guessed else _ """
        if self.guessed:
            return self.char
        else:
            return "_"

    def __add__(self, other):
        return  str(self) + str(other)

    def __radd__(self, other):
        return str(other) + str(self)

    def guess(self, char):
        """ compares and changes the value of self.guessed if the character is guessed """
        if self.char.lower() == char.lower():
            self.guessed = True
            return True
        else:
            return False

    def reset(self):
        self.guessed = True if self.char == " " else False  