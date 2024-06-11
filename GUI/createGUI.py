import ttkbootstrap as ttk
from PIL import Image, ImageTk
from config import (WINDOW_MIN_SIZE, THEME, LOGO_SCALE,
                    GENERAL_PADDING, BUTTON_WIDTH,
                    TASK_WIDTH, APP_ICON, IMAGE_LOGO)


# TODO: disable buttons after click one
# TODO: make task queue frame scrollable
# TODO: solve the problem of logo image

class UserInterface:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
            cls.__create_interface(cls.instance)
        return cls.instance

    def __create_interface(self):
        """
        all created Widgets:
        - canvas image as logo
        - Button
        - ScrolledText for log
        - Frame for task queue
        """
        # Create Window ----------------
        self.window = ttk.Window(themename=THEME, iconphoto=None, minsize=WINDOW_MIN_SIZE)
        self.window.iconbitmap(True, APP_ICON)
        self.window.title('Auto Clicker Tool')

        # logo image ------------------
        canvas = ttk.Canvas(self.window, height=LOGO_SCALE, width=LOGO_SCALE)
        image = Image.open(IMAGE_LOGO)
        image = image.resize((LOGO_SCALE, LOGO_SCALE))
        pic = ImageTk.PhotoImage(image)
        canvas.create_image(int(LOGO_SCALE / 2), int(LOGO_SCALE / 2), image=pic)
        canvas.grid(row=0, column=0, rowspan=2, padx=GENERAL_PADDING, pady=GENERAL_PADDING)

        # Create Buttons ---------------
        self.random_click_button = ttk.Button(self.window, text='add steps',
                                              bootstyle="primary", width=BUTTON_WIDTH, command=self.add_random_clicker)

        self.path_button = ttk.Button(self.window, text='add random clicker',
                                      bootstyle="primary", width=BUTTON_WIDTH, command=self.add_step_clicker)

        self.delay_button = ttk.Button(self.window, text='add delay',
                                       bootstyle="primary", width=BUTTON_WIDTH, command=self.delay_command)

        self.set_button = ttk.Button(self.window, text='set',
                                     bootstyle="warning", command=self.set_command)

        # Create scrolled log text -----------------
        self.seperator_line = ttk.Separator(self.window, bootstyle="success")
        self.log_text = ttk.ScrolledText(self.window, state="disabled")

        # Create task queue frame ------------------
        self.tasks_queue = ttk.Frame(self.window, bootstyle="dark")

        self.__grid_widgets()

    def __grid_widgets(self):
        self.random_click_button.grid(row=0, column=1, padx=GENERAL_PADDING)
        self.path_button.grid(row=0, column=2, padx=GENERAL_PADDING)
        self.delay_button.grid(row=0, column=3, padx=GENERAL_PADDING)
        self.set_button.grid(row=1, column=1, columnspan=3, padx=GENERAL_PADDING, sticky='ew')
        self.seperator_line.grid(row=3, column=0, columnspan=4, padx=GENERAL_PADDING, sticky='ew')
        self.log_text.grid(row=4, column=0, columnspan=4, padx=GENERAL_PADDING,
                           pady=(0, GENERAL_PADDING/2), sticky='ew')
        self.tasks_queue.grid(row=0, column=4, columnspan=2, rowspan=5, padx=10,
                              pady=(GENERAL_PADDING, GENERAL_PADDING/2), sticky='nsew')

    def show_log_msg(self, msg):
        self.log_text.config(state="normal")
        log_msg = f'--- {msg}\n'
        self.log_text.insert(ttk.INSERT, log_msg)
        self.log_text.config(state="disabled")

    def show_new_task(self, task_name, task_obj):
        # TODO: add click command for toggle
        new_task = ttk.Button(self.tasks_queue, text=task_name, bootstyle="secondary", width=TASK_WIDTH)
        new_task.grid(pady=2, padx=5)

    def add_random_clicker(self):
        pass

    def add_step_clicker(self):
        pass

    def delay_command(self):
        pass

    def set_command(self):
        pass


if __name__ == '__main__':
    U = UserInterface()
    U.show_new_task('mio', 0)
    U.show_log_msg('hi there where should i click')
    U.show_log_msg('hi there where should i click')
    # TODO: handle the main loop and insert some widget after it
    # TODO: Text Scroller should scroll down automatically
    U.window.mainloop()
