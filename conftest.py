import pytest
from Shirts import *

# fixtures provide a defined, reliable and consistent context for tests


@pytest.fixture
def mannequin_size():
    size_forty = Shirt_measurements(90, 41, 12, 27, 96, 61, 2, 40)
    return size_forty
