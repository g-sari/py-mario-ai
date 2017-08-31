from mario_ai import MarioAI
from utils import get_image
import pyautogui, time

class GameAI:
    """A simple example class"""

    def __init__(self):
        self.emulator = "desmume"
        self.clicks = 2
        self.interval = 0.0
        self.duration = 1
        self.button = 'left'
        self.mario = MarioAI()

    def find_the_emulator_game(self):
        image = get_image("new-super-mario-bros-find-emu-game.png", self.emulator)
        coordinates = pyautogui.locateCenterOnScreen(image)
        if coordinates is None:  # pixels not found
            image = get_image("new-super-mario-bros-enabled.png", self.emulator)
        # activate the emulator
        x, y = coordinates[0], coordinates[1]
        pyautogui.moveTo(x, y, self.duration)
        pyautogui.click()
        time.sleep(1)




    def start_playing(self):
        print("Starting to play the game ...")
        self.mario.move_forward()
        self.mario.skip_enemy()


################### Start the game ###################
game = GameAI()
if __name__ == '__main__':
    game.find_the_emulator_game()
    game.start_playing()
