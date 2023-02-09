import sqlite3
import sys
import requests
import json
from secrets import wufoo_key

subdomain = 'https://stepht15.wufoo.com/api/v3/'
# comment to test workflow
format = 'forms/cubes-project-proposal-submission/entries/json'
url = subdomain + format
username = wufoo_key
password = 'helloworld'
wufoo_file = open('txtfile.txt', 'w')


def database():
    """This function connects to the sqlite3 database and opens a text file """
    db_connection = None
    try:
        db_connection = connect_to_db('wufoo_db.db')
        db_cursor = create_db_cursor(db_connection)
        db_cursor = setup_db()

        #     db_cursor = call_to_create_all_tables(db_cursor)
        #    open("output_data.txt", "w").write("")
        #    open("txtfile.txt", "w").write("")
        #  open(wufoo_file)
        open('txtfile.txt', 'w')
    #       call_to_getsearchurl(db_cursor)
    except sqlite3.Error as db_error:
        print(f'A Database Error has occurred: {db_error}')
    finally:
        if db_connection:
            db_connection.commit()
            db_connection.close()
            print('\n\nDatabase connection closed.')


def connect_to_db(wufoo_db: str):
    """" this function connects to the database"""
    db_connection = None
    try:
        db_connection = sqlite3.connect(wufoo_db)
        print('connection to database was successful :)')
    except sqlite3.Error as db_error:
        print(f'{db_error}: connection to database was unsuccessful :(')
    finally:
        return db_connection


def create_db_cursor(db_connection_obj: sqlite3.Connection):
    """ this function creates the database cursor object"""
    cursor_obj = None
    try:
        cursor_obj = db_connection_obj.cursor()
        print(f'cursor object created successfully on {db_connection_obj}\n')
    except sqlite3.Error as db_error:
        print(f'cursor object could not be created: {db_error}')
    finally:
        return cursor_obj


def setup_db(cursor: sqlite3.db_cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS wufoo_table(
    entry_id INTEGER PRIMARY KEY,
    prefix TEXT,
    Name TEXT NOT NULL,
    Title TEXT NOT NULL,
    Organization_name TEXT NOT NULL,
    Email TEXT NOT NULL,
    Organization_website TEXT,
    phone TEXT);
    ''')


# still need last 3 open ended questions from form !!! #

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


if __name__ == '__main__':
    database()
    connect_to_db
    message()
    get_wufoo_data1()
    get_wufoo_data2()
    get_wufoo_data3()
    get_wufoo_data4()
