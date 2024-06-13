from Model.cursorControlModule import CursorControl
from pynput import mouse
from config import SLEEP_STEP


class StepClicks(CursorControl):
    def __init__(self):
        super().__init__()
        self.delay = SLEEP_STEP
        self.steps = []
        self.mouse_listener = None
        self.set_steps()

    def set_steps(self):
        """
        record (left) clicked positions , end with right click
        """

        def on_click(x, y, button, pressed):
            if button == mouse.Button.left and pressed:
                self.steps.append(self.cursor.position)
            if button == mouse.Button.right and pressed:
                self.release_listener()

        self.mouse_listener = mouse.Listener(on_click=on_click)
        self.mouse_listener.start()

    def release_listener(self):
        """
        release mouse listener and make steps an unchangeable tuple
        """
        try:
            self.mouse_listener.stop()
        except:
            pass
        self.mouse_listener = None
        self.steps = tuple(self.steps)

    def __call__(self, *args, **kwargs):
        """
        take position of each step and click , using SLEEP_STEP for delay
        """
        for step in self.steps:
            self.click(step)
