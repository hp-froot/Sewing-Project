import pytest
from Shirts import *

# fixtures provide a defined, reliable and consistent context for tests


@pytest.fixture
def mannequin_size():
    size_forty = Shirt_measurements(90, 41, 12, 27, 96, 61, 40, 2)
    return size_forty


@pytest.fixture
def simp_shirt(mannequin_size):
    instance = Simple_Shirt(mannequin_size)
    return instance
