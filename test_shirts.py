from Shirts import *
import pytest
from conftest import *

simple_shirt_instance = Simple_Shirt(shirt_measurement_fixture)


def test_simple_shirt():
    assert simple_shirt_instance.simple_shirt() == (
        53,
        59,
        39.5,
    )
