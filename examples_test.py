import code_test
import pytest


@pytest.fixture
def fixture_example():
    print(" voor test")
    yield
    # Teardown code goes here
    print(" na test")


@pytest.mark.fast
def test_example(fixture_example):
    # Test code goes here
    assert True == True


@pytest.mark.fast
def test_add():
    result = code_test.add(3, 4)
    assert result == 7


def test_add_fractions():
    result = code_test.add(1, 0.1)
    result = result + 0.1
    result = result + 0.1
    assert pytest.approx(result, abs=1e-9) == 1.3


@pytest.mark.parametrize("x, y", [(1, 2), (2, 3), (3, 4), (10, 4)])
def test_div(x, y):
    result = code_test.div(x, y)
    assert result == x / y


def test_div_err():
    with pytest.raises(ZeroDivisionError):
        code_test.div(2, 0)


@pytest.mark.fast
def test_err():
    with pytest.raises(ValueError, match=r'must be \d+$'):
        code_test.err()


def test_silly():
    assert True
