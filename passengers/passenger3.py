import arcade

class Passenger3(arcade.Sprite):

    def __init__(self, filename, scale):
        super().__init__(filename, scale)
        self.basic_info = "Someone in a large fursuit. They hum to themselves."
        self.eavesdrop = "They are humming the theme song from Zootopia."
        self.talk = "..."
        self.talk_direct = "Oh, what's up? *Hands you 40 $100 bills*"
        self.talk_roundabout = "..."
        self.event = "You call them strange. They agree, but they don't like you anymore."