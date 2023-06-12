from lib.gratitudes import *

def test_returns_formatted_string():
    gratitudes = Gratitudes()
    gratitudes.add("sun")
    result = gratitudes.format()
    assert result == "Be grateful for: sun"

def test_returns_two_gratitudes():
    gratitudes = Gratitudes()
    gratitudes.add("sun")
    gratitudes.add("fan")
    result = gratitudes.format()
    assert result == "Be grateful for: sun, fan"

def test_init_empty_list():
    gratitudes = Gratitudes()
    assert gratitudes.gratitudes == []