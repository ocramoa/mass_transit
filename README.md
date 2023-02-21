# Overview

When I started writing code at 11, some really simple games were the first programs I wrote (think Pong). Now, years later, I wrote this program as a proof of concept for a game I've been wanting to develop for a long time. It's an example of a single level and it's pretty rough around the edges, but I love it. I'm making the full game in Unity and C#, but that's quite a ways out from now.

MASS TRANSIT is a game where you are a subway passenger trying to catch a nefarious evildoer among your fellow passengers based on a few clues you've been given. Because this is just a single level as a demo for the game, it is not complex and the assets are rudimentary mockups of what a final version would look like. To play, you use the left and right arrow keys to switch between passengers, Enter to select one and see your first impression of them, and the left mouse button to click on the menu options on the top right for the selected passenger. Get as much info as you can before the time runs out. When it runs out, you'll be asked to select who you think "did the crime." It's like Clue, but worse!

[Software Demo Video](https://youtu.be/8AC2VyCqE2w)

# Development Environment

I used Python's Arcade module to build this, along with several assets (images) downloaded from the Internet. I also used python's threading module. I used Visual Studio Code as a text editor on Windows.

# Assets (Images & Music)

Subway car -- https://www.freepik.com/free-vector/subway-train-car-metro-wagon-interior_7773543.htm?epik=dj0yJnU9WlVrOGxTWDVVUDdiSWlTaG5ENGJYaDU1YkF6QjVNaFUmcD0wJm49UFJTQ0tIMWtVRmdCdmxhSk5vaTVEdyZ0PUFBQUFBR1AwTHRF

Passenger -- https://publicdomainvectors.org/en/free-clipart/Vector-illustration-of-simple-man-or-person-silhouette-icon/21350.html

Music -- https://pixabay.com/sound-effects/soft-piano-100-bpm-121529/

# Useful Websites

* [Arcade: A Primer on the Python Game Framework](https://realpython.com/arcade-python-game-framework/)
* [The Python Arcade Library](https://api.arcade.academy/en/latest/)

# Future Work

* If you close the game before the timer finishes, the music continues to play until an operating system error occurs with lock acquisition.
* This is an example of one level of the game. The game should contain a main menu and many levels, with different characters and stories.
* This is quite the rudimentary game. I did the writing in 20 minutes, so it could definitely be a LOT better.