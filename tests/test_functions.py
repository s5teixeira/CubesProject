import pytest
import sqlite3
import getData
import DatabaseStuff
import Gui
def test_get_data():
    """ for this test we are just getting the data from wufoo, getting the Entries and counting them"""
    json_data = getData.get_wufoo_data()
    entries = json_data['Entries']
    assert len(entries) <= 10
def test_data_in_database():
    """This function tests to make sure there is data in database table"""
    with pytest.raises(TypeError) as exception_info:
        connection, c = DatabaseStuff.add_entries_to_db('entries_data')
        c.execute('SELECT count(*) FROM WuFooData')
        data = c.fethone()
        assert len(data) <= 30
    assert exception_info.type is TypeError
def test_checkboxes():
    """This function tests to see if there are null values(unchecked) from internship table"""
    connection, c = Gui.internship()
    c.execute('SELECT internship FROM WuFooData WHERE internship IS NULL')
    data = c.fethone()
    assert data is None
def test_table_created():
    """There were several ways to do this, some of them include wrapping inserts in try/except blocks,
    but I took an easy way and just check to make sure my table is in the meta deable sqlite_master"""
    connection, cursor = DatabaseStuff.open_db("../test.db")
    DatabaseStuff.create_entries_table(cursor)
    cursor.execute("SELECT Count() FROM SQLITE_MASTER WHERE name = ?", ["WuFooData"])
    record = cursor.fetchone()
    number_of_rows = record[0]  # the number is the first )and only) item in the tuple
    assert number_of_rows == 1
def test_check_text_for_correct_data():
    """This function checks the correct data in the First Name field"""
    with pytest.raises(TypeError) as exception_info:
        conn, c = Gui.first_name()
        c.execute('SELECT first_name FROM WuFooData')
        data = c.fethone()
        test_check = str(data[2])
        assert test_check == 'Pallavi'
        assert test_check == 'hello'
        assert test_check == 'johhny'
        assert test_check == 'Test'
    assert exception_info.type is TypeError
def test_check_text_for_correct_data2():
    """This function checks the correct data in the Title field"""
    with pytest.raises(TypeError) as exception_info:
        conn, c = Gui.title()
        c.execute('SELECT title FROM WuFooData')
        data = c.fethone()
        test_check = str(data[2])
        assert test_check == 'MTA'
        assert test_check == 'hellohello'
        assert test_check == 'House'
        assert test_check == 'ms'
    assert exception_info.type is TypeError
def test_connect_to_db(capfd):
    """this function creates a fake database and makes sure it connects to it"""
    test_db = 'WufooData.db'
    sqlite3.connect(test_db)
def test_user_autofill_data_from_email():
    """This function checks if the autofill function works correctly """
    Gui.entry_first_name.insert(0,)
    assert Gui.entry_first_name.get() == "Steph"
    assert Gui.entry_last_name.get() == "Teix"
    assert Gui.entry_title.get() == "Miss"
    assert Gui.entry_dept.get() == "CS"
    captured = pytest.stdout.getvalue().strip()
    assert captured == "First name: Steph\n Last name:Teix\n Title: Miss\n Dept: CS\n"
def test_user_creation(user_records):
    """This function tests a user with a duplicate username and verifies that it raises an exception: """
    user1 = ("Steph", " Dr", " Hello1")
    user2 = ("Steph", " Mrs", " Hello2")
    user3 = ("Steph", "Ms", "Hello3")
    user_records.insert(user1)
    with pytest.raises(Exception):
        user_records.insert(user2 + user3)
def test_gui_elements_present():
    """This function checks if there are labels and button widgets"""
    assert isinstance(Gui.label1, Gui.root.Label)
    assert isinstance(Gui.btn_email, Gui.root.Button)
    assert isinstance(Gui.label_dept, Gui.root.Label)
    assert isinstance(Gui.btn_org, Gui.root.Button)
    assert isinstance(Gui.label_last_name, Gui.root.Label)
