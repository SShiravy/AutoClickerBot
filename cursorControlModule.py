from pynput import mouse
from time import sleep
from config import SLEEP_CLICK, SLEEP_STEP


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
        self.position = None
        self.delay = SLEEP_CLICK

    def __delay(self):
        """
        :return:
        just delay and count elapsed delay
        """
        sleep(self.delay)
        self.elapsed_time += self.delay

    def get_position(self):
        # TODO: remove self.position
        def on_click(x, y, button, pressed):
            if button == mouse.Button.left and pressed:
                self.position = self.cursor.position
            if button == mouse.Button.right and pressed:
                mouse_listener.stop()

        with mouse.Listener(on_click=on_click) as mouse_listener:
            mouse_listener.join()
        return self.position

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
