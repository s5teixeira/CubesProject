from DatabaseStuff import open_db, close_db
import DatabaseStuff
import getData
from tkinter import *
import sqlite3

db_name = "cubesProject.sqlite"


def main():
    json_response = getData.get_wufoo_data()
    entries_list = json_response["Entries"]
    conn, cursor = open_db(db_name)
    DatabaseStuff.create_entries_table(cursor)
    DatabaseStuff.add_entries_to_db(cursor, entries_list)
    # submit(cursor)
    close_db(conn)


#
# root = Tk()
# root.title("Cubes Project List")
# root.geometry('500x500')
#
# # get database
# conn = sqlite3.connect(db_name)
# c = conn.cursor()
#
# # CREATE TEXT BOXES
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
# emailtextbox.grid(row=5, column=1)
#
# websitetextbox = Entry(root, width=30)
# websitetextbox.grid(row=5, column=1)
#
# course_projecttextbox = Entry(root, width=30)
# course_projecttextbox.grid(row=5, column=1)
#
# guest_speakertextbox = Entry(root, width=30)
# guest_speakertextbox.grid(row=5, column=1)
#
# site_visittextbox = Entry(root, width=30)
# site_visittextbox.grid(row=5, column=1)
#
# job_shadowtextbox = Entry(root, width=30)
# job_shadowtextbox.grid(row=5, column=1)
#
# internshiptextbox = Entry(root, width=30)
# internshiptextbox.grid(row=5, column=1)
#
# career_paneltextbox = Entry(root, width=30)
# career_paneltextbox.grid(row=5, column=1)
#
# networking_eventtextbox = Entry(root, width=30)
# networking_eventtextbox.grid(row=5, column=1)
#
# subject_areatextbox = Entry(root, width=30)
# subject_areatextbox.grid(row=5, column=1)
#
# descriptiontextbox = Entry(root, width=30)
# descriptiontextbox.grid(row=5, column=1)
#
# fundingtextbox = Entry(root, width=30)
# fundingtextbox.grid(row=5, column=1)
#
# created_datetextbox = Entry(root, width=30)
# created_datetextbox.grid(row=5, column=1)
#
# created_bytextbox = Entry(root, width=30)
# created_bytextbox.grid(row=5, column=1)
#
# ################# CREATE TEXT BOX LABELS ######################
# entryidlabel = Label(root, text="EntryID:   ", )
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
# titlelabel.grid(row=3, column=0)
#
# orglabel = Label(root, text="Organization:    ", )
# orglabel.grid(row=3, column=0)
#
# emaillabel = Label(root, text="Email:   ", )
# emaillabel.grid(row=3, column=0)
#
# websitelabel = Label(root, text="Website:   ", )
# websitelabel.grid(row=3, column=0)
#
# courseprojectlabel = Label(root, text="Course Project:   ", )
# courseprojectlabel.grid(row=3, column=0)
#
# guestspeakerlabel = Label(root, text="Guest Speaker:   ", )
# guestspeakerlabel.grid(row=3, column=0)
#
# sitevisitlabel = Label(root, text="Site Visit:   ", )
# sitevisitlabel.grid(row=3, column=0)
#
# jobshadowlabel = Label(root, text="Job Shadow:   ", )
# jobshadowlabel.grid(row=3, column=0)
#
# internshiplabel = Label(root, text="Internship:   ", )
# internshiplabel.grid(row=3, column=0)
#
# careerpanellabel = Label(root, text="Career Pane:   ", )
# careerpanellabel.grid(row=3, column=0)
#
# networkingeventlabel = Label(root, text="Networking Event :   ", )
# networkingeventlabel.grid(row=3, column=0)
#
# subjectarealabel = Label(root, text="Subject Area:   ", )
# subjectarealabel.grid(row=3, column=0)
#
# descriptionlabel = Label(root, text="Description:   ", )
# descriptionlabel.grid(row=3, column=0)
#
# fundinglabel = Label(root, text="Funding:   ", )
# fundinglabel.grid(row=3, column=0)
#
# createdbylabel = Label(root, text="Created By:   ", )
# createdbylabel.grid(row=3, column=0)
#
# createddatelabel = Label(root, text="Created Date:   ", )
# createddatelabel.grid(row=3, column=0)
#
# root.mainloop()
# def submit(cursor: sqlite3.Cursor):
#     #    conn = sqlite3.connect(db_name)
#     #    c = conn.cursor()
#     # insert into gui
#     cursor.execute(
#         "INSERT INTO example123 VALUES (:entryidtextbox, :prefixtextbox, :f_nametextbox, :l_nametextbox, :titletextbox, :orgtextbox) ",
#         {
#             'entryidtextbox': entryidtextbox.get(),
#             'prefixtextbox': prefixtextbox.get(),
#             'f_nametextbox': f_nametextbox.get(),
#             'l_nametextbox': l_nametextbox.get(),
#             'titletextbox': titletextbox.get(),
#             'orgtextbox': orgtextbox.get()
#
#         })
#
#     cursor.commit()
#
#     cursor.close()
#

# Execute Tkinter
# root.mainloop()

if __name__ == "__main__":
    main()
