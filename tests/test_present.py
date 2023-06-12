import pytest
from lib.present import *

def test_present_contents():
    present = Present()
    result = present.contents
    assert result == None

def test_wrap():
    present = Present()
    present.wrap(3)
    with pytest.raises(Exception) as e:
        present.wrap(33)
    error_message = str(e.value)
    assert error_message == "A contents has already been wrapped."

def test_unwrap():
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
    error_message = str(e.value)
    assert error_message == "No contents have been wrapped."