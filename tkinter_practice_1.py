import tkinter
from tkinter.constants import BOTH

class Window(tkinter.Frame):
    def __init__(self, master=None):
        tkinter.Frame.__init__(self, master)
        self.master = master
        self.init__window()
    
    def init__window(self):
        self.master.geometry("1200x720")
        self.master.title("Potato App")
        self.pack(fill=BOTH, expand=1)

        quitButton = tkinter.Button(self, text="Quit", command=self.exit_application)
        quitButton.place(x=20, y=680)

        top_bar = tkinter.Menu(self.master)
        self.master.config(menu=top_bar)

        file_cascade = tkinter.Menu(top_bar)
        file_cascade.add_command(label='Exit', command=self.exit_application)

        edit_cascade = tkinter.Menu(top_bar)
        edit_cascade.add_command(label="Undo")
        edit_cascade.add_command(label="Redo")

        top_bar.add_cascade(label='File', menu=file_cascade)
        top_bar.add_cascade(label='Edit', menu=edit_cascade)
    
    def exit_application(self):
        exit()

    def appearance_size(self, size):
        self.master.geometry(size)

root = tkinter.Tk()
app1 = Window(root)
root.mainloop()