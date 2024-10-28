import pytest
from CallingFunctions.call_octal import to_decimal, to_hex, to_binary

@pytest.mark.parametrize("a, res", [('27', '23'), ('354', '236'), ('2356474', '646460')])
def test_oct_dec(a, res):
    assert to_decimal(a) == res
    
@pytest.mark.parametrize("a, res", [('256', 'ae'), ('3476', '73e'), ('156', '6e')])
def test_oct_hex(a, res):
    assert to_hex(a) == res
    
@pytest.mark.parametrize("a, res", [('27', '10111'), ('3567', '11101110111'), ('1267', '1010110111')])
def test_oct_bin(a, res):
    assert to_binary(a) == res