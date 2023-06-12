from lib.counter import *

def test_counter_returns_10():
    counter = Counter()
    counter.add(10)
    result = counter.report()
    assert result == "Counted to 10 so far."

def test_counter_returns_0():
    counter = Counter()
    result = counter.report()
    assert result == "Counted to 0 so far."