from utils import get_image
import pyautogui, time

# pyautogui.screenshot('current_screen.png')

class MarioAI:
    """A simple example class"""

    def __init__(self):
        self.emulator = "desmume"

    def move_forward(self):
        print("Moving mario forward ...")
        pyautogui.keyDown("right")

    def skip_enemy(self):
        print("Jumping over enemy ...")
        image = get_image("enemy-mushroom.png", self.emulator)
        searching = True;
        while(searching):
            coordinates = pyautogui.locateCenterOnScreen(image)
            if coordinates is not None:
                x, y = coordinates[0], coordinates[1]
                print(x, y)
                searching = False;