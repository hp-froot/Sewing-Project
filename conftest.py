import pytest
from Shirts import *

# fixtures provide a defined, reliable and consistent context for tests


@pytest.fixture
def shirt_measurement_fixture():
    Hannah = Shirt_measurements(117, 20, 112, 32, 110, 15, 2, 44)
    return Hannah
