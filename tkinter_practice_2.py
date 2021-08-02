import tkinter
from PIL import Image, ImageTk
import sys
from tkinter import messagebox

root = tkinter.Tk()
root.title('Potato Apps')
root.iconbitmap('D:/Images/Icon/watame_gangimari_ver_2_KiY_icon.ico')

img_1 = ImageTk.PhotoImage(Image.open('wtm pic.jpg').resize((400,400)))
label_1 = tkinter.Label(root, image=img_1)
label_1.grid(row=0, column=0, columnspan=4)

frame_1 = tkinter.LabelFrame(root, text='Radio Buttons')
frame_1.grid(row=1, column=0)

v = tkinter.IntVar()
tkinter.Radiobutton(frame_1, text='Option 1', variable=v, value=1).pack()
tkinter.Radiobutton(frame_1, text='Option 2', variable=v, value=2).pack()
tkinter.Radiobutton(frame_1, text='Option 3', variable=v, value=3).pack()

frame_2 = tkinter.LabelFrame(root, text='Message Boxes')
frame_2.grid(row=1, column=1)

def popup():
    # showinfo, showwarning, showerror, askquestion, askokcancel, askyesno, askretrycancel, askyesnocancel
    response = messagebox.askyesnocancel('Message popup', 'Hello World!')
    tkinter.Label(frame_2, text=response).pack()

tkinter.Button(frame_2, text='Pop-up', command=lambda: popup()).pack()

root.mainloop()