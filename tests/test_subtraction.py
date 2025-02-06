"""
Unit tests for the subtract function in the subtract module.
"""

from app.subtract import subtract


def test_subtract():
    """
    Test the subtract function with valid inputs.
    Ensure the result is correct for subtraction operations.
    """
    assert subtract(5, 3) == 2
    assert subtract(-1, -1) == 0
    assert subtract(0, 10) == -10
    assert subtract(100, 0) == 100
