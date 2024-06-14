import time
from pynput import keyboard
from View.createGUI import UserInterface
from View.popupModules import PopupDelayInput, PopupRandomButton
from Model.pathStepClicks import StepClicks
from Model.randomizedClicks import RandomClicks
from config import SLEEP_STEP


class Task:
    def __init__(self, name, task):
        self.name = name
        self.clks_task = task
        self.ui_widget = UserInterface().run_button

    def __call__(self, *args, **kwargs):
        self.ui_widget.config(state='normal')
        self.ui_widget.update_idletasks()
        total_clicks, elapsed_time = self.clks_task()
        self.ui_widget.config(state='disable')
        self.ui_widget.update_idletasks()
        UserInterface().insert_log_msg(f'{self.name} done after {elapsed_time}s and {total_clicks} clicks')

    def _delete(self):
        self.ui_widget.destroy()


class Controller:

    def __new__(cls):
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls)
            cls._instance.view = UserInterface()
            cls._instance.tasks_list = []
            cls._instance.current_task = None
            cls._instance.__match_buttons()
            cls._instance.esc_key = False
            cls._instance.view.window.mainloop()

        return cls._instance

    def __match_buttons(self):
        self.view.run_button.config(command=self.__run_button)
        self.view.path_button.config(command=self.__add_path_button)
        self.view.random_click_button.config(command=self.__add_random_clks_button)
        self.view.delay_button.config(command=self.__add_delay_button)
        self.view.set_button.config(command=self.__set_button)

    def __run_button(self):
        # TODO: how much turn it should take whole cycle, creat a pop-up window for it or not
        if self.tasks_list:
            self.view.disable_buttons()
            self.executing_tasks()
            self.view.enable_buttons()
        else:
            self.view.insert_log_msg('there is no task!!')

    def __set_button(self):
        """
        if there is new task it will :
            stop listening mouse - pop-up task setting window - append task to queue
        """
        if self.current_task:
            # create ui widget and pass it to task , release current task attr
            self.tasks_list.append(self.current_task)
            self.current_task.ui_widget = self.view.insert_new_task(self.current_task.name)
            self.view.insert_log_msg(f'{self.current_task.name} added to queue')
            self.current_task = None

    def __add_path_button(self):
        """
        msg hint to user then create path task obj
        """
        if self.current_task is None:
            popup = PopupDelayInput(SLEEP_STEP,'delay between\neach click')
            self.view.window.wait_window(popup.window)
            if popup.ok is False:
                return False
            self.view.insert_log_msg('click all steps you want, press "set" button at the end')
            self.current_task = Task('take path', StepClicks(popup.time_delay))

    def __add_random_clks_button(self):
        if self.current_task is None:
            popup = PopupRandomButton()
            self.view.window.wait_window(popup.window)
            if popup.ok is False:
                return False
            self.view.insert_log_msg('click the center of object')
            self.current_task = Task('random clicks', RandomClicks(popup.n_clicks, popup.time_duration))

    def __add_delay_button(self):
        if self.current_task is None:
            popup = PopupDelayInput(5)
            self.view.window.wait_window(popup.window)
            if popup.ok is False:
                return False
            delay_time = popup.time_delay

            def time_delay():
                time.sleep(delay_time)
                UserInterface().insert_log_msg(f'{delay_time}s program stopped')
                return 0, delay_time
            # create ui widget and pass it to task , release current task attr
            self.current_task = Task('delay', time_delay)
            self.tasks_list.append(self.current_task)
            self.current_task.ui_widget = self.view.insert_new_task(self.current_task.name)
            self.view.insert_log_msg(f'{self.current_task.name} added to queue')
            self.current_task = None

    def executing_tasks(self):
        def on_press(key):
            if key == keyboard.Key.esc:
                self.esc_key = True
                keyboard_listener.stop()

        keyboard_listener = keyboard.Listener(on_press=on_press)
        keyboard_listener.start()
        self.view.insert_log_msg('| Start Executing All Tasks, press esc key to stop |')
        for t in self.tasks_list:
            n_clks,elapsed_t = t()
            if self.esc_key:
                self.view.insert_log_msg('| esc key pressed |')
                break
        self.esc_key = False


# TODO: solve problem of running over and over for add steps

Controller()
