import ctypes

def to_binary(transformation):
    lib = ctypes.CDLL(r"C++\translationLibrary.dll")
    
    lib.hexadecimalToBinary.argtypes = [ctypes.c_char_p]
    lib.hexadecimalToBinary.restype = ctypes.c_char_p
    
    result = lib.hexadecimalToBinary(transformation.encode('utf-8'))
    
    return result.decode('utf-8')

def to_octal(transformation):
    lib = ctypes.CDLL(r"C++\translationLibrary.dll")
    
    lib.hexadecimalToOctal.argtypes = [ctypes.c_char_p]
    lib.hexadecimalToOctal.restype = ctypes.c_char_p
    
    result = lib.hexadecimalToOctal(transformation.encode('utf-8'))
    
    return result.decode('utf-8')

def to_decimal(transformation):
    lib = ctypes.CDLL(r"C++\translationLibrary.dll")
    
    lib.hexadecimalToDecimal.argtypes = [ctypes.c_char_p]
    lib.hexadecimalToDecimal.restype = ctypes.c_char_p
    
    result = lib.hexadecimalToDecimal(transformation.encode('utf-8'))
    
    return result.decode('utf-8')