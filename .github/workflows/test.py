"""PytestCheck."""

# test_show.py
import pytest


def test_sample1():
    """Test1."""
    assert True


def test_sample2():
    """Test2."""
    assert [1, 2, 3] != [3, 2, 1]


@pytest.mark.xfail()
def test_sample3():
    """Test3."""
    assert False


@pytest.mark.xfail()
def test_sample4():
    """Test4."""
    assert True
