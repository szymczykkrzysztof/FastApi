import pytest


def test_equal_or_not_equal():
    assert 3 == 3


def test_is_instance():
    assert isinstance('This is a string', str)
    assert not isinstance('10', int)
    assert isinstance(10, int)


def test_boolean():
    validate = True
    assert validate is True
    assert ('Hello' == 'world') is False


def test_type():
    assert type('Hello' is str)
    assert type(10) is int
    assert type('World') is not int


def test_greater_and_less_than():
    assert 7 > 3
    assert 4 < 10


def test_list():
    num_list = [1, 2, 3, 4, 5]
    any_list = [False, False, True, True, False]
    assert 1 in num_list
    assert 7 not in num_list
    assert None not in any_list


class Student:
    def __init__(self, first_name: str, last_name: str, major: str, years: int):
        self.first_name = first_name
        self.last_name = last_name
        self.major = major
        self.years = years


@pytest.fixture
def default_student():
    return Student('John', 'Doe', 'Computer Science', 3)


def test_person_initialization(default_student):
    assert default_student.first_name == 'John', 'First name should be John'
    assert default_student.last_name == 'Doe', 'Last name should be Doe'
    assert default_student.major == 'Computer Science', 'Major should be Computer Science'
    assert default_student.years == 3, 'Years should be 3'
