import tkinter
from PIL import Image, ImageTk
from tkinter import filedialog

# root = tkinter.Tk()
# root.title('Tkinter Practice 3')
# root.iconbitmap('wtm pic.jpg')

# def open_window():
#     top = tkinter.Toplevel()
#     tkinter.Label(top, text='This is Top').pack()
#     global img
#     img = ImageTk.PhotoImage(Image.open('wtm pic.jpg'))
#     tkinter.Label(top, image=img).pack()
#     tkinter.Button(top, text='Close Window', command=top.destroy).pack()


# tkinter.Button(root, text='Second Window', command=open_window).pack()

# f1 = filedialog.askopenfilename(initialdir='/Images/wtm', title='Select a file', filetypes=(('PNG files', '*.png'), ('All files', '*.*')))
# tkinter.Label(root, text=f1).pack()
# img_1 = ImageTk.PhotoImage(Image.open(f1))
# tkinter.Label(root, image=img_1).pack()

# root.mainloop()

class Window(tkinter.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.__init_window()

    def __init_window(self):
        self.master.title('Practice')
        tkinter.Button(self.master, text='Open Window', command=self.open_new_window).pack()

        options = [1,2,3,4,5]
        var = tkinter.IntVar()
        var.set(options[0])
        tkinter.OptionMenu(self.master, var, *options).pack()

    def open_new_window(self):
        self.top = tkinter.Toplevel()
        self.top.title('This is top')
        d = filedialog.askopenfilename()
        self.img = ImageTk.PhotoImage(Image.open(d))
        tkinter.Label(self.top, image=self.img).pack()
        tkinter.Button(self.top, text='Dupe Image', command=self.dupe_img).pack()



root = tkinter.Tk()
app = Window(root)
app.mainloop()
