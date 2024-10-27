def to_binary(octal : str):
    temp = int(octal, 8)
    result = bin(temp)[2:]
    
    return str(result)
