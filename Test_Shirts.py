#!/usr/bin/python3
from Shirts import *
import pytest

simple_shirt_instance = Simple_Shirt()


def simple_shirt_test():
    assert simple_shirt_instance.simple_shirt() == (53, 59, 39.5)
