from DatabaseStuff import open_db, close_db
import DatabaseStuff
import getData
import sys
from Gui import root

db_name = "cubesProject.sqlite"


def database():  # comment for force workflow
    json_response = getData.get_wufoo_data()
    entries_list = json_response["Entries"]
    print(entries_list[10])
    conn, cursor = open_db(db_name)
    DatabaseStuff.create_entries_table(cursor)
    DatabaseStuff.add_entries_to_db(cursor, entries_list)
    close_db(conn)

def data_visualization():
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
        database()
    elif answer == "2":
        data_visualization()
    else:
        print("Invalid Entry, ending program...")
        sys.exit(0)  # exit successfully



if __name__ == "__main__":
    main()
