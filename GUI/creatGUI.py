import ttkbootstrap as ttk
from PIL import Image, ImageTk

PADDING = 20
MARGIN = 20
# TODO: add a ScrolledText fot log
# TODO: add a frame and multi buttons or a Treeview for tasks
# TODO: add alert dialog for creating clicker bot
# TODO: make all a class for gui
# TODO: change icon and logo
# TODO: add telegram link to clickable image

root = ttk.Window(themename='darkly',
                  iconphoto=None,
                  minsize=(800, 600), )
root.iconbitmap(True, 'app_icon.ico')
root.title('Auto Clicker Tool')


canvas = ttk.Canvas(height=120, width=120)
image = Image.open("app_logo.png")
image = image.resize((120, 120))
pic = ImageTk.PhotoImage(image)
canvas.create_image(60, 60, image=pic)
canvas.grid(row=0, column=0, rowspan=2, padx=20, pady=20)

add_bot = ttk.Button(root, text='add steps', bootstyle="primary", width=20)
add_bot.grid(row=0, column=1, padx=20)

add_path = ttk.Button(root, text='add random clicker', bootstyle="primary", width=20)
add_path.grid(row=0, column=2, padx=20)

add_path = ttk.Button(root, text='add delay', bootstyle="primary", width=20)
add_path.grid(row=0, column=3, padx=20)

add_path = ttk.Button(root, text='set', bootstyle="warning",width=77)
add_path.grid(row=1, column=1, columnspan=3, padx=20)

root.mainloop()
