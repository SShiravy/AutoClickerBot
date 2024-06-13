import time
from View.createGUI import UserInterface
from Model.pathStepClicks import StepClicks
from Model.randomizedClicks import RandomClicks


class Task:
    def __init__(self, name, task):
        self.name = name
        self.clks_task = task
        self.ui_widget = None

    def __call__(self, *args, **kwargs):
        self.ui_widget.config(state='normal')
        self.ui_widget.update_idletasks()
        self.clks_task()
        self.ui_widget.config(state='disable')
        self.ui_widget.update_idletasks()

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
            cls._instance.view.window.mainloop()
        return cls._instance

    def __match_buttons(self):
        self.view.run_button.config(command=self.__run_button)
        self.view.path_button.config(command=self.__add_path_button)
        self.view.random_click_button.config(command=self.__add_random_clks_button)
        self.view.delay_button.config(command=self.__add_delay_button)
        self.view.set_button.config(command=self.__set_button)

    def __run_button(self):
        # TODO: how much turn it should take whole cycle
        if self.tasks_list:
            self.view.insert_log_msg('| Start Executing All Tasks |')
            self.view.disable_buttons()
            for t in self.tasks_list:
                t()
        else:
            self.view.insert_log_msg('there is no task!!')

    def __set_button(self):
        """
        if there is new task it will :
            stop listening mouse - pop-up task setting window - append task to queue
        """
        if self.current_task:
            # end of setting method and listening
            self.current_task.clks_task.release_listener()
            # show the pop-up window for setting
            self.view.pop_up_window()
            # TODO: if the pop-up window not canceled the task
            # TODO: get the pop-up setting and pass it to task
            # create ui widget and pass it to task , release current task attr
            self.tasks_list.append(self.current_task)
            self.current_task.ui_widget = self.view.insert_new_task(self.current_task.name)
            self.view.insert_log_msg(f'{self.current_task.name} added to queue')
            self.current_task = None

    def __add_path_button(self):
        """
        msg hint to user then create path task obj
        """
        # TODO: log msg after each click
        if self.current_task is None:
            self.view.insert_log_msg('click all steps you want, press "set" button at the end')
            self.current_task = Task('take path', StepClicks())

    def __add_random_clks_button(self):
        if self.current_task is None:
            self.view.insert_log_msg('click the center of object')
            self.current_task = Task('random clicks', RandomClicks())

    def __add_delay_button(self):
        if self.current_task is None:
            # TODO: get data of delay from pop-up window
            # create ui widget and pass it to task , release current task attr
            self.view.pop_up_window()
            delay_time = 2
            self.current_task = Task('delay', lambda: time.sleep(delay_time))
            self.tasks_list.append(self.current_task)
            self.current_task.ui_widget = self.view.insert_new_task(self.current_task.name)
            self.view.insert_log_msg(f'{self.current_task.name} added to queue')
            self.current_task = None





Controller()