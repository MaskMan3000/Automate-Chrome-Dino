# Dino Game Bot

The Auto dino is a Python script designed to automate gameplay for the popular T-Rex Run game in the Chrome browser. This script is for individuals who want to explore basic automation using PyAutoGUI and PIL while having fun with the classic Dino Game.


## Installation

Make sure you have the required libraries installed. You can install them using:

```bash
pip install pyautogui
pip install pillow
```
    
## How to Use
1. Open the Chrome browser and navigate to the Dino Game by entering "chrome://dino" in the address bar.

2. Run the script using the following command:

```Python
python dino_game_bot.py
```
3. The script will wait for 2 seconds before starting the game by pressing the 'space' key.

4. The Dino will automatically jump over cacti and duck under birds.
## Documentation

The code is organized into a class structure:

The Operations class handles common operations such as increasing the x-coordinate, checking the theme, and collisions.

Dino class inherits from Operations and is responsible for running the game by calling appropriate methods.

### Important Functions:-

increase_x: Increases the x-coordinate of the Dino every 10 seconds.

check_theme: Analyzes pixel colors to determine the game theme (White or Black).

hit_up: Simulates a jump by pressing the 'up' key.

hit_down: Simulates a duck by holding and releasing the 'down' key.

Collide_with_cactus: Checks for collisions with cacti.

Collide_with_bird: Checks for collisions with birds.


## Configuring Pixel Ranges
The commented code in the script can be uncommented and modified to find the appropriate pixel ranges for your machine.

The image below serves as a reference guide to help you better understand how to fine-tune the strip to achieve optimal detection accuracy.




## Screenshot

![image](https://github.com/MaskMan3000/Automate-Chrome-Dino/assets/157305465/fc41c5e2-b51e-45d8-aec3-44f4a46d3f1a)

