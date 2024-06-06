from cursorControlModules import CursorControl


class ClksAirDrops:
    def __init__(self, name):
        self.cursor_control = CursorControl()
        self.clks_pos = None
        self.corner_clks_pos = None
        self.steps_to_earn = []
        self.steps_to_out = []
        self.air_drop_name = name

    def set_clks_pos(self):
        """
        :return:
        record Center of Button to click multiple times later
        """
        self.clks_pos = self.cursor_control.set_position()

    def set_corner_clks_pos(self):
        """
        :return:
        record corner of Button to define our random parameter
        """
        self.corner_clks_pos = self.cursor_control.set_position()

    def __do_clks_n_limit(self, n):
        """
        :param n: the ClksLimit
        :return:
        click n times
        """
        for _ in range(n):
            self.cursor_control.click_randomized(self.clks_pos, self.corner_clks_pos)

    def __do_clks_t_limit(self, t):
        """
        :param t: the ClksLimit, time in second
        :return:
        click until minimum t time
        """
        start_time = self.cursor_control.elapsed_time
        while abs(start_time - self.cursor_control.elapsed_time) < t:
            self.cursor_control.click_randomized(self.clks_pos, self.corner_clks_pos)

    def earn_coin(self, t_period=None, n_times=None):
        """
        :param t_period: minimum time in second , if time limit wanted
        :param n_times: number of clicks , if clicks limit wanted
        :return: n_clicks , zero if there is an error
        the priority is time, no parameters returns False /
        we always use randomized position between clks_pos and corner_clks_pos
        """
        n_clicks = self.cursor_control.total_clicks
        if t_period:
            self.__do_clks_t_limit(t_period)
        elif n_times:
            self.__do_clks_n_limit(n_times)
        else:
            return False
        return abs(n_clicks-self.cursor_control.total_clicks)

    # --------------- path and steps --------------------------

    def set_path_to_earn(self):
        """
        :return:
        set path of clicks to click screen
        """
        self.steps_to_earn = self.cursor_control.set_path()

    def set_path_to_out(self):
        """
        :return:
        set path of clicks to out of click screen
        """
        self.steps_to_out = self.cursor_control.set_path()

    def go_to_earn(self):
        """
        :return:
        take steps to click screen
        """
        self.cursor_control.take_path(self.steps_to_earn)

    def go_out(self):
        """
        :return:
        take steps to out of click screen
        """
        self.cursor_control.take_path(self.steps_to_out)

    def get_report(self):
        report_dict = {
            "total_clicks": self.cursor_control.total_clicks,
            "total_elapsed_time": self.cursor_control.elapsed_time,
            "steps_to_earn": self.steps_to_earn,
            "steps_to_out": self.steps_to_out,
            "center_clks": self.clks_pos,
            "corner_clks": self.corner_clks_pos
        }
        return report_dict
