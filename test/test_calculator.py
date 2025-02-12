'''Tests for CalcEngine functionality'''
from decimal import Decimal
from calculator import CalcEngine

def test_sum_values():
    assert CalcEngine.sum_values(Decimal('2'), Decimal('2')) == Decimal('4')

def test_difference():
    assert CalcEngine.difference(Decimal('2'), Decimal('2')) == Decimal('0')

def test_quotient():
    assert CalcEngine.quotient(Decimal('2'), Decimal('2')) == Decimal('1')

def test_product():
    assert CalcEngine.product(Decimal('2'), Decimal('2')) == Decimal('4')
