# Import your Game class
from phrasehunter.game import Game
# Create your Dunder Main statement.
if __name__ == "__main__":
    g = Game("The desire to write the desire to live",
    "The laws of nature", 
    "Forget yourself",
    "For my contemporaries",
    "Know yout own readers")
    g.main_loop()
# Inside Dunder Main:
## Create an instance of your Game class
## Start your game by calling the instance method that starts the game loop
