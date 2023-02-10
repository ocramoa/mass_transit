import arcade

class Passenger1(arcade.Sprite):

    def __init__(self, filename, scale):
        super().__init__(filename, scale)
        self.basic_info = "A man reading a newspaper. He wears glasses and taps his foot anxiously."
        self.eavesdrop = "He appears to be scanning through an article on the bank robbery yesterday."
        self.talk = "...Hello? Do you need anything? Hobos, always sniffing for spare change."
        self.talk_direct = "Yes, of course I've heard about it. Why? You don't look like a cop."
        self.talk_roundabout = "Did you say something?"
        self.event = 'You bump into the man, spilling his coffee. "Are you kidding me? Stupid kid!" he shouts. As he stands up, he drops his wallet, which opens and spills pennies all over the floor.'