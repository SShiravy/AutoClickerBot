from random import randrange
from math import cos, sin, pi
from Model.cursorControlModule import CursorControl
from pynput import mouse
from View.createGUI import UserInterface


def get_random_pos(pos, corner_pos):
    """
    :param pos: (x,y) position
    :param corner_pos: (x,y) corner position
    :return: pose with tolerance as new pos
    use randomized position between pos and corner_pos
    """
    x, y = pos
    corner_x, corner_y = corner_pos
    radius = int(pow((x - corner_x) ** 2 + (y - corner_y) ** 2, 1 / 2))
    random_r = randrange(start=-radius, stop=radius)
    random_radian = randrange(start=-0, stop=int(200 * pi)) / 10
    new_x, new_y = int(random_r * cos(random_radian)), int(random_r * sin(random_radian))
    new_pos = (x + new_x, y + new_y)
    return new_pos


class RandomClicks(CursorControl):
    def __init__(self):
        self.clks_pos = None
        self.corner_clks_pos = None
        self.t_clks = None
        self.n_clks = None
        super().__init__()
        self.set_clks_listener()

    def on_click_listener(self, x, y, button, pressed):
        """
        record Center and Corner of random clks state
        """
        if button == mouse.Button.left and pressed:
            if self.clks_pos is None:
                self.clks_pos = self.cursor.position
                UserInterface().insert_log_msg('center recorded | click the corner')
            elif self.corner_clks_pos is None:
                self.corner_clks_pos = self.cursor.position
                UserInterface().insert_log_msg('corner recorded | press set button')
            else:
                self.release_listener()
        if button == mouse.Button.right and pressed:
            self.release_listener()

    def __random_clk(self):
        """
        :return:
        set cursor on random position -> click -> release -> delay
        """
        new_pos = get_random_pos(self.clks_pos, self.corner_clks_pos)
        self.click(new_pos)

    def __do_clks_n_limit(self, n):
        """
        :return:
        click n times
        """
        for _ in range(n):
            self.__random_clk()

    def __do_clks_t_limit(self, t):
        """
        :return:
        click until minimum t time
        """
        start_time = self.elapsed_time
        while abs(start_time - self.elapsed_time) < t:
            self.__random_clk()

    def __call__(self, *args, **kwargs):
        """
        :return: n_clicks , zero if there is an error
        the priority is time, no parameters returns False /
        we always use randomized position between clks_pos and corner_clks_pos
        """
        total_click = self.total_clicks
        elapsed_time = self.elapsed_time
        if self.t_clks:
            self.__do_clks_t_limit(self.t_clks)
        elif self.n_clks:
            self.__do_clks_n_limit(self.n_clks)

        return self.total_clicks-total_click, round(self.elapsed_time-elapsed_time)
