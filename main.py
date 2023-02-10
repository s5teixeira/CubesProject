import sqlite3
import sys
import requests
import json
from secrets import wufoo_key

subdomain = 'https://stepht15.wufoo.com/api/v3/'
format = 'forms/cubes-project-proposal-submission/entries/json'
url = subdomain + format
username = wufoo_key
password = 'helloworld'
wufoo_file = open('txtfile.txt', 'w')


def connect_to_database():
    """This function connects to the sqlite3 database and opens a text file """
    db_connection = None
    try:
        db_connection = sqlite3.connect('wufoo_db.db')
        cursor = db_connection.cursor()
        print('connection to database was successful')
        return db_connection, cursor
    except sqlite3.Connection.Error as error:
        print(f'A Database Error has occurred: {error}')


def close_db(connection: sqlite3.Connection):
    """this function commits and closes database """
    connection.commit()  # make sure any changes get saved
    connection.close()


def setup_db(cursor: sqlite3.Cursor):
    """This function creates the table"""
    cursor.execute('''CREATE TABLE IF NOT EXISTS table_forms(
    entry_id INTEGER PRIMARY KEY,
    prefix TEXT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    Title TEXT NOT NULL,
    Organization_name TEXT NOT NULL,
    Email TEXT NOT NULL,
    Organization_website TEXT,
    phone TEXT);
    ''')


def make_initial_entries(cursor: sqlite3.Cursor):
    """Inserting in my own data"""
    entry_id = 150
    prefix = "Ms"
    first_name = "Stephanie"
    last_name = "Teixeira"
    Title = "student"
    Organization_name = "bsu"
    Email = "student.bridgew.edu"
    Organization_website = "www.company.com"
    phone = '78788787878'
    cursor.execute(f'''INSERT INTO table_forms(entry_id, prefix, first_name, last_name, Title, Organization_name,
    Email, Organization_website, phone)VALUES({entry_id}, '{prefix}' ,'{first_name}', '{last_name}', '{Title}',
    '{Organization_name}', '{Email}', '{Organization_website}', '{phone}'  )''')


def message():
    response = requests.get(url, auth=(username, password))
    if response.status_code != 200:
        print(f"Failed to get data, response code:{response.status_code} and error message: {response.reason} ")
        print(response.raise_for_status())
        sys.exit(-1)


def get_wufoo_data1():
    response = requests.get(url, auth=(username, password))
    data = json.loads(response.text)
    print(json.dumps(data, indent=4, sort_keys=True))


def get_wufoo_data2():
    response = requests.get(url, auth=(username, password))
    data = json.loads(response.text)
    print(json.dumps(data, indent=4, sort_keys=True))


def get_wufoo_data3():
    response = requests.get(url, auth=(username, password))
    data = json.loads(response.text)
    wufoo_file.write(str(data))
    print(json.dumps(data, indent=4, sort_keys=True))


def get_wufoo_data4():
    response = requests.get(url, auth=(username, password))
    data = json.loads(response.text)
    wufoo_file.write(str(data))
    print(json.dumps(data, indent=4, sort_keys=True))


def main():
    conn, cursor = connect_to_database()
    print(type(conn))
    setup_db(cursor)
    make_initial_entries(cursor)
    close_db(conn)


if __name__ == '__main__':
    main()
