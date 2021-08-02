import tkinter, pynput, time, threading

class Window(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.__init_window()

    def __init_window(self):
        self.master.geometry('200x400')



root = tkinter.Tk()
app_1 = Window(root)
app_1.mainloop()