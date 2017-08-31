import os, pyautogui, time

"""
Some useful functions.
"""

# Local variables
duration = 1;

def get_image(image, emulator):
    image = normalize_file(image);
    defaultImage = "screenshots/" + image
    # check and return when the image is in the given "emulator" folder
    if emulator is not None:
        emulator = "screenshots/" + emulator + "/" + image
        if os.path.isfile(emulator):
            return emulator
    # else return the default image
    assert os.path.isfile(defaultImage)
    return defaultImage


def normalize_file(image):
    filename, file_extension = os.path.splitext(image)
    filename = "".join([c if c.isalnum() else "-" for c in filename])
    return filename + file_extension

def reset_ui_field_on_android():
    # select all texts in the UI field
    pyautogui.mouseDown();
    time.sleep(2)
    pyautogui.mouseUp()
    # reset the UI field
    pyautogui.press("backspace")
    pyautogui.press("del")
    pyautogui.press("delete")
    # unfocus the UI field
    pyautogui.moveRel(-150, 0, duration)
    pyautogui.click()
    time.sleep(1)

def locate_on_center():
    screenWidth, screenHeight = pyautogui.size()
    pyautogui.moveTo(screenWidth / 2, screenHeight / 2)

def v_scroll_on_android(scroll_value=20, locate_first_on_center = True, scrollDown = True):
    # Locate the mouse on screen center
    if(locate_first_on_center is True):
        locate_on_center()
    # Simulate drag and drop
    # pyautogui.mouseDown();
    x, y = pyautogui.position()[0], pyautogui.position()[1]
    if(scrollDown is True):
        y = y - scroll_value;
    else:
        y = y + scroll_value;
    pyautogui.dragTo(x, y)