import arcade

class Passenger4(arcade.Sprite):

    def __init__(self, filename, scale):
        super().__init__(filename, scale)
        self.basic_info = "A teenager scrolling on his phone. He wears a beanie with quite a few pins on it."
        self.eavesdrop = "He's texting his mother. She's talking about how times have been hard lately."
        self.talk = "Whatever it is, I didn't do it."
        self.talk_direct = "I didn't know about that, but that's awesome. I wish I did it."
        self.talk_roundabout = "Sorry, am I in your way?"
        self.event = 'You show him a meme about being poor. He laughs.'