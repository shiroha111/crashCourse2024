from tkinter import filedialog, messagebox
from tkinter import *
import tkinter as tk


class Texteditor:
    def __init__(self, root):
        self.root = root
        self.root.title = '编辑器'
        self.widgets()

    def widgets(self):
        menu_bar = tk.Menu(self.root)
        self.root.config(menu=menu_bar)
        file_menu = tk.Menu(menu_bar,tearoff=0)
        menu_bar.add_cascade(label='文件', menu=file_menu)
        file_menu.add_command(label='打开', command=self.load)
        file_menu.add_command(label='另存为', command=self.save_as)
        file_menu.add_command(label='退出', command=self.root.quit)


        self.text = tk.Text(self.root, wrap='word')
        self.text.pack(expand=1, fill='both')
        self.text.bind('<<Modified>>', self.update_statu_bar)

        self.statu_bar = tk.Label(self.root, text='行数=0', anchor='e')
        self.statu_bar.pack(side='bottom', fill='x')

    def save_as(self):
        file_path = filedialog.asksaveasfilename(defaultextension='txt',
                                                 filetypes=[('文本文件', '*,text'), ('所有文件', '*.*')])
        if file_path:
            with open(file_path,'w') as sb:
                sb.write(self.text.get('1', tk.END))

    def update_statu_bar(self):
        self.text.edit_modified(False)
        line_count = self.text.index('end-1c').split('.')[0]
        self.statu_bar.config(text=f"行数: {line_count}")


    def load(self):
        file_path_ = filedialog.askopenfilename(title="打开文件",
                                                filetypes=[('文本文件', '*,text'), ('所有文件', '*.*')])

        if file_path_:
            with open(file_path_, "r") as file:
                self.text.delete(1.0, tk.END)
                self.text.insert(INSERT, file.read())

if __name__ == "__main__":
    root = tk.Tk()
    editor = Texteditor(root)
    root.mainloop()
