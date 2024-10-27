import ctypes

def to_binary(transformation):
    lib = ctypes.CDLL(r"C++\translationLibrary.dll")
    
    lib.octalToBinary.argtypes = [ctypes.c_char_p]
    lib.octalToBinary.restype = ctypes.c_char_p
    
    result = lib.octalToBinary(transformation.encode('utf-8'))
    
    return result.decode('utf-8')