import sqlite3
from tkinter import Tk, Label, Button, Toplevel, Text, Entry, StringVar, OptionMenu
root = Tk()
root.title("Cubes Project List")
root.geometry('900x900')
conn = sqlite3.connect("cubesProject.sqlite")
c = conn.cursor()
def entryid():
    newWindow = Toplevel(root)
    newWindow.geometry("300x300")
    newWindow.title('Data: ')
    content = c.execute('SELECT * FROM WuFooData WHERE entryID = 1').fetchall()
    for row in content:
        print(row)
        Label(newWindow, text=row)

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

# def website():
#     newWindow = Toplevel(root)
#     newWindow.geometry("300x300")
#     newWindow.title('Data: ')
#     content = c.execute('SELECT website FROM WuFooData').fetchall()
#     for row in content:
#         print(row)
#         Label(newWindow, text=row).pack()
#
# def courseproject():
#     newWindow = Toplevel(root)
#     newWindow.geometry("300x300")
#     newWindow.title('Data: ')
#     content = c.execute('SELECT course_project FROM WuFooData').fetchall()
#     for row in content:
#         print(row)
#         Label(newWindow, text=row).pack()
#
# def guestspeaker():
#     newWindow = Toplevel(root)
#     newWindow.geometry("300x300")
#     newWindow.title('Data: ')
#     content = c.execute('SELECT guest_speaker FROM WuFooData').fetchall()
#     for row in content:
#         print(row)
#         Label(newWindow, text=row).pack()
#
# def sitevisit():
#     newWindow = Toplevel(root)
#     newWindow.geometry("300x300")
#     newWindow.title('Data: ')
#     content = c.execute('SELECT site_visit FROM WuFooData').fetchall()
#     for row in content:
#         print(row)
#         Label(newWindow, text=row).pack()
#
# def jobshadow():
#     newWindow = Toplevel(root)
#     newWindow.geometry("300x300")
#     newWindow.title('Data: ')
#     content = c.execute('SELECT job_shadow FROM WuFooData').fetchall()
#     for row in content:
#         print(row)
#         Label(newWindow, text=row).pack()
#
# def internship():
#     newWindow = Toplevel(root)
#     newWindow.geometry("300x300")
#     newWindow.title('Data: ')
#     content = c.execute('SELECT internship FROM WuFooData').fetchall()
#     for row in content:
#         print(row)
#         Label(newWindow, text=row).pack()
#
# def careerpanel():
#     newWindow = Toplevel(root)
#     newWindow.geometry("300x300")
#     newWindow.title('Data: ')
#     content = c.execute('SELECT career_panel FROM WuFooData').fetchall()
#     for row in content:
#         print(row)
#         Label(newWindow, text=row).pack()
#
# def networkingevent():
#     newWindow = Toplevel(root)
#     newWindow.geometry("300x300")
#     newWindow.title('Data: ')
#     content = c.execute('SELECT networking_event FROM WuFooData').fetchall()
#     for row in content:
#         print(row)
#         Label(newWindow, text=row).pack()
#
# def subjectarea():
#     newWindow = Toplevel(root)
#     newWindow.geometry("300x300")
#     newWindow.title('Data: ')
#     content = c.execute('SELECT subject_area FROM WuFooData').fetchall()
#     for row in content:
#         print(row)
#         Label(newWindow, text=row).pack()
#
# def description():
#     newWindow = Toplevel(root)
#     newWindow.geometry("300x300")
#     newWindow.title('Data: ')
#     content = c.execute('SELECT description FROM WuFooData').fetchall()
#     for row in content:
#         print(row)
#         Label(newWindow, text=row).pack()
#
# def funding():
#     newWindow = Toplevel(root)
#     newWindow.geometry("300x300")
#     newWindow.title('Data: ')
#     content = c.execute('SELECT funding FROM WuFooData').fetchall()
#     for row in content:
#         print(row)
#         Label(newWindow, text=row).pack()
#
# def createddate():
#     newWindow = Toplevel(root)
#     newWindow.geometry("300x300")
#     newWindow.title('Data: ')
#     content = c.execute('SELECT created_date FROM WuFooData').fetchall()
#     for row in content:
#         print(row)
#         Label(newWindow, text=row).pack()
#
# def createdby():
#     newWindow = Toplevel(root)
#     newWindow.geometry("300x300")
#     newWindow.title('Data: ')
#     content = c.execute('SELECT created_by FROM WuFooData').fetchall()
#     for row in content:
#         print(row)
#         Label(newWindow, text=row).pack()


