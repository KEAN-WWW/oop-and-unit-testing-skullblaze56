"""
Unit tests for the multiply function in the multiply module.
"""

from app.multiply import multiply


def test_multiply():
    """
    Test the multiply function with valid inputs.
    Ensure it returns the correct result for multiplication.
    """
    assert multiply(2, 3) == 6
    assert multiply(-1, -1) == 1
    assert multiply(0, 100) == 0
