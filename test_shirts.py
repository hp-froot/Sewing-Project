from Shirts import *
import pytest
from conftest import *


def test_simple_shirt(simp_shirt: Simple_Shirt):
    assert simp_shirt.simple_shirt() == (
        53,
        59,
        39.5,
    )
