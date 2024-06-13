from pynput import mouse
from time import sleep
from config import SLEEP_CLICK


class CursorControl:
    """
    to have easier process when we want to click somewhere (exact position or randomized)
    also to record path of clicks and take list of steps to click
    it will record elapsed time for each click and total number of clicks
    """

    def __init__(self):
        self.cursor = mouse.Controller()
        self.elapsed_time = 0
        self.total_clicks = 0
        self.delay = SLEEP_CLICK
        self.mouse_listener = None

    def __delay(self):
        """
        :return:
        just delay and count elapsed delay
        """
        sleep(self.delay)
        self.elapsed_time += self.delay

    def click(self, pos):
        """
        :param pos: position to click
        :return:
        set cursor position -> click -> release -> delay
        """
        self.cursor.position = pos
        self.cursor.press(mouse.Button.left)
        self.cursor.release(mouse.Button.left)
        self.total_clicks += 1
        self.__delay()

    def set_clks_listener(self):
        self.mouse_listener = mouse.Listener(on_click=self.on_click_listener)
        self.mouse_listener.start()

    def on_click_listener(self, x, y, button, pressed):
        pass

    def release_listener(self):
        """
        release mouse listener and make steps an unchangeable tuple
        """
        try:
            self.mouse_listener.stop()
        except:
            pass
        self.mouse_listener = None