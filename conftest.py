import pytest
from Shirts import *

# fixtures provide a defined, reliable and consistent context for tests


@pytest.fixture
def shirt_measurement_fixture():
    size_forty = Shirt_measurements(90, 41, 12, 27, 96, 61, 2, 40)
    return size_forty
