from flask import Flask

app = flask(__name__)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero."
    else:
        return a / b
    
def is_int_try(x):
    int(x)
