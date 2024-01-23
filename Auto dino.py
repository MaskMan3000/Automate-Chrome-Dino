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

# Comment code is used to find the pixel range for your machine, By this code works perfectly for you
    # image = ImageGrab.grab().convert('L')
    # data = image.load()
    
    # To find the pixel range for the "Collide_with_cactus" Function
    # for i in range(200, 315):                 # Note here 315 = cls.x for me
    #         for j in range(510, 535):
    #             if (data[i, j] < 100):
    #                 data[i,j] = 0
    
    #  To find the pixel range for the "Collide_with_bird" Function
    # for i in range(220, (315 - 25)):
    #         for j in range(440, 460):
    #             if (data[i, j] < 100):
    #                 data[i,j] = 0
        
    # To find the pixel range for the "check_theme" Function  
    # for i in range(50,100):
    #         for j in range(170,220):
    #             if data[i,j] <  100:
    #                 data[i,j] = 0
    
    # image.show() 
