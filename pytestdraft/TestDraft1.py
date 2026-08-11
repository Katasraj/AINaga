import pytest


def test_total_divisable_by_5(input_total):
    assert input_total % 5 == 0

def test_total_divisable_by_10(input_total):
    assert input_total % 10 == 0

def test_total_divisable_by_9(input_total):
    assert input_total % 9 == 0