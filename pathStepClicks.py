from cursorControlModule import CursorControl
from pynput import mouse
from config import SLEEP_STEP


class StepClicks(CursorControl):
    def __init__(self):
        super().__init__()
        self.delay = SLEEP_STEP
        self.steps = []
        self.set_steps()

    def set_steps(self):
        """
        :return: tuple of recorded positions
        record (left) clicked positions and end with right click
        """
        def on_click(x, y, button, pressed):
            if button == mouse.Button.left and pressed:
                self.steps.append(self.cursor.position)
            if button == mouse.Button.right and pressed:
                mouse_listener.stop()

        with mouse.Listener(on_click=on_click) as mouse_listener:
            mouse_listener.join()

        self.steps = tuple(self.steps)

    def __call__(self, *args, **kwargs):
        """
        :return:
        take position of each step and click , using SLEEP_STEP for delay
        """
        for step in self.steps:
            self.click(step)

