from tkinter import *
import sqlite3

root = Tk()
root.title("Cubes Project List")
root.geometry('700x700')
conn = sqlite3.connect("cubesProject.sqlite")
c = conn.cursor()


label = Label(root, text="Select one of the entries to view the entry data: ", fg='red').pack()


def entryid():
    newWindow = Toplevel(root)
    newWindow.geometry("300x300")
    newWindow.title('Data: ')
    content = c.execute('SELECT entryID FROM WuFooData').fetchall()
    for row in content:
        print(row)
        Label(newWindow, text=row).pack()


btn_entryid = Button(root, text="Click to see list of Entry ID's ", command=entryid,fg='magenta').pack()


def prefix():
    newWindow = Toplevel(root)
    newWindow.geometry("300x300")
    newWindow.title('Data: ')
    content = c.execute('SELECT prefix FROM WuFooData').fetchall()
    for row in content:
        print(row)
        Label(newWindow, text=row).pack()


btn_prefix = Button(root, text="Click to see list of Prefix's ", command=prefix,fg='magenta').pack()


def first_name():
    newWindow = Toplevel(root)
    newWindow.geometry("300x300")
    newWindow.title('Data: ')
#    btn = Button(root, text="Click to see list of first names ", command=newWindow)
#    btn.pack(pady=10)
    content = c.execute('SELECT first_name FROM WuFooData').fetchall()
    for row in content:
        print(row)
        Label(newWindow, text=row).pack()



btn = Button(root, text="Click to see list of First Names ", command=first_name, fg='magenta').pack()

def last_name():
    newWindow = Toplevel(root)
    newWindow.geometry("300x300")
    newWindow.title('Data: ')
    content = c.execute('SELECT last_name FROM WuFooData').fetchall()
    for row in content:
        print(row)
        Label(newWindow, text=row).pack()


btn_lastname = Button(root, text="Click to see list of Last Names ", command=last_name,fg='magenta').pack()

def title():
    newWindow = Toplevel(root)
    newWindow.geometry("300x300")
    newWindow.title('Data: ')
    content = c.execute('SELECT title FROM WuFooData').fetchall()
    for row in content:
        print(row)
        Label(newWindow, text=row).pack()


btn_title = Button(root, text="Click to see list of Title's ", command=title,fg='magenta').pack()

def org():
    newWindow = Toplevel(root)
    newWindow.geometry("300x300")
    newWindow.title('Data: ')
    content = c.execute('SELECT title FROM WuFooData').fetchall()
    for row in content:
        print(row)
        Label(newWindow, text=row).pack()


btn_org = Button(root, text="Click to see list of Organizations ", command=org,fg='magenta').pack()


































if __name__ == "__main__":
    entryid()
    prefix()
    first_name()
    last_name()
    title()
    org()
    root.mainloop()


# def all_the_entry_boxes():
#     websitetextbox = Entry(root, width=30)
#     websitetextbox.grid(row=7, column=1)
#
#     course_projecttextbox = Entry(root, width=30)
#     course_projecttextbox.grid(row=8, column=1)
#
#     guest_speakertextbox = Entry(root, width=30)
#     guest_speakertextbox.grid(row=9, column=1)
#
#     site_visittextbox = Entry(root, width=30)
#     site_visittextbox.grid(row=10, column=1)
#
#     job_shadowtextbox = Entry(root, width=30)
#     job_shadowtextbox.grid(row=11, column=1)
#
#     root.mainloop()



#
# B = root.Button(text="Click this button to see list of first names!!")
# #B.pack()
# firstnameMessageBox = c.execute('SELECT first_name FROM WuFooData')
#
# firstname_button = Button(root, text="First name button click here", command=firstnameMessageBox)
# firstname_button.grid(row=23, column=10)
#
# firstnameMessageBox.pack()
#
# for output in firstnameMessageBox:
#    print(output)

