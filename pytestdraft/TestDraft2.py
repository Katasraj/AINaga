import pytest


def test_total_divisable_by_6(input_total):
    assert input_total % 6 == 0

def test_total_divisable_by_15(input_total):
    assert input_total % 15 == 0
