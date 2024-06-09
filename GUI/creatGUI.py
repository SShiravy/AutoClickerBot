import ttkbootstrap as ttk
from PIL import Image, ImageTk


PADDING = 20
MARGIN = 20
# TODO: add a ScrolledText fot log
# TODO: add a frame and multi buttons or a Treeview for tasks
# TODO: add alert dialog for creating clicker bot
# TODO: make all a class for gui
root = ttk.Window(themename='superhero',
                  iconphoto=None,
                  minsize=(800, 600),)
root.iconbitmap(True, 'app_icon.ico')
root.title('Auto Clicker Tool')

canvas = ttk.Canvas(height=150, width=150)
image = Image.open("app_logo.png")
image = image.resize((150, 150))
pic = ImageTk.PhotoImage(image)
canvas.create_image(75, 75, image=pic)
canvas.grid(row=0, column=0,rowspan=2, padx=20, pady=20)


add_bot = ttk.Button(root, text='add clicker bot', bootstyle="primary",width=20)
add_bot.grid(row=0, column=1)

add_path = ttk.Button(root, text='add path', bootstyle="primary",width=20)
add_path.grid(row=1, column=1)

root.mainloop()