# def get_db_data_to_gui() -> list[dict]:
#     conn = sqlite3.connect("cubesProject.sqlite")
#     c = conn.cursor()
#     data_list = []
#     record = {" prefix ": prefixtextbox, "first_name": f_nametextbox }
#     data_list.insert(record(c))
#     return data_list


# def submit(cursor: sqlite3.Cursor):
#         conn = sqlite3.connect(db_name)
#         c = conn.cursor()
#     # insert into gui
#     cursor.execute(
#         "INSERT INTO wufoo_db VALUES (:entryidtextbox, :prefixtextbox, :f_nametextbox, :l_nametextbox, :titletextbox, :orgtextbox) ",
#         {
#             'entryidtextbox': entryidtextbox.get(),
#             'prefixtextbox': prefixtextbox.get(),
#             'f_nametextbox': f_nametextbox.get(),
#             'l_nametextbox': l_nametextbox.get(),
#             'titletextbox': titletextbox.get(),
#             'orgtextbox': orgtextbox.get()
#
#         })

#    cursor.commit()

#    cursor.close()


# CREATE TEXT BOXES
# entryidtextbox = Entry(root, width=30)
# entryidtextbox.grid(row=0, column=1, padx=20)
#
# prefixtextbox = Entry(root, width=30)
# prefixtextbox.grid(row=1, column=1)
#
# f_nametextbox = Entry(root, width=30)
# f_nametextbox.grid(row=2, column=1)
#
# l_nametextbox = Entry(root, width=30)
# l_nametextbox.grid(row=3, column=1)
#
# titletextbox = Entry(root, width=30)
# titletextbox.grid(row=4, column=1)
#
# orgtextbox = Entry(root, width=30)
# orgtextbox.grid(row=5, column=1)
#
# emailtextbox = Entry(root, width=30)
# emailtextbox.grid(row=6, column=1)
#
# websitetextbox = Entry(root, width=30)
# websitetextbox.grid(row=7, column=1)
#
# course_projecttextbox = Entry(root, width=30)
# course_projecttextbox.grid(row=8, column=1)
#
# guest_speakertextbox = Entry(root, width=30)
# guest_speakertextbox.grid(row=9, column=1)
#
# site_visittextbox = Entry(root, width=30)
# site_visittextbox.grid(row=10, column=1)
#
# job_shadowtextbox = Entry(root, width=30)
# job_shadowtextbox.grid(row=11, column=1)
#
# internshiptextbox = Entry(root, width=30)
# internshiptextbox.grid(row=12, column=1)
#
# career_paneltextbox = Entry(root, width=30)
# career_paneltextbox.grid(row=13, column=1)
#
# networking_eventtextbox = Entry(root, width=30)
# networking_eventtextbox.grid(row=14, column=1)
#
# subject_areatextbox = Entry(root, width=30)
# subject_areatextbox.grid(row=15, column=1)
#
# descriptiontextbox = Entry(root, width=30)
# descriptiontextbox.grid(row=16, column=1)
#
# fundingtextbox = Entry(root, width=30)
# fundingtextbox.grid(row=17, column=1)
#
# created_datetextbox = Entry(root, width=30)
# created_datetextbox.grid(row=18, column=1)
#
# created_bytextbox = Entry(root, width=30)
# created_bytextbox.grid(row=19, column=1)
#
# ################# CREATE TEXT BOX LABELS ######################
# entryidlabel = Label(root, text="EntryID:   ") # bg='magenta'
# entryidlabel.grid(row=0, column=0)
#
# prefixlabel = Label(root, text="Prefix:   ", )
# prefixlabel.grid(row=1, column=0)
#
# f_namelabel = Label(root, text="First Name:   ", )
# f_namelabel.grid(row=2, column=0)
#
# l_namelabel = Label(root, text="Last Name:   ", )
# l_namelabel.grid(row=3, column=0)
#
# titlelabel = Label(root, text="Title:   ", )
# titlelabel.grid(row=4, column=0)
#
# orglabel = Label(root, text="Organization:    ", )
# orglabel.grid(row=5, column=0)
#
# emaillabel = Label(root, text="Email:   ", )
# emaillabel.grid(row=6, column=0)
#
# websitelabel = Label(root, text="Website:   ", )
# websitelabel.grid(row=7, column=0)
#
# courseprojectlabel = Label(root, text="Course Project:   ", )
# courseprojectlabel.grid(row=8, column=0)
#
# guestspeakerlabel = Label(root, text="Guest Speaker:   ", )
# guestspeakerlabel.grid(row=9, column=0)
#
# sitevisitlabel = Label(root, text="Site Visit:   ", )
# sitevisitlabel.grid(row=10, column=0)
#
# jobshadowlabel = Label(root, text="Job Shadow:   ", )
# jobshadowlabel.grid(row=11, column=0)
#
# internshiplabel = Label(root, text="Internship:   ", )
# internshiplabel.grid(row=12, column=0)
#
# careerpanellabel = Label(root, text="Career Pane:   ", )
# careerpanellabel.grid(row=13, column=0)
#
# networkingeventlabel = Label(root, text="Networking Event:   ", )
# networkingeventlabel.grid(row=14, column=0)
#
# subjectarealabel = Label(root, text="Subject Area:   ", )
# subjectarealabel.grid(row=15, column=0)
#
# descriptionlabel = Label(root, text="Description:   ", )
# descriptionlabel.grid(row=16, column=0)
#
# fundinglabel = Label(root, text="Funding:   ", )
# fundinglabel.grid(row=17, column=0)
#
# createdbylabel = Label(root, text="Created By:   ", )
# createdbylabel.grid(row=18, column=0)
#
# createddatelabel = Label(root, text="Created Date:   ", )
# createddatelabel.grid(row=19, column=0)

