from Model.cursorControlModule import CursorControl
from pynput import mouse
from config import SLEEP_STEP


class StepClicks(CursorControl):
    def __init__(self, delay=SLEEP_STEP):
        self.delay = delay
        self.steps = []
        super().__init__()
        self.set_clks_listener()

    def on_click_listener(self, x, y, button, pressed):
        if button == mouse.Button.left and pressed:
            self.steps.append(self.cursor.position)
        if button == mouse.Button.right and pressed:
            self.release_listener()

    def release_listener(self):
        """
        release mouse listener and make steps an unchangeable tuple
        """
        super().release_listener()
        self.steps = tuple(self.steps)

    def __call__(self, *args, **kwargs):
        """
        :return: number of clicks , elapsed time
        take position of each step and click , using SLEEP_STEP for delay
        """
        total_click = self.total_clicks
        elapsed_time = self.elapsed_time
        for step in self.steps:
            self.click(step)
        return self.total_clicks-total_click, round(self.elapsed_time-elapsed_time,2)
