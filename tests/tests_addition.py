"""
Unit tests for the add function in the add module.
"""

from app.add import add


def test_add():
    """
    Test the add function with valid inputs.
    Ensure the result is correct for addition operations.
    """
    assert add(1, 2) == 3
    assert add(-1, -1) == -2
    assert add(0, 0) == 0
    assert add(100, 200) == 300
