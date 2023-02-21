import arcade

class Selector(arcade.Sprite):
    """A Selector hovers above the player's currently selected passenger."""
    
    def __init__(self, filename: str = None, scale: float = 1):
        super().__init__(filename, scale)
        
        self._visible = False

    def change_vis(self, status):

        if status == 1:
            self._visible = True
        else:
            self._visible = False