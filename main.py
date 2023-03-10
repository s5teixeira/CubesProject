import update_database
from DatabaseStuff import open_db, close_db
import DatabaseStuff
import getData
import sys
from Gui import root

db_name = "cubesProject.sqlite"

def database():
    json_response = getData.get_wufoo_data()
    entries_list = json_response["Entries"]
    conn, cursor = open_db(db_name)
    DatabaseStuff.create_entries_table(cursor)
    DatabaseStuff.create_table_for_users(cursor)
    DatabaseStuff.add_entries_to_db(cursor, entries_list)
    close_db(conn)

def data_visualization():
    database()
    root.mainloop()

def show_options():
    print("=======================================")
    print("[1] Update the database with wufoo data")
    print("[2] Run the Graphical Program")
    print("=======================================")

def main():
    show_options()
    answer = input("Please enter your choice:")
    if answer == "1":
        update_database.update_records_from_table()
    elif answer == "2":
        data_visualization()
    else:
        print("Invalid Entry, ending program...")
        sys.exit(0)

if __name__ == "__main__":
    main()
