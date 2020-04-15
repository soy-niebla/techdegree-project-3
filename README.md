#  _Phrase hunter_
 
## Character class

```
Character(char)
```
A Character instance needs a sigle character to initialize, a variable _guessed_ is automatically initialized as False on creation.

```
def __str__(self):
    if self.guessed:
        return self.char
    else:
        return "_"
```
Returns the value if the character is guessed else returns _.


```
def guess(self, char):
    if self.char.lower() == char.lower():
        self.guessed = True
        return True
    else:
        return False
```
Compares and changes the value of self.guessed if the character is guessed.


## Phrase class

```
Phrase(string)
```
The phrase class inherits from _list_. An instance is initialised with a single string wich is separated and each character is converted to a _Character_ object and appended to the phrase.

```
def guess(self, char):
    return True in [i.guess(char) for i in self]
```
Returns True if a character is guessed else False

```
@property
def all_guessed(self):
    g = [i.guessed for i in self]
    g = False if False in g else True
    return g
```

Returns True if all characters are guessed

```
    def reset(self):
        for i in self:
            i.guessed = False
```
Resets all the guessed properties in the characters
## Game class

