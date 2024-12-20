

# Naming Conventions : modules are camelCase, classes are PascalCase and variables and functions are snake_case


from pynput import keyboard
from Model.pathStepClicks import StepClicks
from Model.randomizedClicks import RandomClicks

if __name__ == '__main__':

    def on_press(key):
        """
        :param key: pynput.keyboard.Key type
        :return: bool
        """
        # initialization -------------------------------------

        if key == keyboard.Key.shift_l:
            print('path clicks')
            path = StepClicks()
            print('random clicks')
            random_click = RandomClicks()
            random_click.n_clks = 5
            input('go ahead--')
            print('do steps')
            path()
            print('random clks')
            random_click()
        elif key == keyboard.Key.esc:

            keyboardListener.stop()

    with keyboard.Listener(
            on_press=on_press,
            on_release=None) as keyboardListener:
        keyboardListener.join()


