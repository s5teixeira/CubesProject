import sqlite3
from tkinter import Tk, Label, Button, Toplevel, Entry
import DatabaseStuff

root = Tk()
root.title("Cubes Project List")
root.geometry('1000x1000')
conn = sqlite3.connect("cubesProject.sqlite")
c = conn.cursor()

# create form fields for user records
label_bsuEmail = Label(root, text="Bsu Email")
label_bsuEmail.grid(row=12, column=1)

entry_bsuEmail = Entry(root)
entry_bsuEmail.grid(row=12, column=2)

label_first_name = Label(root, text="First name")
label_first_name.grid(row=13, column=1)

entry_first_name = Entry(root)
entry_first_name.grid(row=13, column=2)

label_last_name = Label(root, text="Last name")
label_last_name.grid(row=14, column=1)

entry_last_name = Entry(root)
entry_last_name.grid(row=14, column=2)

label_title = Label(root, text="Title")
label_title.grid(row=15, column=1)

entry_title = Entry(root)
entry_title.grid(row=15, column=2)

label_dept = Label(root, text="Department")
label_dept.grid(row=16, column=1)

entry_dept = Entry(root)
entry_dept.grid(row=16, column=2)

def button_click():
    """This functions gets the data from the form fields and deletes it after  """
    bsuEmail = entry_bsuEmail.get()
    first_name = entry_first_name.get()
    last_name = entry_last_name.get()
    title = entry_title.get()
    dept = entry_dept.get()
    DatabaseStuff.insert_user_data_to_table(bsuEmail, first_name, last_name, title, dept)
    entry_bsuEmail.delete(0, root.END)
    entry_first_name.delete(0, root.END)
    entry_last_name.delete(0, root.END)
    entry_title.delete(0, root.END)
    entry_dept.delete(0, root.END)
def user_autofill_data_from_email(cursor: sqlite3.Cursor):
    """This function autofills the users data based off the database"""
    cursor.execute(f"SELECT * FROM user_records WHERE bsuEmail=?", (entry_bsuEmail.get(), ))
    bsuemail = cursor.fetchone()
    if bsuemail:
        entry_first_name.delete(0, root.END)
        entry_first_name.insert(0, bsuemail[1])
        entry_last_name.delete(0, root.END)
        entry_last_name.insert(0, bsuemail[2])
        entry_title.delete(0, root.END)
        entry_title.insert(0, bsuemail[3])
        entry_dept.delete(9, root.END)
        entry_dept.insert((0, bsuemail[0]))
    conn.close()

"""These functions are the window pop opps when selecting an entry to view the entire data """
def entryid():
    newWindow = Toplevel(root)
    newWindow.geometry("300x300")
    newWindow.title('Data: ')
    content = c.execute('SELECT * FROM WuFooData WHERE entryID = 1').fetchall()
    for row in content:
        print(row, end='')
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


label1 = Label(root, text="Some of the data listed below shows Organization Name, First Name, and Last Name.", fg='red')
label1.grid(row=1, column=1)

""" These for loops display the data in a short list """
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

btn_entryid = Button(root, text="Click to see complete entry data ", command=entryid, fg='magenta')
btn_entryid.grid(row=3, column=2)

btn_prefix = Button(root, text="Click to see complete entry data ", command=prefix, fg='magenta')
btn_prefix.grid(row=4, column=2)

btn = Button(root, text="Click to see complete entry data ", command=first_name, fg='magenta')
btn.grid(row=5, column=2)

btn_lastname = Button(root, text="Click to see complete entry data ", command=last_name, fg='magenta')
btn_lastname.grid(row=6, column=2)

btn_title = Button(root, text="Click to see complete entry data", command=title, fg='magenta')
btn_title.grid(row=7, column=2)

btn_org = Button(root, text="Click to see complete entry data", command=org, fg='magenta')
btn_org.grid(row=8, column=2)

btn_email = Button(root, text="Click to see complete entry data ", command=email, fg='magenta')
btn_email.grid(row=9, column=2)

def change_color_button():
    """This function changes the selection button after its clicked """
    btn_select1.config(bg="blue", text="SELECTED")
    btn_select2.config(bg="blue", text="SELECTED")
    btn_select3.config(bg="blue", text="SELECTED")
    btn_select4.config(bg="blue", text="SELECTED")
    btn_select5.config(bg="blue", text="SELECTED")
    btn_select6.config(bg="blue", text="SELECTED")
    btn_select7.config(bg="blue", text="SELECTED")

btn_select1 = Button(root, text="Select to claim Project", command=change_color_button)
btn_select1.grid(row=3, column=3)

btn_select2 = Button(root, text="Select to claim Project", command=change_color_button)
btn_select2.grid(row=4, column=3)

btn_select3 = Button(root, text="Select to claim Project", command=change_color_button)
btn_select3.grid(row=5, column=3)

btn_select4 = Button(root, text="Select to claim Project", command=change_color_button)
btn_select4.grid(row=6, column=3)

btn_select5 = Button(root, text="Select to claim Project", command=change_color_button)
btn_select5.grid(row=7, column=3)

btn_select6 = Button(root, text="Select to claim Project", command=change_color_button)
btn_select6.grid(row=8, column=3)

btn_select7 = Button(root, text="Select to claim Project", command=change_color_button)
btn_select7.grid(row=9, column=3)

""" Simple button for submitting user records info """
submit_button = Button(root, text="Submit Info", command=button_click, fg='green')
submit_button.grid(row=20, column=2)

"""Simple button for exiting the GUI"""
exit_button = Button(root, text="Exit ", command=root.destroy, fg='orange')
exit_button.grid(row=19, column=2)

root.mainloop()
