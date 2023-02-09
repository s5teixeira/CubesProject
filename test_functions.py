import pytest
import sqlite3
import pretendProductionCode


def test_show_output():
    with open("test.txt", "w") as test:
        pretendProductionCode.testable_show_output(1000, .1, test)
    test_file = open("test.txt")
    everything = test_file.readlines()
    str_everything = str(everything)
    assert ' ' in str_everything


def test_interest():
    with pytest.raises(TypeError):
        pretendProductionCode.add_interest('too much money', 1)
