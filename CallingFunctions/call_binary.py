import ctypes

def to_octal(transformation):
    lib = ctypes.CDLL(r"C++\translationLibrary.dll")
    
    lib.binaryToOctal.argtypes = [ctypes.c_char_p]
    lib.binaryToOctal.restype = ctypes.c_char_p
    
    result = lib.binaryToOctal(transformation.encode('utf-8'))
    
    return result.decode('utf-8')

def to_decimal(transformation):
    lib = ctypes.CDLL(r"C++\translationLibrary.dll")
    
    lib.binaryToDecimal.argtypes = [ctypes.c_char_p]
    lib.binaryToDecimal.restype = ctypes.c_char_p
    
    result = lib.binaryToDecimal(transformation.encode('utf-8'))
    
    return result.decode('utf-8')

def to_hex(transformation):
    lib = ctypes.CDLL(r"C++\translationLibrary.dll")
    
    lib.binaryToHexadecimal.argtypes = [ctypes.c_char_p]
    lib.binaryToHexadecimal.restype = ctypes.c_char_p
    
    result = lib.binaryToHexadecimal(transformation.encode('utf-8'))
    
    return result.decode('utf-8')