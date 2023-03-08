import sqlite3
from tkinter import Tk, Label, Button, Toplevel, Text, Entry, StringVar, OptionMenu
root = Tk()
root.title("Cubes Project List")
root.geometry('1000x1000')
conn = sqlite3.connect("cubesProject.sqlite")
c = conn.cursor()
def entryid():
    newWindow = Toplevel(root)
    newWindow.geometry("300x300")
    newWindow.title('Data: ')
    content = c.execute('SELECT * FROM WuFooData WHERE entryID = 1').fetchall()
    for row in content:
        print(row)
        Label(newWindow, text=row).pack()

def prefix():
    newWindow = Toplevel(root)
    newWindow.geometry("300x300")
    newWindow.title('Data: ')
    content = c.execute('SELECT * FROM WuFooData WHERE entryID = 2').fetchall()
    for row in content:
        print(row)
        Label(newWindow, text=row).pack()

def first_name():
    newWindow = Toplevel(root)
    newWindow.geometry("300x300")
    newWindow.title('Data: ')
    content = c.execute('SELECT * FROM WuFooData WHERE entryID = 3').fetchall()
    for row in content:
        print(row)
        Label(newWindow, text=row).pack()

def last_name():
    newWindow = Toplevel(root)
    newWindow.geometry("300x300")
    newWindow.title('Data: ')
    content = c.execute('SELECT * FROM WuFooData WHERE entryID = 4').fetchall()
    for row in content:
        print(row)
        Label(newWindow, text=row).pack()

def title():
    newWindow = Toplevel(root)
    newWindow.geometry("300x300")
    newWindow.title('Data: ')
    content = c.execute('SELECT * FROM WuFooData WHERE entryID = 5').fetchall()
    for row in content:
        print(row)
        Label(newWindow, text=row).pack()

def org():
    newWindow = Toplevel(root)
    newWindow.geometry("300x300")
    newWindow.title('Data: ')
    content = c.execute('SELECT * FROM WuFooData WHERE entryID = 6').fetchall()
    for row in content:
        print(row)
        Label(newWindow, text=row).pack()

def email():
    newWindow = Toplevel(root)
    newWindow.geometry("300x300")
    newWindow.title('Data: ')
    content = c.execute('SELECT * FROM WuFooData WHERE entryID = 7').fetchall()
    for row in content:
        print(row)
        Label(newWindow, text=row).pack()


label1 = Label(root, text="Some of the data listed below shows Organization Name, First Name, and Last Name.", fg='red').grid(row=1, column=1)

data1 = c.execute('SELECT org, first_name, last_name FROM WuFooData WHERE entryID = 1 ')
for i in data1:
    print(i)
    Label(root, text=i).grid(row=3, column=1)

data2 = c.execute('SELECT org, first_name, last_name FROM WuFooData WHERE entryID = 2 ')
for x in data2:
    print(x)
    Label(root, text=x).grid(row=4, column=1)

data3 = c.execute('SELECT org, first_name, last_name FROM WuFooData WHERE entryID = 3 ')
for z in data3:
    print(z)
    Label(root, text=z).grid(row=5, column=1)


data4 = c.execute('SELECT org, first_name, last_name FROM WuFooData WHERE entryID = 4 ')
for s in data4:
    print(s)
    Label(root, text=s).grid(row=6, column=1)


data5 = c.execute('SELECT org, first_name, last_name FROM WuFooData WHERE entryID = 5 ')
for t in data5:
    print(t)
    Label(root, text=t).grid(row=7, column=1)


data6 = c.execute('SELECT org, first_name, last_name FROM WuFooData WHERE entryID = 6 ')
for g in data6:
    print(g)
    Label(root, text=g).grid(row=8, column=1)


data7 = c.execute('SELECT org, first_name, last_name FROM WuFooData WHERE entryID = 7 ')
for h in data7:
    print(h)
    Label(root, text=h).grid(row=9, column=1)

btn_entryid = Button(root, text="Click to see complete entry data ", command=entryid, fg='magenta').grid(row=3 ,column=2)
btn_prefix = Button(root, text="Click to see complete entry data ", command=prefix, fg='magenta').grid(row=4 ,column=2)
btn = Button(root, text="Click to see complete entry data ", command=first_name, fg='magenta').grid(row=5 ,column=2)
btn_lastname = Button(root, text="Click to see complete entry data ", command=last_name, fg='magenta').grid(row=6 ,column=2)
btn_title = Button(root, text="Click to see complete entry data", command=title, fg='magenta').grid(row=7 ,column=2)
btn_org = Button(root, text="Click to see complete entry data", command=org, fg='magenta').grid(row=8 ,column=2)
btn_email = Button(root, text="Click to see complete entry data ", command=email, fg='magenta').grid(row=9 ,column=2)

#ENTRY LABELS
label_entry = Label(root, text="BSU Email:").grid(row=0,column=0)
entry1 = Entry(root,)
def if_selected_1():
    newWindow = Toplevel(root)
    newWindow.geometry("500x500")
    newWindow.title('Congrats you chose this project ;) ')
    # for h in
    # Entry(root, )


def change_color_button():
    """This function changes the selection button after its clicked """
    btn_select1.configure(bg="red")
    btn_select2.configure(bg="red")
    btn_select3.configure(bg="red")
    btn_select4.configure(bg="red")
    btn_select5.configure(bg="red")
    btn_select6.configure(bg="red")
    btn_select7.configure(bg="red")

# SELECTION BUTTON
btn_select1 =Button(root, text="Select to claim Project",command=change_color_button, fg='blue').grid(row=3, column=3)
btn_select2 =Button(root, text="Select to claim Project",command=change_color_button, fg='blue').grid(row=4, column=3)
btn_select3 =Button(root, text="Select to claim Project",command=change_color_button, fg='blue').grid(row=5, column=3)
btn_select4 =Button(root, text="Select to claim Project",command=change_color_button, fg='blue').grid(row=6, column=3)
btn_select5 =Button(root, text="Select to claim Project",command=change_color_button, fg='blue').grid(row=7, column=3)
btn_select6 =Button(root, text="Select to claim Project",command=change_color_button, fg='blue').grid(row=8, column=3)
btn_select7 =Button(root, text="Select to claim Project",command=change_color_button, fg='blue').grid(row=9, column=3)

"""Simple button for exiting the GUI"""
exit_button = Button(root, text="Exit ", command=root.destroy, fg='orange').grid(row=15,column=2)



root.mainloop()
