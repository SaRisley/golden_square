import pytest
from lib.password_checker import *

def test_password_is_valid():
    checker = PasswordChecker()
    result = checker.check("password!")
    assert result == True

def test_password_is_not_valid():
    checker = PasswordChecker()
    with pytest.raises(Exception) as e:
        checker.check("hello")
    error_message = str(e.value)
    assert error_message == "Invalid password, must be 8+ characters."

def test_8_is_valid():
    checker = PasswordChecker()
    result = checker.check("password")
    assert result == True