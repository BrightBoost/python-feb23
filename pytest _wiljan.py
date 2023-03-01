import pytest
from calc_wiljan import *


@pytest.mark.parametrize("x, y, expected",
                         [(1, 2, 3),
                          (2, 4, 6),
                          (3, 4, 7)])
def test_add(x, y, expected):
    result = add(x, y)
    assert result == expected
