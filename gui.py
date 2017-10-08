# PYTHON GUI PROJECT
# INVENTORY MANAGEMENT SYSTEM v1.1
# 15IT322E PYTHON PROGRAMMING

# importing necessary modules
import datetime
import tkinter.messagebox as tm
from tkinter import *
import tkinter.ttk as ttk
import sqlite3


def logged():
    s = str(datetime.datetime.now())
    tm.showinfo("Log", "Entry created successfully at "+s)

# database integration
def Database():
    global conn, cursor
    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()
    cursor.execute(
    "CREATE TABLE IF NOT EXISTS 'INVENTORY' (SNO INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,prodName TEXT, prodCode TEXT UNIQUE, prodWeig TEXT, prodQty TEXT, prodDate TEXT, prodDispatch TEXT, Delivery TEXT, Dispatch TEXT, Category INTEGER, Fragile INTEGER, FastShip INTEGER, Supervisor TEXT)")
    conn.commit()

def DatabaseAdd():
    Database()
    global conn, cursor
    cursor.execute("INSERT INTO 'INVENTORY'(prodName, prodCode, prodWeig, prodQty, prodDate, prodDispatch, Delivery, Dispatch, Category, Fragile, FastShip, Supervisor) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                   (str(v1.get()), str(v2.get()), str(v3.get()), str(v4.get()), str(v5.get()), str(v6.get()), str(v7.get()), str(v8.get()), str(v.get()), str(var.get()), str(var1.get()), str(log.get())))
    conn.commit()
    v1.set(""), v2.set(""), v3.set(""), v4.set(""), v5.set(""), v6.set(""), v7.set(""), v8.set(""), v.set("Appliances"), var.set("0"), var1.set("0"), log.set("")
    cursor.close()
    conn.close()
    logged()

def DatabaseView():
    Database()
    frame = Toplevel()
    global conn, cursor
    frame.title("View Contents")
    w = 450
    h = 75
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    frame.geometry('%dx%d+%d+%d' % (w, h, x, y))

    def Viewall():
        Database()
        ViewFrame = Toplevel()
        cursor.execute("SELECT * FROM 'INVENTORY'")
        conn.commit()
        fetch = cursor.fetchall()
        scrollbarx = Scrollbar(ViewFrame, orient=HORIZONTAL)
        scrollbary = Scrollbar(ViewFrame, orient=VERTICAL)
        tree = ttk.Treeview(ViewFrame, columns=("SNo", "prodName", "prodCode", "prodWeig", "prodQty", "prodDate", "prodDispatch", "Delivery", "Dispatch", "Category", "Fragile", "FastShip", "Supervisor"),
                            selectmode=EXTENDED, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
        scrollbary.config(command=tree.yview)
        scrollbary.pack(side=RIGHT, fill=Y)
        scrollbarx.config(command=tree.xview)
        scrollbarx.pack(side=BOTTOM, fill=X)
        tree.heading('SNo', text="SNo", anchor=CENTER), tree.heading('prodName', text="prodName", anchor=CENTER), tree.heading('prodCode', text="prodCode", anchor=CENTER),
        tree.heading('prodWeig', text="prodWeig", anchor=CENTER), tree.heading('prodQty', text="prodQty", anchor=CENTER), tree.heading('prodDate', text="prodDate", anchor=CENTER),
        tree.heading('prodDispatch', text="prodDispatch", anchor=CENTER), tree.heading('Delivery', text="Delivery", anchor=CENTER), tree.heading('Dispatch', text="Dispatch", anchor=CENTER),
        tree.heading('Category', text="Category", anchor=CENTER), tree.heading('Fragile', text="Fragile", anchor=CENTER), tree.heading('FastShip', text="FastShip", anchor=CENTER),
        tree.heading('Supervisor', text="Supervisor", anchor=CENTER)
        tree.column('#0', stretch=NO, minwidth=0, width=0), tree.column('#1', stretch=NO, minwidth=0, width=120), tree.column('#2', stretch=NO, minwidth=0, width=120),
        tree.column('#3', stretch=NO, minwidth=0, width=120), tree.column('#4', stretch=NO, minwidth=0, width=120), tree.column('#5', stretch=NO, minwidth=0, width=120),
        tree.column('#6', stretch=NO, minwidth=0, width=120), tree.column('#7', stretch=NO, minwidth=0, width=120), tree.column('#8', stretch=NO, minwidth=0, width=120),
        tree.column('#9', stretch=NO, minwidth=0, width=120), tree.column('#10', stretch=NO, minwidth=0, width=120), tree.column('#11', stretch=NO, minwidth=0, width=120),
        tree.column('#12', stretch=NO, minwidth=0, width=120), tree.column('#13', stretch=NO, minwidth=0, width=120)
        tree.pack()
        for data in fetch:
            tree.insert('', 'end', values=data)
        cursor.close()
        conn.close()

    def Search():
        Database()
        ViewFrame = Toplevel()
        scrollbarx = Scrollbar(ViewFrame, orient=HORIZONTAL)
        scrollbary = Scrollbar(ViewFrame, orient=VERTICAL)
        tree = ttk.Treeview(ViewFrame, columns=(
        "SNo", "prodName", "prodCode", "prodWeig", "prodQty", "prodDate", "prodDispatch", "Delivery", "Dispatch",
        "Category", "Fragile", "FastShip", "Supervisor"),
                            selectmode=EXTENDED, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
        scrollbary.config(command=tree.yview)
        scrollbary.pack(side=RIGHT, fill=Y)
        scrollbarx.config(command=tree.xview)
        scrollbarx.pack(side=BOTTOM, fill=X)
        tree.heading('SNo', text="SNo", anchor=CENTER), tree.heading('prodName', text="prodName", anchor=CENTER), tree.heading('prodCode', text="prodCode", anchor=CENTER),
        tree.heading('prodWeig', text="prodWeig", anchor=CENTER), tree.heading('prodQty', text="prodQty", anchor=CENTER), tree.heading('prodDate', text="prodDate", anchor=CENTER),
        tree.heading('prodDispatch', text="prodDispatch", anchor=CENTER), tree.heading('Delivery', text="Delivery", anchor=CENTER), tree.heading('Dispatch', text="Dispatch", anchor=CENTER),
        tree.heading('Category', text="Category", anchor=CENTER), tree.heading('Fragile', text="Fragile", anchor=CENTER), tree.heading('FastShip', text="FastShip", anchor=CENTER), tree.heading('Supervisor', text="Supervisor", anchor=CENTER),
        tree.column('#0', stretch=NO, minwidth=0, width=0), tree.column('#1', stretch=NO, minwidth=0, width=120), tree.column('#2', stretch=NO, minwidth=0, width=120),
        tree.column('#3', stretch=NO, minwidth=0, width=120), tree.column('#4', stretch=NO, minwidth=0, width=120), tree.column('#5', stretch=NO, minwidth=0, width=120),
        tree.column('#6', stretch=NO, minwidth=0, width=120), tree.column('#7', stretch=NO, minwidth=0, width=120), tree.column('#8', stretch=NO, minwidth=0, width=120),
        tree.column('#9', stretch=NO, minwidth=0, width=120), tree.column('#10', stretch=NO, minwidth=0, width=120), tree.column('#11', stretch=NO, minwidth=0, width=120),
        tree.column('#12', stretch=NO, minwidth=0, width=120), tree.column('#13', stretch=NO, minwidth=0, width=120)
        tree.pack()
        if st.get() != "":
            cursor.execute("SELECT * FROM `INVENTORY` WHERE `prodCode` LIKE ?", ('%' + str(st.get()) + '%',))
            conn.commit()
            fetch = cursor.fetchall()
            for data in fetch:
                tree.insert('', 'end', values=data)
        cursor.close()
        conn.close()

    def Reset():
        st.set("")

    Button(frame, text="View All", command=Viewall).pack(side=LEFT, anchor=N, padx=10, pady=10)
    Button(frame, text="Search", command=Search).pack(side=LEFT, anchor=N, padx=10, pady=10)
    st = StringVar()
    Entry(frame, textvariable=st, width=30).pack(side=LEFT, anchor=N, padx=5, pady=11)
    st.get()
    Button(frame, text="Reset", command=Reset).pack(side=LEFT, anchor=N, padx=10, pady=10)
    frame.resizable(0, 0)

def Exit():
    result = tm.askquestion('Inventory Management v1.3', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        root.destroy()
        cursor.close()
        conn.close()
        exit()

def Chnglog():
    tm.showinfo("Changelog", "v1.0 - Only GUI \nv1.1 - Accepts inputs and saves it to text file \nv1.2 - Open previous logs\nv1.3 - SQLite3 Database integration")


def About():
    tm.showinfo("About", "Python GUI Project\nInventory Management v1.3")


root = Tk()

# create a drop down menu
menu = Menu(root)
root.title("Inventory Management")
root.config(menu=menu)

# file menu
file = Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=file)
file.add_command(label="Open File", command=DatabaseView)
file.add_separator()
file.add_command(label="Exit", command=Exit)

# help menu
hlp = Menu(menu, tearoff=0)
menu.add_cascade(label="Help", menu=hlp)
hlp.add_command(label="About", command=About)
hlp.add_command(label="Changelog", command=Chnglog)

# text labels
field1 = Label(text="Item Name").grid(row=0, sticky=W+E)
field2 = Label(text="Item Code").grid(row=0, column=11, sticky=E)
field3 = Label(text="Item Weight").grid(row=1, sticky=W+E)
field4 = Label(text="Item Qty").grid(row=1, column=11, sticky=E)
field5 = Label(text="Delivery Date").grid(row=2, column=0, sticky=W+E)
field6 = Label(text="Dispatch Date").grid(row=2, column=11, sticky=E)
field7 = Label(text="Delivered By").grid(row=3, column=0, sticky=W+E)
field8 = Label(text="Dispatched To").grid(row=3, column=11, sticky=E)

# text fields
v1 = StringVar()
v2 = StringVar()
v3 = StringVar()
v4 = StringVar()
v5 = StringVar()
v6 = StringVar()
v7 = StringVar()
v8 = StringVar()
prodName = Entry(root, textvariable=v1).grid(row=0, column=10, sticky=E)
prodCode = Entry(root, textvariable=v2).grid(row=0, column=12, sticky=E)
prodWeig = Entry(root, textvariable=v3).grid(row=1, column=10, sticky=E)
prodQty = Entry(root, textvariable=v4).grid(row=1, column=12, sticky=E)
prodDate = Entry(root, textvariable=v5).grid(row=2, column=10, sticky=W+E)
prodDispatch = Entry(root, textvariable=v6).grid(row=2, column=12, sticky=W+E)
Delivered = Entry(root, textvariable=v7).grid(row=3, column=10, sticky=W+E)
Dispatched = Entry(root, textvariable=v8).grid(row=3, column=12, sticky=W+E)

# radio buttons
v = StringVar()
v.set("Appliances")
radio = Label(root, text="Item type").grid(row=4, sticky=W)
b1 = Radiobutton(root, text="Appliances", variable=v, value="Appliances").grid(row=5, sticky=W)
b2 = Radiobutton(root, text="Clothes", variable=v, value="Clothes").grid(row=5, column=10)
b3 = Radiobutton(root, text="Gadgets", variable=v, value="Gadgets").grid(row=5, column=11)
b4 = Radiobutton(root, text="Consumables", variable=v, value="Consumables").grid(row=5, column=12)
b5 = Radiobutton(root, text="Furniture", variable=v, value="Furniture").grid(row=6, sticky=W)
b6 = Radiobutton(root, text="Crockery", variable=v, value="Crockery").grid(row=6, column=10)
b7 = Radiobutton(root, text="Home", variable=v, value="Home").grid(row=6, column=11)

# check box
var = StringVar()
var1 = StringVar()
var.set("0"), var1.set("0")
check1 = Checkbutton(root, text="FRAGILE", variable=var).grid(row=7, sticky=W)
check2 = Checkbutton(root, text="FAST SHIP", variable=var1).grid(row=8, sticky=W)

# signature
log = StringVar()
field9 = Label(text="Supervisor Name").grid(row=9, sticky=W)
Sname = Entry(root, textvariable=log).grid(row=9, column=10, sticky=W)

# create log
logButton = Button(root, text="Create Entry", command=DatabaseAdd).grid(row=10, sticky=W)


# set the dimensions of the screen and where it is placed
w = 450
h = 300
ws = root.winfo_screenwidth()  # width of the screen
hs = root.winfo_screenheight()  # height of the screen
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))

# display the menu
root.resizable(0, 0)
root.mainloop()
