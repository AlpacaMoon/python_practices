from tkinter import *
import tkinter
from PIL import Image, ImageTk
import os

directory = 'D:/Images/wtm'

accepted_formats = ['png', 'jpg', 'jpeg', 'webm', 'gif']
os.chdir(directory)
img_list = []

for file in os.listdir():
    for format in accepted_formats:
        if file.endswith(format):
            img_list.append(file)
            break

for each in img_list:
    each.replace('\\', '/')

class Image_Viewer(Frame):
    max_width, max_height = 1280, 720
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.__init_window()

    def __init_window(self):
        self.master.title('Image Viewer 1.0')
        
        self.index = 0
        self.update_img(init=True)

        self.prev_btn = Button(self.master, text='<<', command=lambda: self.btn_func('prev'))
        self.next_btn = Button(self.master, text='>>', command=lambda: self.btn_func('next'))
        self.prev_btn.grid(row=0, column=0, pady=3)
        self.next_btn.grid(row=0, column=2)

    def btn_func(self, direction):
        if direction == 'prev':
            self.index = len(img_list) - 1 if self.index == 0 else self.index - 1
        elif direction == 'next':
            self.index = 0 if self.index == len(img_list) - 1 else self.index + 1
        self.update_img()
        
    def update_img(self, init=False):
        img = Image.open(directory + '/' + img_list[self.index])
        
        if img.width > self.max_width:
            img = img.resize((self.max_width, int(self.max_width / img.width * img.height)))
        if img.height > self.max_height:
            img = img.resize((int(self.max_height / img.height * img.width), self.max_height))

        if not init:
            self.image_frame.grid_forget()
        img = ImageTk.PhotoImage(img)
        self.image_frame = Label(self.master, image=img)
        self.image_frame.image = img
        self.image_frame.grid(row=1, column=0, columnspan=3)

        self.status = Label(self.master, text='Image ' + str(self.index + 1) + ' of ' + str(len(img_list)), bd=1, relief=SUNKEN)
        self.status.grid(row=0, column=1, pady=4, sticky=W+E+N+S)


root = Tk()
app = Image_Viewer(root)
app.mainloop()