#label = Label(root, text="Select one of the entries to view the complete entry data: ", fg='red').grid(row=1, column=1)
label2 = Label(root, text="Some of the data listed below shows Organization name, first name, and last name.", fg='red').grid(row=1, column=1)

data1 = c.execute('SELECT org, first_name, last_name FROM WuFooData WHERE entryID = 1 ')
for i in data1:
    print(i)
    Label(root, text=i).grid(row=3, column=1)

data2 = c.execute('SELECT org, first_name, last_name FROM WuFooData WHERE entryID = 2 ')
for x in data2:
    print(x)
    Label(root, text=x).grid(row=4, column=1)

data3 = c.execute('SELECT org, first_name, last_name FROM WuFooData WHERE entryID = 3 ')
for x in data3:
    print(x)
    Label(root, text=x).grid(row=5, column=1)


data4 = c.execute('SELECT org, first_name, last_name FROM WuFooData WHERE entryID = 4 ')
for x in data4:
    print(x)
    Label(root, text=x).grid(row=6, column=1)


data5 = c.execute('SELECT org, first_name, last_name FROM WuFooData WHERE entryID = 5 ')
for x in data5:
    print(x)
    Label(root, text=x).grid(row=7, column=1)


data6 = c.execute('SELECT org, first_name, last_name FROM WuFooData WHERE entryID = 6 ')
for x in data6:
    print(x)
    Label(root, text=x).grid(row=8, column=1)


data7 = c.execute('SELECT org, first_name, last_name FROM WuFooData WHERE entryID = 7 ')
for x in data7:
    print(x)
    Label(root, text=x).grid(row=9, column=1)


btn_entryid = Button(root, text="Click to see complete entry data ", command=entryid, fg='magenta').grid(row=3 ,column=2)
btn_prefix = Button(root, text="Click to see complete entry data ", command=prefix, fg='magenta').grid(row=4 ,column=2)
btn = Button(root, text="Click to see complete entry data ", command=first_name, fg='magenta').grid(row=5 ,column=2)
btn_lastname = Button(root, text="Click to see complete entry data ", command=last_name, fg='magenta').grid(row=6 ,column=2)
btn_title = Button(root, text="Click to see complete entry data", command=title, fg='magenta').grid(row=7 ,column=2)
btn_org = Button(root, text="Click to see complete entry data", command=org, fg='magenta').grid(row=8 ,column=2)
btn_email = Button(root, text="Click to see complete entry data ", command=email, fg='magenta').grid(row=9 ,column=2)
# btn_website = Button(root, text="Click to see list of Website's ", command=website, fg='magenta').pack()
# btn_courseproject = Button(root, text="Click to see list of Course Projects ", command=courseproject,fg='magenta').pack()
# btn_guestspeaker = Button(root, text="Click to see list of Guest Speakers ", command=guestspeaker, fg='magenta').pack()
# btn_sitevisit = Button(root, text="Click to see list of Sites Visits ", command=sitevisit, fg='magenta').pack()
# btn_jobshadow = Button(root, text="Click to see list of Job Shadows ", command=jobshadow, fg='magenta').pack()
# btn_internship = Button(root, text="Click to see list of Internships ", command=internship, fg='magenta').pack()
# btn_careerpanel = Button(root, text="Click to see list of Career Panels ", command=careerpanel, fg='magenta').pack()
# btn_networkingevent = Button(root, text="Click to see list of Networking Events ", command=networkingevent,fg='magenta').pack()
# btn_subjectarea = Button(root, text="Click to see list of Subject Areas ", command=subjectarea, fg='magenta').pack()
# btn_description = Button(root, text="Click to see list of Descriptions ", command=description, fg='magenta').pack()
# btn_funding = Button(root, text="Click to see list of Fundings ", command=funding, fg='magenta').pack()
# btn_createddate = Button(root, text="Click to see list of Created Dates ", command=createddate, fg='magenta').pack()
# btn_createdby = Button(root, text="Click to see list of Created By ", command=createdby, fg='magenta').pack()

"""Simple button for exiting the GUI"""
exit_button = Button(root, text="Exit ", command=root.destroy).grid(row=15,column=2)

root.mainloop()