# Button for closing
# exit_button = Button(root, text="Exit", command=root.destroy)
# exit_button.grid(row=20, column=8)

# root.configure(background="magenta")

#root.mainloop()

# from tkinter import *
# import tkinter as tk
#
# # When the user selects one of the entries from your list, display the complete entry data in a Graphical User interface
# import cursor as cursor
# import getData
# import DatabaseStuff
# import sqlite3
#
# from main import main
#
# conn = sqlite3.connect('cubesProject.sqlite')
# cursor = conn.cursor()
#
# class Window():
#     def __init__(self):
#         super().__init__()
#         # Creating the tkinter Window
#         self.root = Tk()
#         self.root.title("Cubes Project List")
#         self.root.geometry('400x350')
#
#         # Button for closing
#         exit_button = Button(self.root, text="Exit", command=self.root.destroy)
#         exit_button.grid(column=0, row=0)
#
#         # LABELS
#         prefix_label = Label(self.root, text="Prefix:  ", bg='magenta')
#         prefix_label.grid(column=0, row=1)
#         #       prefix_label.insert(json_response[0])
#
#         first_nameLabel = Label(self.root, text="First Name:  ", bg='magenta')
#         first_nameLabel.grid(column=0, row=2)
#
#         last_nameLabel = Label(self.root, text="Last Name:  ", bg='magenta')
#         last_nameLabel.grid(column=0, row=3)
#
#         titleLabel = Label(self.root, text="Title:  ", bg='magenta')
#         titleLabel.grid(column=0, row=4)
#
#         organization_nameLabel = Label(self.root, text="Organization Name:  ", bg='magenta')
#         organization_nameLabel.grid(column=0, row=5)
#
#         emailLabel = Label(self.root, text="Email:  ", bg='magenta')
#         emailLabel.grid(column=0, row=6)
#
#         org_websiteLabel = Label(self.root, text="Organization Website:  ", bg='magenta')
#         org_websiteLabel.grid(column=0, row=7)
#
#         entryidlabel = Label(self.root, text="Entry ID:   ", bg='magenta')
#         entryidlabel.grid(column=0, row=8)
#         entryidlabel.insert(DatabaseStuff.add_entries_to_db(cursor))
