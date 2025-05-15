#!/usr/bin/env python3

# The stack - the procedural approach

stack = []

def push(val):
    stack.append(val)

def pop():
    val = stack[-1]
    del stack[-1]
    return val

push(8)
push(7)
push(6)
push(5)

print(pop())
print(pop())
print(pop())
