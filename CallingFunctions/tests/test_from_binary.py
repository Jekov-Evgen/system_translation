import pytest
from CallingFunctions.call_binary import to_decimal, to_hex, to_octal

@pytest.mark.parametrize("a, res", [('1010', '10'), ('10110', '22'), ('11111', '31')])
def test_bin_dec(a, res):
    assert to_decimal(a) == res
    
@pytest.mark.parametrize("a, res", [('1010', 'a'), ('100001111', '10f'), ('1011001', '59')])
def test_bin_hex(a, res):
    assert to_hex(a) == res
    
@pytest.mark.parametrize("a, res", [('11100111', '347'), ('1000000111011', '10073'), ('1011', '13')])
def test_bin_oct(a, res):
    assert to_octal(a) == res