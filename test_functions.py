import pytest
import sqlite3
#import pretendProductionCode
#cant import pretendproductioncode
import main


def test_show_output():
    with open("test.txt", "w") as test:
        testable_show_output(1000, .1, test)
    test_file = open("test.txt")
    everything = test_file.readlines()
    str_everything = str(everything)
    assert ' ' in str_everything

#
# def test_interest():
#     with pytest.raises(TypeError):
#         pretendProductionCode.add_interest('too much money', 1)


def test_questions_about_data():
    """Attempted to test on my own data that i put in my database"""
    with pytest.raises(AssertionError) as exception_info:
        assert main.make_initial_entries(45) is False
        assert main.make_initial_entries('Stephanie' is True
        assert main.make_initial_entries('No') is True
        assert main.make_initial_entries('Mac') is True
    assert exception_info is AssertionError
