from lib.report_length import *

def test_report_length_returns_12():
    result = report_length("Hello world!")
    assert result == "This string was 12 characters long."
