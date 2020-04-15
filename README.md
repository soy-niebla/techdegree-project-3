#  _Phrase hunter_
 
## Character class

```
Character(char)
```
A Character instance needs a single character to initialize, a variable _guessed_ is automatically initialized as False on creation.

```
def __str__(self):
```
Returns the value if the character is guessed else returns _.


```
def guess(self, char):
```
Compares and changes the value of self.guessed if the character is guessed.


## Phrase class

```
Phrase(string)
```
The Phrase class inherits from _list_. An instance is initialised with a single string wich is separated and each character is converted to a _Character_ object and appended to the phrase.

```
def guess(self, char):
```
Returns True if a character is guessed else False

```
@property
def all_guessed(self):
```

Returns True if all characters are guessed

```
def reset(self):
```
Resets all the _guessed_ properties in the characters

## Game class

```
Game(*args)
```

The Game class inherits from _list_. Initilizes with a list of strings wich are converted to Phrase objects and appended to the Game object, additionally initialize the _life_ variable, the _active_ phrase and a set *choices_made* wich stores the choices made by the player.

```
def reset(self)
```
Resets the game object for a new game

```
def main_loop(self):
```
Here is where the game starts