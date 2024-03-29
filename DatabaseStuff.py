import sqlite3
import tkinter.messagebox
from typing import Tuple


def open_db(filename: str) -> Tuple[sqlite3.Connection, sqlite3.Cursor]:
    db_connection = sqlite3.connect(
        filename
    )  # connect to existing DB or create new one
    cursor = db_connection.cursor()  # get ready to read/write data
    return db_connection, cursor


def close_db(connection: sqlite3.Connection):
    connection.commit()  # make sure any changes get saved
    connection.close()


def create_table_for_users(cursor: sqlite3.Cursor):
    """This function creates a database form the users info"""
    try:
        cursor.execute("""CREATE TABLE IF NOT EXISTS user_records(
        bsuEmail PRIMARY KEY,
        first_name TEXT,
        last_name TEXT,
        title TEXT,
        dept TEXT );""")
    except TypeError:
        print('Unable to create users table :(')
        tkinter.messagebox.showwarning('Sqlite Error', 'Unable to create table :( ')


def insert_user_data_to_table(cursor: sqlite3.Cursor, entry_bsuEmail, entry_first_name, entry_last_name, entry_title,
                              entry_dept):
    """This function inserts the users data into the database"""
    try:
        cursor.execute(
            f"""INSERT INTO users_records '{entry_bsuEmail.get()}', '{entry_first_name.get()}',
        '{entry_last_name.get()}', '{entry_title.get()}', '{entry_dept.get()}'
        VALUES(?, ?, ?, ?, ?)""")
    except TypeError:
        print('Unable to insert values into table :(')
        tkinter.messagebox.showwarning('Sqlite Error', 'Unable to insert values into table :( ')


def create_entries_table(cursor: sqlite3.Cursor):
    create_statement = """CREATE TABLE IF NOT EXISTS WuFooData(
    entryID INTEGER PRIMARY KEY,
    prefix TEXT NOT NULL,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    title TEXT,
    org TEXT,
    email TEXT,
    website TEXT,
    course_project BOOLEAN,
    guest_speaker BOOLEAN,
    site_visit BOOLEAN,
    job_shadow BOOLEAN,
    internship BOOLEAN,
    career_panel BOOLEAN,
    networking_event BOOLEAN,
    subject_area TEXT NOT NULL,
    description TEXT,
    funding BOOLEAN,
    created_date TEXT,
    created_by TEXT);"""
    cursor.execute(create_statement)


def add_entries_to_db(cursor: sqlite3.Cursor, entries_data: list[dict]):
    # the insert or ignore syntax will insert if the primary key isn't in use or ignore if the primary key is in the DB
    insertStatement = """INSERT OR IGNORE INTO WuFooData (entryID, prefix, first_name, last_name, title, org, email, website,
    course_project, guest_speaker, site_visit, job_shadow, internship, career_panel, networking_event,
    subject_area, description, funding, created_date, created_by) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"""
    for entry in entries_data:
        entry_values = list(
            entry.values()
        )  # get the list of values from the dictionary
        entry_values[0] = int(
            entry_values[0]
        )  # the EntryID is a string, but I want it to be a number
        entry_values = entry_values[:20]
        cursor.execute(insertStatement, entry_values)
