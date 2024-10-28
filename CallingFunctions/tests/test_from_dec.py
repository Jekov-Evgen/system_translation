import pytest
from CallingFunctions.call_decimal import to_binary, to_octal, to_hex

@pytest.mark.parametrize("a, res", [('35', '100011'), ('1811', '11100010011'), ('3007', '101110111111')])
def test_dec_bin(a, res):
    assert to_binary(a) == res
    
@pytest.mark.parametrize("a, res", [('20112007', '114561207'), ('18112005', '105057005'), ('567', '1067')])
def test_dec_oct(a, res):
    assert to_octal(a) == res
    
@pytest.mark.parametrize("a, res", [('10', 'a'), ('124', '7c'), ('30072007', '1cadcc7')])
def test_dec_hex(a, res):
    assert to_hex(a) == res