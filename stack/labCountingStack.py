#!/usr/bin/env python3

class Stack:
    """
    A basic stack implementation with push and pop operations.

    Attributes:
        __stk (list): Private list to store stack elements.
    """
    def __init__(self):
        """Initialize an empty stack."""
        self.__stk = []

    def push(self, val):
        """
        Add a value to the top of the stack.

        Args:
            val: The value to be pushed onto the stack.
        """
        self.__stk.append(val)

    def pop(self):
        """
        Remove and return the top value from the stack.

        Returns:
            The value at the top of the stack.

        Raises:
            IndexError: If the stack is empty.
        """
        val = self.__stk[-1]
        del self.__stk[-1]
        return val

class CountingStack(Stack):
    """
    A stack that extends the basic Stack class and counts the number of pop operations.

    Attributes:
        __counter(int): Private counter for the number of pop operations.
    """
    def __init__(self):
        """Initialize an empty CountingStack and reset the pop counter."""
        Stack.__init__(self)
        self.__counter = 0

    def get_counter(self):
        """
        Get the number of pop operations performed.

        Returns:
            int: The total number of pop operations.
        """
        return self.__counter

    def pop(self):
        """
        Remove and return the top value from the stack, incrementing the top counter.

        Returns:
            The value at the top of the stack.

        Raises:
            IndexError: If the stack is empty.
        """
        self.__counter += 1
        return Stack.pop(self)


stk = CountingStack()
for i in range(100):
    stk.push(i)
    stk.pop()
print(stk.get_counter())
