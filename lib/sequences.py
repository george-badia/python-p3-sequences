#!/usr/bin/env python3

def print_fibonacci(length):
    if length == 0:
        print("[]")
    elif length == 1:
        print("[0]")
    else:
        a, b = 0, 1
        fib_sequence = [a, b]
        for _ in range(2, length):
            a, b = b, a + b
            fib_sequence.append(b)
        print(f"{fib_sequence}")