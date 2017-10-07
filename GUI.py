# PYTHON GUI PROJECT
# INVENTORY MANAGEMENT SYSTEM v1.1
# IT322E PYTHON PROGRAMMING

# importing necessary modules
import datetime
import tkinter.messagebox as tm
from tkinter import *
from tkinter.filedialog import askopenfilename
import sqlite3

root = Tk()

# database integration
def Database():
    global conn, cursor
    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()


# functions for menus
def OpenFile():
    fname = askopenfilename(filetypes=(("Text Files", ".txt"), ("All Files", "*.*")))
    f = open(fname, 'r')
    Master = Toplevel()
    text = f.read()
    Label(Master, text=text).pack()
    Master.maxsize(width=300,height=300)
    Master.minsize(width=300, height=300)

def Chnglog():
    tm.showinfo("Changelog", "v1.0 - Only GUI \nv1.1 - Accepts inputs and saves it to file \nv1.2 - Open previous records")


def About():
    tm.showinfo("About", "Python GUI Project\nInventory Management v1.2")


def logged():
    s = str(datetime.datetime.now())
    tm.showinfo("Log", "Log created successfully at "+s)

# save logs
def save():
    f = open('LOG.txt', 'w')
    s = v1.get()+'\n'+v2.get()+'\n'+v3.get()+'\n'+v4.get()+'\n'+v5.get()+'\n'+v6.get()+'\n'+v7.get()+'\n'+v.get()+'\n'+var.get()+'\n'+var1.get()+'\n'+log.get()
    f.write(s)
    f.close()
    logged()


# create a drop down menu
menu = Menu(root)
root.title("Inventory Management")
root.config(menu=menu)

# file menu
file = Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=file)
file.add_command(label="Open File", command=OpenFile)
file.add_separator()
file.add_command(label="Exit", command=root.quit)

# help menu
hlp = Menu(menu, tearoff=0)
menu.add_cascade(label="Help", menu=hlp)
hlp.add_command(label="About", command=About)
hlp.add_command(label="FAQ", command=Chnglog)

# text labels
field1 = Label(text="Item Name").grid(row=0, sticky=W+E)
field2 = Label(text="Item Code").grid(row=0, column=11, sticky=E)
field3 = Label(text="Item Weight").grid(row=1, sticky=W+E)
field4 = Label(text="Delivery Date").grid(row=2, column=0, sticky=W+E)
field5 = Label(text="Dispatch Date").grid(row=2, column=11, sticky=E)
field6 = Label(text="Delivered By").grid(row=3, column=0, sticky=W+E)
field7 = Label(text="Dispatched To").grid(row=3, column=11, sticky=E)

# text fields
v1 = StringVar()
v2 = StringVar()
v3 = StringVar()
v4 = StringVar()
v5 = StringVar()
v6 = StringVar()
v7 = StringVar()
prodName = Entry(root, textvariable=v1).grid(row=0, column=10, sticky=E)
prodCode = Entry(root, textvariable=v2).grid(row=0, column=12, sticky=E)
prodWieg = Entry(root, textvariable=v3).grid(row=1, column=10, sticky=E)
prodDate = Entry(root, textvariable=v4).grid(row=2, column=10, sticky=W+E)
prodDispatch = Entry(root, textvariable=v5).grid(row=2, column=12, sticky=W+E)
Delivered = Entry(root, textvariable=v6).grid(row=3, column=10, sticky=W+E)
Dispatched = Entry(root, textvariable=v7).grid(row=3, column=12, sticky=W+E)

# radio buttons
v = StringVar()
radio = Label(root, text="Item type").grid(row=4, sticky=W)
b1 = Radiobutton(root, text="Appliances", variable=v, value=0).grid(row=5, sticky=W)
b2 = Radiobutton(root, text="Clothes", variable=v, value=1).grid(row=5, column=10)
b3 = Radiobutton(root, text="Gadgets", variable=v, value=2).grid(row=5, column=11)
b4 = Radiobutton(root, text="Consumables", variable=v, value=3).grid(row=5, column=12)
b5 = Radiobutton(root, text="Furniture", variable=v, value=4).grid(row=6, sticky=W)
b6 = Radiobutton(root, text="Crockery", variable=v, value=5).grid(row=6, column=10)
b7 = Radiobutton(root, text="Home", variable=v, value=6).grid(row=6, column=11)

# check box
var = StringVar()
var1 = StringVar()
check1 = Checkbutton(root, text="FRAGILE", variable=var).grid(row=7, sticky=W)
check2 = Checkbutton(root, text="FAST SHIP", variable=var1).grid(row=8, sticky=W)

# signature
log = StringVar()
field8 = Label(text="Supervisor Name").grid(row=9, sticky=W)
Sname = Entry(root, textvariable=log).grid(row=9, column=10, sticky=W)

# create log
logButton = Button(root, text="Create Log", command=save).grid(row=10, sticky=W)


# set width and height of box
w = 450
h = 300
ws = root.winfo_screenwidth()  # width of the screen
hs = root.winfo_screenheight()  # height of the screen

# calculate x and y coordinates for the Tk root window
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

# set the dimensions of the screen and where it is placed
root.geometry('%dx%d+%d+%d' % (w, h, x, y))

# display the menu
root.maxsize(width=450, height=400)
root.mainloop()
