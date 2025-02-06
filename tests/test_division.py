"""
Unit tests for the divide function in the divide module.
"""

import pytest
from app.divide import divide


def test_divide():
    """
    Test the divide function with valid inputs.
    Ensure it returns the correct result for division.
    """
    assert divide(6, 3) == 2
    assert divide(-10, -2) == 5
    assert divide(0, 5) == 0


def test_divide_zero_exception():
    """
    Test that divide raises a ZeroDivisionError when dividing by zero.
    """
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)
