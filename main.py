
# TODO : add escape key ,add log, to another airdrop bot and another account : 'ChngBot' state and
#  'ChngAccount' State handle queue of states and timing add GUI

# Naming Conventions : modules are camelCase, classes are PascalCase and variables and functions are snake_case


from pynput import keyboard
from clksAirDrops import ClksAirDrops

if __name__ == '__main__':

    clks_bot = ClksAirDrops('test')

    def on_press(key):
        """
        :param key: pynput.keyboard.Key type
        :return: bool
        """
        # initialization -------------------------------------

        if key == keyboard.Key.shift_l:
            print('--- set path to earn button/ right click for ending')
            clks_bot.set_path_to_earn()
            print('--- set center of earn button/ right click for ending')
            clks_bot.set_clks_pos()
            print('--- set corner of earn button/ right click for ending')
            clks_bot.set_corner_clks_pos()
            print('--- set path to out/ right click for ending')
            clks_bot.set_path_to_out()
            n = input('---- enter number of clicks/ process will be start, !!! check the start screen')
            clks_bot.go_to_earn()
            clks_bot.earn_coin(n_times=int(n))
            clks_bot.go_out()

        elif key == keyboard.Key.esc:
            keyboardListener.stop()

    with keyboard.Listener(
            on_press=on_press,
            on_release=None) as keyboardListener:
        keyboardListener.join()

    print(clks_bot.cursor_control.elapsed_time)

