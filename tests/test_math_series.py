from math_series import __version__
from math_series.series import fibonacci

def test_version():
    assert __version__ == "0.1.0"

def test_fibonacci():
    actual = fibonacci(5)
    expected = [0, 1, 1, 2, 3, 5]
    assert actual == expected

## Second test for fibonacci
def test_fibonacci_2():
# assign
    actual = fibonacci(13)
# arrange
    expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233]
# assert
    assert actual == expected


