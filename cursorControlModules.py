from pynput import mouse
from time import sleep
from config import SLEEP_CLICK, SLEEP_STEP
from randomizeFunctions import set_random_pos


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

    def __delay(self, delay):
        """
        :return:
        just delay and count elapsed delay
        """
        sleep(delay)
        self.elapsed_time += delay

    def set_position(self):
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
        self.__delay(SLEEP_CLICK)

    def click_randomized(self, pos, corner_pos):
        """
        :param corner_pos:
        :param pos: position to click
        :return:
        set cursor position -> click -> release -> delay
        """
        new_pos = set_random_pos(pos, corner_pos)
        self.click(new_pos)

    def set_path(self):
        """
        :return: tuple of recorded positions
        record (left) clicked positions and end with right click
        """
        path_recorder_list = []

        def on_click(x, y, button, pressed):
            if button == mouse.Button.left and pressed:
                path_recorder_list.append(self.cursor.position)
            if button == mouse.Button.right and pressed:
                mouse_listener.stop()

        with mouse.Listener(on_click=on_click) as mouse_listener:
            mouse_listener.join()

        return tuple(path_recorder_list)

    def take_path(self, path):
        """
        :param path: list of positions in form [(x,y),....]
        :return:
        take position of each step and click , using SLEEP_STEP for delay
        """
        for step in path:
            self.click(step)
            self.__delay(SLEEP_STEP)
