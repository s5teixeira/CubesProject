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

   #add try execpt and print tables were printed



# def make_intial_students(cursor:sqlite3.Cursor):
#  cursor.execute(f'''INSERT INTO STUDENTS (banner_id, first_name, last_name, gpa, credits)
#  VALUES (1001, "John", "Santore", {random.uniform(0.0,4.0)},
# {random.randint(0,120)})''')
#  cursor.execute(f'''INSERT INTO STUDENTS(banner_id, first_name, last_name, gpa, credits)
#  VALUES(1002, "Enping", "Li", {random.uniform(0.0, 4.0)}, {random.randint(0,
# 120)})''')
#  cursor.execute(f'''INSERT INTO STUDENTS(banner_id, first_name, last_name, gpa, credits)
#  VALUES(1003, "Margaret", "Black", {random.uniform(0.0, 4.0)}, {random.randint(0, 120)})''')
#  cursor.execute(f'''INSERT INTO STUDENTS(banner_id, first_name, last_name, gpa, credits)
#  VALUES(1004, "Seikyung", "Jung", {random.uniform(0.0, 4.0)}, {random.randint(0,
# 120)})''')
#  cursor.execute(f'''INSERT INTO STUDENTS(banner_id, first_name, last_name, gpa, credits)
#  VALUES(1005, "Haleh", "Khojasteh", {random.uniform(0.0, 4.0)},
# {random.randint(0, 120)})''')

# def show_simple_select(cursor:sqlite3.Cursor):
#  cutoff = float(input("What should the GPA cutoff be?"))
#  #question to class-what about security issues here?
#  #Discuss
#  result = cursor.execute(f'SELECT * from STUDENTS WHERE\ gpa < {cutoff}')
#  for row in result:
#  print(f'BannerId: {row[0]}\nName: {row[1]}\
#  {row[2]}\nGPA:{row[4]}')

# def make_initial_classLists(cursor:sqlite3.Cursor):
# cursor.execute(f'''INSERT INTO CLASS_LIST (banner_id, course_prefix, course_number, registration_date)
# VALUES(1001, 'Comp', 490, DATE('now'))
# ''')
# cursor.execute(f'''INSERT INTO CLASS_LIST (banner_id, course_prefix, course_number, registration_date)
# VALUES(1002, 'Comp', 490, DATE('now'))
# ''')
# cursor.execute(f'''INSERT INTO CLASS_LIST (banner_id, course_prefix, course_number, registration_date)
# VALUES(1003, 'Comp', 490, DATE('now'))
# ''')
# cursor.execute(f'''INSERT INTO CLASS_LIST (banner_id, course_prefix, course_number, registration_date)
# VALUES(1004, 'Comp', 490, DATE('now'))
# ''')
# cursor.execute(f'''INSERT INTO CLASS_LIST (banner_id, course_prefix, course_number, registration_date)
# VALUES(1005, 'Comp', 490, DATE('now'))
# ''')


# def inserting_values_into_data(cursor: sqlite3.Cursor):
#     response = requests.get(url, auth=(username, password))
#     data = json.loads(response.text)
#     try:
#         for record in data:
#             cursor.execute('''INSERT INTO wufoo_db VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
#                                   (record.get('name', None),
#                                    record.get('mass', None),
#                                    record.get('reclat', None),
#                                    record.get('reclong', None),
#
#                            #        record.get(':@computed_region_cbhk_fwbd', None),
#                             #       record.get(':@computed_region_nnqa_25f4', None)))
#
#             # run a SELECT query on the table that holds all meteorite data
#             cursor.execute('SELECT * FROM meteorite_data WHERE id <= 1000')
#             # get the result of the query as a list of tuples
#         #    cursor.fetchall()
#     # catch any database errors
#     except sqlite3.Error as db_error:
#         # print the error description
#         print(f'A Database Error has occurred: {db_error}')
#


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

    # connect_to_database()
    # setup_db()
    # close_db()
    # message()
    # get_wufoo_data1()
    # get_wufoo_data2()
    # get_wufoo_data3()
    # get_wufoo_data4()
