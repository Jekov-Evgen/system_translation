import ctypes

def to_binary(transformation):
    lib = ctypes.CDLL(r"C++\translationLibrary.dll")
    
    lib.fromDecimalToBinary.argtypes = [ctypes.c_char_p]
    lib.fromDecimalToBinary.restype = ctypes.c_char_p
    
    result = lib.fromDecimalToBinary(transformation.encode('utf-8'))
    
    return result.decode('utf-8')

def to_octal(transformation):
    lib = ctypes.CDLL(r"C++\translationLibrary.dll")
    
    lib.fromDecimalToOctal.argtypes = [ctypes.c_char_p]
    lib.fromDecimalToOctal.restype = ctypes.c_char_p
    
    result = lib.fromDecimalToOctal(transformation.encode('utf-8'))
    
    return result.decode('utf-8')

def to_hex(transformation):
    lib = ctypes.CDLL(r"C++\translationLibrary.dll")
    
    lib.decimalToHexadecimal.argtypes = [ctypes.c_char_p]
    lib.decimalToHexadecimal.restype = ctypes.c_char_p
    
    result = lib.decimalToHexadecimal(transformation.encode('utf-8'))
    
    return result.decode('utf-8')