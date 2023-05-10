import ctypes

lib = ctypes.CDLL('./libHello.so')

lib.greet.argtypes = [ctypes.c_char_p]

name = "Khaled".encode('utf-8')

lib.greet(name)
