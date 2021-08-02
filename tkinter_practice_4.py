from sqlite3.dbapi2 import PARSE_DECLTYPES
import tkinter
import sqlite3
from tkinter.constants import GROOVE, SOLID
from tkinter.font import BOLD

root = tkinter.Tk()
root.title('Practice 4')



try:
    connection = sqlite3.connect('address_book.db')
    c = connection.cursor()
    c.execute('''
        CREATE TABLE person (
            first_name text, 
            last_name text, 
            age integer
        )
    ''')
except:
    pass
finally:
    connection.commit()
    connection.close()


f1 = tkinter.LabelFrame(root, padx=8, pady=8)
f1.pack(padx=5, pady=5)

f_name = tkinter.Entry(f1, width=30)
tkinter.Label(f1, text='First Name :').grid(row=0, column=0)
f_name.grid(row=0, column=1)

l_name = tkinter.Entry(f1, width=30)
tkinter.Label(f1, text='Last Name :').grid(row=1, column=0)
l_name.grid(row=1, column=1)

age_ = tkinter.Entry(f1, width=10)
tkinter.Label(f1, text='Age :').grid(row=2, column=0)
age_.grid(row=2, column=1, sticky=tkinter.W)

def submit():
    connection = sqlite3.connect('address_book.db')
    c = connection.cursor()

    c.execute('''
        INSERT INTO person VALUES (:f_name, :l_name, :age_)
            ''', 
        {
            'f_name': f_name.get(),
            'l_name': l_name.get(),
            'age_' : int(age_.get())
        }
    )

    connection.commit()
    connection.close()
    
    f_name.delete(0, tkinter.END)
    l_name.delete(0, tkinter.END)
    age_.delete(0, tkinter.END)


submit_btn = tkinter.Button(root, text='Submit', padx=3, pady=3, command=submit)
submit_btn.pack(padx=3, pady=3, ipadx=112)

def query():
    connection = sqlite3.connect('address_book.db')
    c = connection.cursor()
    c.execute('''
        SELECT oid, * FROM person
    ''')
    person_records = c.fetchall()
    connection.commit()
    connection.close()

    top = tkinter.Toplevel()
    f2 = tkinter.LabelFrame(top, text='Person', padx=3, pady=3)
    f2.pack(padx=5, pady=5)
    tkinter.Label(f2, text='OID', borderwidth=2, relief=GROOVE).grid(row=0, column=0)
    tkinter.Label(f2, text='First Name', borderwidth=2, relief=GROOVE).grid(row=0, column=1)
    tkinter.Label(f2, text='Last Name', borderwidth=2, relief=GROOVE).grid(row=0, column=2)
    tkinter.Label(f2, text='Age', borderwidth=2, relief=GROOVE).grid(row=0, column=3)

    print(person_records)
    for i in range(len(person_records)):
        for j in range(len(person_records[i])):
            tkinter.Label(f2, text=person_records[i][j], borderwidth=2, relief=GROOVE).grid(row=i+1, column=j, sticky=tkinter.W)


query_btn = tkinter.Button(root, text='Query Table', padx=3, pady=3, command=query)
query_btn.pack(padx=3, pady=3, ipadx=100)



root.mainloop()