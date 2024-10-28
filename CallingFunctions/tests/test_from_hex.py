import pytest
from CallingFunctions.call_hex import to_decimal, to_octal, to_binary

@pytest.mark.parametrize("a, res", [('11ac', '4524'), ('1459cc', '1333708'), ('2439ccaf', '607767727')])
def test_hex_dec(a, res):
    assert to_decimal(a) == res
    
@pytest.mark.parametrize("a, res", [('1a', '32'), ('a', '12'), ('123ab', '221653')])
def test_hex_oct(a, res):
    assert to_octal(a) == res
    
@pytest.mark.parametrize("a, res", [('34a', '1101001010'), ('198a', '1100110001010'), ('123456ab', '10010001101000101011010101011')])
def test_hex_bin(a, res):
    assert to_binary(a) == res