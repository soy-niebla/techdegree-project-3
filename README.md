#  _Phrase hunter_
 
## Character class

```
Character(char)
```
A Character instance needs a sigle character to initialize, a variable _guessed_ is automatically initialized as False on creation

```
def __str__(self):
    if self.guessed:
        return self.char
    else:
        return "_"
```

Returns the value if the character is guessed else returns _

```
def guess(self, char):
    if self.char.lower() == char.lower():
        self.guessed = True
        return True
    else:
        return False
```
Compares and changes the value of self.guessed if the character is guessed

## Phrase class

## Game class

