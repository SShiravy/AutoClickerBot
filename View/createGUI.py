import ttkbootstrap as ttk
from ttkbootstrap.scrolled import ScrolledFrame
from PIL import Image, ImageTk
import webbrowser
from config import (WINDOW_MIN_SIZE, THEME, LOGO_SCALE,
                    GENERAL_PADDING, BUTTON_WIDTH,
                    TASK_WIDTH, APP_ICON, IMAGE_LOGO, TELEGRAM_CHANNEL_LINK)


# TODO: change icon and logo


def open_telegram_channel(event):
    webbrowser.open_new(TELEGRAM_CHANNEL_LINK)


class UserInterface:
    def __new__(cls):
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls)
            cls.__create_interface(cls._instance)
        return cls._instance

    def __create_interface(self):
        """
        all created Widgets: - canvas image as logo - Button - ScrolledText for log - Frame for task queue
        """
        # Create Window ----------------
        self.window = ttk.Window(themename=THEME, iconphoto=None, minsize=WINDOW_MIN_SIZE)
        self.window.iconbitmap(True, APP_ICON)
        self.window.title('Auto Clicker Tool')
        # logo image ------------------
        self.__logo()
        # Create Buttons ---------------
        self.random_click_button = ttk.Button(self.window, text='add random clicker',
                                              bootstyle="primary", width=BUTTON_WIDTH)

        self.path_button = ttk.Button(self.window, text='add steps',
                                      bootstyle="primary", width=BUTTON_WIDTH)

        self.delay_button = ttk.Button(self.window, text='add delay',
                                       bootstyle="primary", width=BUTTON_WIDTH)

        self.set_button = ttk.Button(self.window, text='set', bootstyle="warning")

        self.run_button = ttk.Button(self.window, text='RUN', bootstyle="success")

        # Create scrolled log text -----------------
        self.seperator_line = ttk.Separator(self.window, bootstyle="success")
        self.log_text = ttk.ScrolledText(self.window, state="disabled")

        # Create task queue frame ------------------
        self.queue_frame = ttk.Frame(self.window, bootstyle='dark')
        self.tasks_queue = ScrolledFrame(self.queue_frame, bootstyle="dark", width=190, height=690)
        task_frame_label = ttk.Label(self.tasks_queue, text='Tasks', width=TASK_WIDTH, bootstyle="light",
                                     # textvariable=text_var,
                                     anchor=ttk.CENTER,
                                     font=("Normal", 12, "bold"),
                                     justify=ttk.CENTER,
                                     relief=ttk.RAISED,
                                     wraplength=250
                                     )
        task_frame_label.grid(sticky='ew')

        # grid widgets -----------------------------
        self.__grid_widgets()
        # show the screen --------------------------

    def __logo(self):
        """
        Create Logo image and open Channel Link by clicking on it
        """
        logo_image = Image.open(IMAGE_LOGO)
        logo_image = logo_image.resize((LOGO_SCALE, LOGO_SCALE))
        photo_logo = ImageTk.PhotoImage(logo_image)
        canvas = ttk.Canvas(self.window, height=LOGO_SCALE, width=LOGO_SCALE)
        logo_widget = canvas.create_image(int(LOGO_SCALE / 2), int(LOGO_SCALE / 2), image=photo_logo)
        canvas.image = photo_logo
        canvas.grid(row=0, column=0, rowspan=2, padx=GENERAL_PADDING, pady=GENERAL_PADDING)
        canvas.tag_bind(logo_widget, "<Button-1>", open_telegram_channel)

    def __grid_widgets(self):
        """
        griding all widgets
        """
        self.path_button.grid(row=0, column=1, padx=GENERAL_PADDING, pady=(GENERAL_PADDING, 0))
        self.random_click_button.grid(row=0, column=2, padx=GENERAL_PADDING, pady=(GENERAL_PADDING, 0))
        self.delay_button.grid(row=0, column=3, padx=GENERAL_PADDING, pady=(GENERAL_PADDING, 0))
        self.set_button.grid(row=1, column=1, columnspan=3, padx=GENERAL_PADDING, sticky='ewn')
        self.seperator_line.grid(row=3, column=0, columnspan=4, padx=GENERAL_PADDING, sticky='ew')
        self.log_text.grid(row=4, column=0, columnspan=4, padx=GENERAL_PADDING,
                           pady=(0, GENERAL_PADDING / 2), sticky='ew')
        self.queue_frame.grid(row=0, column=4, rowspan=6, padx=GENERAL_PADDING / 2,
                              pady=(GENERAL_PADDING, GENERAL_PADDING / 2), sticky='nsew')
        self.tasks_queue.grid(sticky='nsew')
        self.run_button.grid(row=5, column=0, columnspan=4, padx=GENERAL_PADDING,
                             pady=GENERAL_PADDING / 2, sticky='ew')

    def insert_log_msg(self, msg):
        """
        :param msg: str
        show msg in log box
        """
        self.log_text.config(state="normal")
        log_msg = f'--- {msg}\n'
        self.log_text.insert(ttk.END, log_msg)
        self.log_text.config(state="disabled")
        # show changes ---
        self.window.update_idletasks()

    def insert_new_task(self, task_name):
        """
        :param task_name: str
        add a button as a task in task queue
        """
        # TODO: add click command for toggle
        new_task_widget = ttk.Button(self.tasks_queue, text=task_name, bootstyle="secondary",
                                     width=TASK_WIDTH, state='disable')
        new_task_widget.grid(pady=2, padx=5)

        # show changes ---
        self.window.update_idletasks()
        return new_task_widget

    def __change_buttons_state(self, state):
        for widget in self.window.winfo_children():
            if isinstance(widget, ttk.Button):
                widget.config(state=state)
        self.window.update_idletasks()

    def disable_buttons(self):
        self.__change_buttons_state('disable')

    def enable_buttons(self):
        self.__change_buttons_state('normal')


if __name__ == '__main__':
    U = UserInterface()
    U.insert_new_task('mio', 0)
    U.insert_log_msg('hi there where should i click')
    U.insert_log_msg('hi there where should i click')
    U.window.mainloop()
