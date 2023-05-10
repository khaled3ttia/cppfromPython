# Instructions

This example demonstrates one way of calling C++ functions from Python. The function takes a simple argument and returns nothing. It just prints to `stdout`

## Compile the C++ code as a shared library
A `Makefile` is already provided to do this. Make sure that `g++` is installed, and then simply run `make`. 


## Run the Python code that calls the C++ function using `ctypes`
If you look at `hello.py`, it uses `ctypes` and expects the shared library to be compiled. It first loads the shared lib, and prepares the argument with the correct type. Finally, it calls the function. 
Make sure that python is installed and then run `python hello.py`
