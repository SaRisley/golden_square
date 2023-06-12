from lib.string_builder import *

def test_string_builder_returns_helloworld():
    string_builder = StringBuilder()
    string_builder.add("Hello, world")
    result = string_builder.output()
    assert result == "Hello, world"

def test_length_of_string():
    string_builder = StringBuilder()
    string_builder.add("testing")
    result = string_builder.size()
    assert result == 7

def test_initial_string():
    string_builder = StringBuilder()
    result = string_builder.output()
    assert result == ""