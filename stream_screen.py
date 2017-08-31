import numpy as np
from mss import mss
from PIL import Image
from pykeyboard import PyKeyboard
import cv2
import time

# local variables
mon = {'top': 40, 'left': 0, 'width': 800, 'height': 600}
sct = mss()
k = PyKeyboard()

# convert image to gray colors
def process_img(original_image):
    # convert to gray
    processed_img = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    # edge detection
    processed_img = cv2.Canny(processed_img, threshold1=200, threshold2=300)
    return processed_img;

def get_current_screen(mon):
    sct.get_pixels(mon)
    return np.array(Image.frombytes('RGB', (sct.width, sct.height), sct.image))

# stream screen
def stream_screen(mon):
    sct = mss()
    last_time = time.time()
    while(True):
        # current_screen = ImageGrab.grab(bbox=(0,40,800,640))
        #sct.get_pixels(mon)
        current_screen = get_current_screen(mon)
        processed_screen = process_img(current_screen)

        #KeyPress("s");
        k.tap_key('Space')

        #printscreen =  np.array(ImageGrab.grab(bbox=(0,40,800,640)))
        #print('loop took {} seconds'.format(time.time()-last_time))
        #last_time = time.time()
        cv2.imshow('window', cv2.cvtColor(current_screen, cv2.COLOR_BGR2RGB))
        #cv2.imshow('window', cv2.cvtColor(current_screen, cv2.COLOR_BGR2RGB))
        if cv2.waitKey(25) & 0xFF == ord('q'):
           cv2.destroyAllWindows()
           break


stream_screen(mon)