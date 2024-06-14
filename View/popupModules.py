import ttkbootstrap as ttk

from config import BUTTON_WIDTH, GENERAL_PADDING


# TODO: add validation to entries

class Popup:
    def __init__(self):
        self.window = ttk.Toplevel()
        self.window.minsize(200, 20)
        self.window.focus()
        self.ok = False
        # Buttons -------------
        self.cancel_button = ttk.Button(self.window, text='Cancel Task',
                                        bootstyle="danger", width=BUTTON_WIDTH, command=self.destroy)
        self.cancel_button.grid(row=1, column=0, padx=GENERAL_PADDING / 2, pady=GENERAL_PADDING / 2, sticky='ew')

        self.ok_button = ttk.Button(self.window, text='OK',
                                    bootstyle="success", width=BUTTON_WIDTH, command=self.ok_command)
        self.ok_button.grid(row=1, column=1, padx=GENERAL_PADDING / 2, pady=GENERAL_PADDING / 2, sticky='ew')

    def destroy(self):
        self.window.destroy()

    def ok_command(self):
        self.ok = True
        self.window.destroy()


class PopupRandomButton(Popup):
    def __init__(self, time_duration='', n_clicks=50):
        super().__init__()
        self.time_duration = None
        self.n_clicks = None
        time_frame = ttk.Labelframe(self.window, text='time duration', bootstyle='info')
        time_frame.grid(row=0, column=0, padx=GENERAL_PADDING / 2, pady=GENERAL_PADDING / 2, sticky='ew')
        self.time_duration_entry = ttk.Entry(time_frame, bootstyle="info", width=BUTTON_WIDTH)
        self.time_duration_entry.insert(index=0, string=time_duration)
        self.time_duration_entry.grid(padx=GENERAL_PADDING / 2, pady=GENERAL_PADDING / 2)

        n_click_frame = ttk.Labelframe(self.window, text='number of clicks', bootstyle='info')
        n_click_frame.grid(row=0, column=1, padx=GENERAL_PADDING / 2, pady=GENERAL_PADDING / 2, sticky='ew')
        self.n_click_entry = ttk.Entry(n_click_frame, bootstyle="info", width=BUTTON_WIDTH)
        self.n_click_entry.insert(index=0, string=str(n_clicks))
        self.n_click_entry.grid(padx=GENERAL_PADDING / 2, pady=GENERAL_PADDING / 2)

    def ok_command(self):
        try:
            self.n_clicks = int(self.n_click_entry.get())
            self.time_duration = float(self.time_duration_entry.get())
        except:
            pass
        super().ok_command()


class PopupDelayInput(Popup):
    def __init__(self, default_val, description=None):
        super().__init__()
        self.time_delay = None
        time_frame = ttk.Labelframe(self.window, text='delay(s)', bootstyle='info')
        time_frame.grid(row=0, column=0, padx=GENERAL_PADDING / 2, pady=GENERAL_PADDING / 2, sticky='ew')
        self.time_entry = ttk.Entry(time_frame, bootstyle="info", width=BUTTON_WIDTH)
        self.time_entry.insert(index=0, string=str(default_val))
        self.time_entry.grid(padx=GENERAL_PADDING / 2, pady=GENERAL_PADDING / 2)
        if description:
            label = ttk.Label(self.window, text=description, width=BUTTON_WIDTH)
            label.grid(row=0, column=1, padx=GENERAL_PADDING / 2, pady=GENERAL_PADDING / 2, sticky='ew')

    def ok_command(self):
        try:
            self.time_delay = float(self.time_entry.get())
        except:
            pass
        super().ok_command()
