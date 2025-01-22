#!/usr/bin/python3
import sys
from calculator_1 import *
if __name__ == "__main__":
    sepa = ['+', '-', '*', '/']
    if len(sys.argv) == 4:
        a = int(sys.argv[1])
        sep = sys.argv[2]
        b = int(sys.argv[3])
        if sep not in sepa:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
        if sep == '+':
            print(f"{a} + {(b)} = {(add(a, b))}")
        elif sep == '-':
            print(f"{(a)} - {(b)} = {sub(a, b)}")
        elif sep == '*':
            print(f"{(a)} * {(b)} = {mul(a, b)}")
        elif sep == '/':
            print(f"{(a)} / {(b)} = {div(a, b)}")
    else:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
