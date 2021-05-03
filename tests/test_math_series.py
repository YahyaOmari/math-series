from math_series import __version__
from math_series.series import fibonacci
from math_series.series import lucas

def test_version():
    assert __version__ == "0.1.0"

def test_fibonacci():
    actual = fibonacci(5)
    expected = [0, 1, 1, 2, 3, 5]
    assert actual == expected

## Second test for fibonacci
def test_fibonacci_2():
    actual = fibonacci(13)
    expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233]
    assert actual == expected

# ---------------------Test for second function---------------------------


def test_lucas():
    actual = lucas(5)
    expected = [2, 1, 3, 4, 7, 11]
    assert actual == expected


def test_lucas_2():
    actual = lucas(8)
    expected = [2, 1, 3, 4, 7, 11, 18, 29, 47]
    assert actual == expected

