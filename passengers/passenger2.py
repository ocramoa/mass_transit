import arcade

class Passenger2(arcade.Sprite):

    def __init__(self, filename, scale):
        super().__init__(filename, scale)
        self.basic_info = "A woman with a baby. Although she appears stressed, the smile lines around her mouth are obvious."
        self.eavesdrop = "As her baby begins to cry, she puts an expensive binky in its mouth."
        self.talk = "Oh, uh . . . hi there."
        self.talk_direct = "Oh, I heard about that! Good thing I'm deathly allergic to copper."
        self.talk_roundabout = "Sorry, what was that?"
        self.event = 'You hand the baby a small stuffed toy, which it chews on. The mother regards you with a smile.'