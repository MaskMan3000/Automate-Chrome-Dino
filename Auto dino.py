# Version 1.0
"""
import pyautogui
from PIL import ImageGrab
import time


class Operations:
    x = 315
    present_time = time.time()
    @classmethod
    def increase_streak_length(cls):
        current_time = time.time()
        elapsed_time = current_time - cls.present_time
        if elapsed_time >= 10:
            cls.x += 10
            cls.present_time = current_time

    def check_theme(self):
        for i in range(50,100):
            for j in range(170,220):
                if data[i,j] > 100:
                    return "White"
                else:
                    return "Black"
    @classmethod
    def hit_up(cls):
        pyautogui.press('up')
        time.sleep(0.08)
        pyautogui.press('down')
        return

    @classmethod
    def hit_down(cls):
        pyautogui.keyDown("down")
        time.sleep(0.08)
        pyautogui.keyUp("down")
        return

class White(Operations):
    def Collide_with_cactus_white(self,data):
        for i in range(200, self.x):
            for j in range(510, 535):
                if data[i, j] < 100:
                    return True
        return False

    def Collide_with_bird_white(self,data):
        for i in range(220, (self.x - 25)):
            for j in range(440, 460):
                if data[i, j] < 100:
                    return True
        return False

class Black(Operations):
    def Collide_with_cactus_black(self,data):
        for i in range(200, self.x):
            for j in range(510, 535):
                if data[i, j] > 150:
                    return True
        return False

    def Collide_with_bird_black(self,data):
        for i in range(220, (self.x - 25)):
            for j in range(440, 460):
                if data[i, j] > 150:
                    return True
        return False

class Dino(White,Black):
    def __init__(self,data):
        self.data = data
    def run(self):
        self.increase_streak_length()
        if self.check_theme() == "White":
            if self.Collide_with_cactus_white(data):
                self.hit_up()
            elif self.Collide_with_bird_white(data):
                self.hit_down()
        elif self.check_theme() == "Black":
            if self.Collide_with_cactus_black(data):
                self.hit_up()
            elif self.Collide_with_bird_black(data):
                self.hit_down()


if __name__ == '__main__':
    time.sleep(2)
    pyautogui.press('space')        #To start the game
    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        # image.show()
        dino = Dino(data)
        dino.run()

"""
# Version 2.0
"""
import pyautogui
from PIL import ImageGrab
import time

class Operations:
    x = 315
    present_time = time.time()
    @classmethod
    def increase_x(cls):
        current_time = time.time()
        elapsed_time = current_time - cls.present_time
        if elapsed_time >= 10:
            cls.x += 10
            cls.present_time = current_time

    def check_theme(self):
        for i in range(50,100):
            for j in range(170,220):
                if data[i,j] > 100:
                    return "White"
                else:
                    return "Black"

    def hit_up(self):
        pyautogui.press('up')
        time.sleep(0.08)
        pyautogui.press('down')
        return

    def hit_down(self):
        pyautogui.keyDown("down")
        time.sleep(0.08)
        pyautogui.keyUp("down")
        return

    def Collide_with_cactus(self,data):
        for i in range(200, self.x):
            for j in range(510, 535):
                if (data[i, j] < 100) and (self.check_theme() == "White"):
                    return True
                elif (data[i, j] > 150) and (self.check_theme() == "Black"):
                    return True
        return False

    def Collide_with_bird(self,data):
        for i in range(220, (self.x - 25)):
            for j in range(440, 460):
                if (data[i, j] < 100) and (self.check_theme() == "White"):
                    return True
                elif (data[i, j] > 150) and (self.check_theme() == "Black"):
                    return True
        return False

class Dino(Operations):
    def __init__(self,data):
        self.data = data
    def run(self):
        self.increase_x()
        if self.Collide_with_cactus(self.data):
            self.hit_up()
        elif self.Collide_with_bird(self.data):
            self.hit_down()

if __name__ == '__main__':
    time.sleep(2)
    pyautogui.press('space')        #To start the game
    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        dino = Dino(data)
        dino.run()
"""
# image = ImageGrab.grab().convert('L')
# data = image.load()
# Collide_with_bird(data)
# Collide_with_cactus(data)
# image.show()