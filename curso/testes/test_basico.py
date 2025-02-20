from functions import is_positive, validate_email


def test_soma():
    assert sum([1, 4, 5]) == 10


def test_is_positive():
    assert is_positive(5) is True
    assert is_positive(-2) is False


def test_email():
    assert validate_email('fulano@email.com') is True
    assert validate_email('fulano.email.com') is False
