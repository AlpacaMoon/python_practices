import tkinter
from tkinter.constants import END

class Calculator(tkinter.Frame):
    def __init__(self, master=None):
        tkinter.Frame.__init__(self, master)
        self.master = master
        self.__init_widgets()
    
    def __init_widgets(self):
        self.master.title("Simple Calculator")
        self.field = tkinter.Entry(self.master, width=30, borderwidth=5)
        self.field.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        for i in range(1,10):
            b = self.number_button(i)
            b.grid(row=(3 - ((i-1) // 3)), column=((i-1) % 3))
        self.number_button(0).grid(row=4, column=0)
        self.operator_button("+").grid(row=1, column=3)
        self.operator_button("-").grid(row=2, column=3)
        self.operator_button("*").grid(row=3, column=3)
        self.operator_button("/").grid(row=4, column=3)
        self.equal = self.equal_button()
        self.equal.grid(row=4, column=2)
        self.decimal_button().grid(row=4, column=1)
        self.clear_button().grid(row=5, column=0, columnspan=4)
        
        self.operator = ''
        self.n1 = None
        self.is_op = False
        self.previous = ''
        
    def number_button(self, number):
        def onclick(n):
            #Delete field if the previous button is operator or '='
            if not (isinstance(self.previous, int) or self.previous == '.'):
                self.field.delete(0, END)
            self.field.insert(END, n)
            self.previous = n
        return tkinter.Button(self.master, text=str(number), padx=18, pady=10, command=lambda: onclick(number))

    def operator_button(self, oper):
        def onclick(o):
            if self.field.get() != '':
                if self.is_op:
                    self.equal.invoke()
                self.operator = o
                self.n1 = float(self.field.get())
                self.is_op = True
            self.previous = o
        return tkinter.Button(self.master, text=str(oper), padx=18, pady=10, command=lambda: onclick(oper))
    
    def equal_button(self):
        def onclick():
            if self.field.get() != '' and self.operator != '':
                result = float(self.field.get())

                if self.operator == '+':
                    result = self.n1 + result
                elif self.operator == '-':
                    result = self.n1 - result
                elif self.operator == '*':
                    result = self.n1 * result
                elif self.operator == '/':
                    result = self.n1 / result

                self.operator = '='
                self.n1 = None
                self.field.delete(0, END)
                self.field.insert(0, str(result))
                self.is_op = False
            self.previous = '='
        return tkinter.Button(self.master, text="=", padx=18, pady=10, command=lambda: onclick())

    def decimal_button(self):
        def onclick():
            if '.' not in self.field.get():
                self.field.insert(END, '.')
            self.previous = '.'
        return tkinter.Button(self.master, text=".", padx=18, pady=10, command=lambda: onclick())

    def clear_button(self):
        def onclick():
            self.field.delete(0, END)
            self.operator = ''
            self.n1 = None
            self.previous = 'CLEAR'
        return tkinter.Button(self.master, text="CLEAR", padx=83, pady=10, command=lambda: onclick())     

root = tkinter.Tk()
Calculator(root).mainloop()