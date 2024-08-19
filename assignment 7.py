import tkinter as tk
from PIL import Image, ImageTk, ImageOps
from tkinter import filedialog


def open_image():
    global file_path
    file_path = filedialog.askopenfilename(title='打开文件',
                                           filetypes=[('所有文件', '*,*')])
    img = Image.open(file_path)
    img.thumbnail((500, 500))
    img = ImageTk.PhotoImage(img)
    image_label.config(image=img)
    image_label.image = img


def flip_image():
    global file_path
    img = Image.open(file_path)
    img = ImageOps.mirror(img)
    img.thumbnail((500, 500))
    img = ImageTk.PhotoImage(img)
    image_flip_label.config(image=img)
    image_flip_label.image = img


root = tk.Tk()
root.title('图片翻转')

frame = tk.Frame(root)
frame.pack()

tk.Button(frame, text='open', command=open_image).pack(side=tk.LEFT)
tk.Button(frame, text='flip', command=flip_image).pack(side=tk.RIGHT)

image_label = tk.Label(root)
image_label.pack(side=tk.LEFT)
image_flip_label = tk.Label(root)
image_flip_label.pack(side=tk.RIGHT)

root.mainloop()