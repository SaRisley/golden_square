from lib.greet import *

def test_greet_returns_hello_name():
    result = greet("Sarah")
    assert result == "Hello, Sarah!"
