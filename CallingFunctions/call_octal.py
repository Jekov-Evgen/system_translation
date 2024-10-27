import ctypes

def to_binary(transformation):
    lib = ctypes.CDLL(r"C++\translationLibrary.dll")
    
    lib.octalToBinary.argtypes = [ctypes.c_char_p]
    lib.octalToBinary.restype = ctypes.c_char_p
    
    result = lib.octalToBinary(transformation.encode('utf-8'))
    
    return result.decode('utf-8')

def to_decimal(transformation):
    lib = ctypes.CDLL(r"C++\translationLibrary.dll")
    
    lib.octalToDemical.argtypes = [ctypes.c_char_p]
    lib.octalToDemical.restype = ctypes.c_char_p
    result = lib.octalToDemical(transformation.encode('utf-8'))
    
    return result.decode('utf-8')

def to_hex(transformation):
    lib = ctypes.CDLL(r"C++\translationLibrary.dll")
    
    lib.octalToHexadecimal.argtypes = [ctypes.c_char_p]
    lib.octalToHexadecimal.restype = ctypes.c_char_p
    result = lib.octalToHexadecimal(transformation.encode('utf-8'))
    
    return result.decode('utf-8')