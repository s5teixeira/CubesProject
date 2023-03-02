import sqlite3


conn = sqlite3.connect("cubesProject.sqlite")
c = conn.cursor()


# prompt user to update the data from the database
def update_records_from_database():
    print("You have selected to update the data from the database :) ")
    update_column = input('Enter the column to update: \n ')
    new_value = input('Enter the new value: \n ')
    condition = input('Enter the condition for the update:    (e.g first_name = Test) \n ')
    query = f''' 
    UPDATE WuFooData 
    SET {update_column} = ?
    WHERE {condition} '''
    c.execute(query, (new_value,)).fetchone()
    conn.commit()
    conn.close()
    print('You have updated the data in the database successfully, please refresh database to see changes :) ')
    # still need to update to make spaces for input and int values







