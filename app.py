from phrasehunter.game import Game

if __name__ == "__main__":
    print("Welcome to the Phrasehunter Game!")
    g = Game("The desire to write the desire to live",
    "The laws of nature", 
    "Forget yourself",
    "For my contemporaries",
    "Know your own readers")
    
    g.main_loop()
