# Imports
import arcade
import threading
import time
import arcade.gui as gui
from arcade.gui.widgets import UITextArea

from passengers.passenger1 import Passenger1
from passengers.passenger2 import Passenger2
from passengers.passenger3 import Passenger3
from passengers.passenger4 import Passenger4
from pickers.selector import Selector

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
SCREEN_TITLE = "MASS TRANSIT"
PASSENGER_IMG = "images/people-png-clipart-20t.png"
SELECTOR_IMG = "images/selectort.png"
SCALING = 1.5
PASS_X_POS_LIST = [80, 300, 800, 1100]
PASS_Y_POS = 250
CLUES = "There was a bank robbery earlier today. The robber only took pennies."

time_left = ""

        

class SubwayCar(arcade.Window):
    """An instance of an Arcade Window that creates and runs the game.
    """

    def __init__(self, width, height, title):
        """Initialize the game
        """
        super().__init__(width, height, title)

        self.is_game_over = False
        # Set up the empty sprite lists
        self.passengers_list = arcade.SpriteList()
        self.notebook_list = arcade.SpriteList()
        self.selectors_list = arcade.SpriteList()
        self.all_sprites = arcade.SpriteList()

        self.currently_selected = None
        self.info = "The subway car rattles as it passes over the tracks."
        self.title = "MASS TRANSIT"

    def setup(self):
        """Get the game ready to play
        """

        # Set the background color. I left this next comment line in just in case I want to change it back to purple.
        # arcade.set_background_color(arcade.color.NAVY_PURPLE)
        arcade.set_background_color((23, 20, 85))
        self.add_car() #830 * 278
        self.background_music = arcade.Sound("sounds/soft-piano.wav", True)
        self.background_music.play(loop=True)
        # enable gui manager
        self.manager = gui.UIManager()
        self.manager.enable()
        # define the text area where information will be displayed
        self.text_area = UITextArea(x=20,
                               y=417,
                               width=900,
                               height=170,
                               text=self.info,
                               font_size=20,
                               text_color=arcade.color.DUTCH_WHITE)
        

        
        self.manager.add(self.text_area)

        self.v_box = gui.UIBoxLayout(x=900, y=420, vertical=True)

        # add all the buttons at the top left
        self.clues_button = gui.UIFlatButton(text="Clues", width=200, height=30)
        self.v_box.add(self.clues_button.with_space_around(bottom=10))

        self.talk_button = gui.UIFlatButton(text="Talk", width=200, height=30)
        self.v_box.add(self.talk_button.with_space_around(bottom=10))

        self.spy_on_button = gui.UIFlatButton(text="Spy On", width=200, height=30)
        self.v_box.add(self.spy_on_button.with_space_around(bottom=10))

        self.event_button = gui.UIFlatButton(text="Event", width=200, height=30)
        self.v_box.add(self.event_button.with_space_around(bottom=10))

        self.clues_button.on_click = self.get_clues
        self.talk_button.on_click = self.get_talk
        self.spy_on_button.on_click = self.get_eavesdrop
        self.event_button.on_click = self.get_event

        # an anchor widget for the buttons
        self.manager.add(
            gui.UIAnchorWidget(
                anchor_x="left",
                anchor_y="bottom",
                align_x=910,
                align_y=420,
                size_hint_max=300,
                child=self.v_box)
        )

        # initialize all the selectors
        self.selector1 = Selector(SELECTOR_IMG, SCALING)

        self.currently_selected = self.selector1
        # if the selector is visible, put it above its associated passenger. otherwise, it is off screen
        self.selector1._visible == True
        self.selector1.center_y = PASS_Y_POS + 70
        self.selector1.center_x = PASS_X_POS_LIST[0]

        self.selector2 = Selector(SELECTOR_IMG, SCALING)
        if self.selector2._visible == True:
            self.selector2.center_y = PASS_Y_POS + 70
            self.selector2.center_x = PASS_X_POS_LIST[1]
        else:
            self.selector2.center_y = PASS_Y_POS + 70
            self.selector2.center_x = -400

        self.selector3 = Selector(SELECTOR_IMG, SCALING)
        if self.selector3._visible == True:
            self.selector3.center_y = PASS_Y_POS + 70
            self.selector3.center_x = PASS_X_POS_LIST[2]
        else:
            self.selector3.center_y = PASS_Y_POS + 70
            self.selector3.center_x = -400

        self.selector4 = Selector(SELECTOR_IMG, SCALING)
        if self.selector4._visible == True:
            self.selector4.center_y = PASS_Y_POS + 70
            self.selector4.center_x = PASS_X_POS_LIST[3]
        else:
            self.selector4.center_y = PASS_Y_POS + 70
            self.selector4.center_x = -400

        self.selectors_list.append(self.selector1)
        self.selectors_list.append(self.selector2)
        self.selectors_list.append(self.selector3)
        self.selectors_list.append(self.selector4)

        self.all_sprites.append(self.selector1)
        self.all_sprites.append(self.selector2)
        self.all_sprites.append(self.selector3)
        self.all_sprites.append(self.selector4)

        self.add_passenger_1()
        self.add_passenger_2()
        self.add_passenger_3()
        self.add_passenger_4()

        self.label = arcade.gui.UILabel(
            text=self.info,
            text_color=arcade.color.DUTCH_WHITE,
            width=350,
            height=40,
            font_size=24,
            font_name="Kenney Future")
        
        self.game_end_timer = 0.0
        
        # start the timer
        self.timer = threading.Thread(target=self.countdown,args=(60,))
        self.timer.start()


    def add_passenger_1(self):
        """Adds new passenger.
        """


        passenger1 = Passenger1(PASSENGER_IMG, SCALING)
        passenger1.center_x = PASS_X_POS_LIST[0]
        passenger1.top = PASS_Y_POS

        self.passengers_list.append(passenger1)
        self.all_sprites.append(passenger1)

    def add_passenger_2(self):
        """Adds new passenger.
        """
        passenger2 = Passenger2(PASSENGER_IMG, SCALING)

        passenger2.center_x = PASS_X_POS_LIST[1]
        passenger2.top = PASS_Y_POS

        self.passengers_list.append(passenger2)
        self.all_sprites.append(passenger2)

    def add_passenger_3(self):
        """Adds new passenger.
        """
        passenger3 = Passenger3(PASSENGER_IMG, SCALING)
        passenger3.center_x = PASS_X_POS_LIST[2]
        passenger3.top = PASS_Y_POS

        self.passengers_list.append(passenger3)
        self.all_sprites.append(passenger3)

    def add_passenger_4(self):
        """Adds new passenger.
        """
        passenger4 = Passenger4(PASSENGER_IMG, SCALING)
        passenger4.center_x = PASS_X_POS_LIST[3]
        passenger4.top = PASS_Y_POS

        self.passengers_list.append(passenger4)
        self.all_sprites.append(passenger4)

    def add_car(self):
        """Adds the subway car image."""

        car = arcade.Sprite("images/subway_car.jpg", SCALING)
        
        car.left = 0
        car.bottom = 0

        self.all_sprites.append(car)

    def on_key_press(self, symbol: int, modifiers: int):
        """Handle user keyboard input
        Q: Quit the game
        Arrows: Move Left, Right

        Arguments:
            symbol {int} -- Which key was pressed
            modifiers {int} -- Which modifiers were pressed
        """
        
        if symbol == arcade.key.Q:
            # Quit immediately
            arcade.close_window()

        # move left
        if symbol == arcade.key.LEFT:
            
            current_index = self.selectors_list.index(self.currently_selected)
            
            if (current_index - 1) >= 0:
                self.currently_selected = self.selectors_list[current_index - 1]
                
                for s in self.selectors_list:
                    if s != self.currently_selected:
                        s.center_x = -400
                    else:
                        pass
                
                new_index = self.selectors_list.index(self.currently_selected)
                self.currently_selected._visible = True
                self.currently_selected.center_y = PASS_Y_POS + 70
                self.currently_selected.center_x = PASS_X_POS_LIST[new_index]
                     
            elif (current_index - 1) < 0:
                self.currently_selected = self.selectors_list[-1]
                
                for s in self.selectors_list:
                    if s != self.currently_selected:
                        s.center_x = -400
                    else:
                        pass
                
                new_index = self.selectors_list.index(self.currently_selected)
                self.currently_selected._visible = True
                self.currently_selected.center_y = PASS_Y_POS + 70
                self.currently_selected.center_x = PASS_X_POS_LIST[new_index]

        # move selector right
        if symbol == arcade.key.RIGHT:
            current_index = self.selectors_list.index(self.currently_selected)
            if (current_index + 1) <= 3:
                self.currently_selected = self.selectors_list[current_index + 1]
                for s in self.selectors_list:
                    if s != self.currently_selected:
                        s.center_x = -400
                    else:
                        pass
                new_index = self.selectors_list.index(self.currently_selected)
                self.currently_selected._visible = True
                self.currently_selected.center_y = PASS_Y_POS + 70
                self.currently_selected.center_x = PASS_X_POS_LIST[new_index]
            elif (current_index + 1) > 3:
                self.currently_selected = self.selectors_list[-1]
                for s in self.selectors_list:
                    if s != self.currently_selected:
                        s.center_x = -400
                    else:
                        pass
                new_index = self.selectors_list.index(self.currently_selected)
                self.currently_selected._visible = True
                self.currently_selected.center_y = PASS_Y_POS + 70
                self.currently_selected.center_x = PASS_X_POS_LIST[new_index]
        # enter to select passenger
        if symbol == arcade.key.ENTER:

            for p in self.passengers_list:

                if p.center_x == self.currently_selected.center_x:
                    self.info = p.basic_info
                    self.text_area.text = self.info

    def get_clues(self, event): # gotta pass in another unused param for some unknown reason
        
        self.text_area.text = CLUES

    def get_talk(self, event):
            
        for p in self.passengers_list:
                        
            if p.center_x == self.currently_selected.center_x:    
                if self.text_area.text == p.basic_info:
                    self.text_area.text = p.talk

                elif self.text_area.text == p.talk:
                    self.text_area.text = p.talk_direct

                else:
                    self.text_area.text = p.talk_roundabout

    def get_event(self, event):
                
        for p in self.passengers_list:
            if p.center_x == self.currently_selected.center_x:
                self.text_area.text = p.event

    def get_eavesdrop(self, event):

        for p in self.passengers_list:
            if p.center_x == self.currently_selected.center_x:
                self.text_area.text = p.eavesdrop

    # success and game over messages
    def fail_wail(self, event):

        self.text_area.text = "Incorrect. Try again next time."
        self.is_game_over = True

    def yay(self, event):

        self.text_area.text = "CORRECT! CONGRATS YOU WON!"
        self.is_game_over = True
    # do the countdown
    def countdown(self, t):
        global time_left
        while t >= 0:
            time_left = t
            time.sleep(1)
            t -= 1
    # end the game if needed
    def on_update(self, delta_time: float):
        
        if self.is_game_over == True:
            self.game_end_timer += delta_time
            if self.game_end_timer > 2:
                arcade.close_window()
            return
            
        
        if time_left > 0:
            return
        else:
            self.text_area.text = "Make your guess. Who was the robber?"
            self.clues_button.text = "The man."
            self.talk_button.text = "The woman."
            self.spy_on_button.text = "The furry."
            self.event_button.text = "The teen."

            self.clues_button.on_click = self.yay
            self.talk_button.on_click = self.fail_wail
            self.spy_on_button.on_click = self.fail_wail
            self.event_button.on_click = self.fail_wail
        

    def on_draw(self):
        """Draw all game objects"""

        arcade.Window.clear(self)
        self.manager.draw()
        self.all_sprites.draw()
        arcade.draw_text(time_left,1150,550,(218,62,62),20,80)

if __name__ == "__main__":
    # Create a window!
    MassTransit = SubwayCar(
        int(SCREEN_WIDTH * SCALING), int(SCREEN_HEIGHT * SCALING), SCREEN_TITLE
    )
    # Setup to play
    MassTransit.setup()
    # Run the game
    arcade.run()