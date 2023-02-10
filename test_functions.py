import pytest
import sqlite3

import main


def test_connect_to_db(capfd):
    """this function creates a fake database and makes sure it connects to it"""
    test_db = 'wufoo_db.db'
    sqlite3.connect(test_db)


def test_questions_about_data():
    """Attempted to test on my own data that I put in my database"""
    with pytest.raises(AssertionError) as exception_info:
        assert main.make_initial_entries(45) is False
        assert main.make_initial_entries('Stephanie') is True
        assert main.make_initial_entries('No') is False
        assert main.make_initial_entries('Mac') is False
        assert main.make_initial_entries('Booooo') is False
        assert main.make_initial_entries('Hiiii') is False
        assert main.make_initial_entries('Helloworld') is False
        assert main.make_initial_entries('') is True
    assert exception_info is AssertionError
