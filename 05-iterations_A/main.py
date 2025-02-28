#!/usr/bin/env python3

# Breaking Out of a Loop
"""
- Break statement ends the current loop and jumps
    to the statement immediately following the loop.
"""
def get_user_input():
    """
    Continuously prompts user for input until 'done' is entered.
    Print each line of input expect 'done'.
    """
    print("Enter text (type 'done' to exit):")

    while True:
        try:
            user_input = input ('> ').strip()
            if user_input.lower() == 'done':
                break
            print(user_input)
        except KeyboardInterrupt:
            print("\nProgram terminated by user.")
            break
        except EOFError:
            print("\nEnd of input reached.")
            break

if __name__ == "__main__":
    get_user_input()
    print('Done!')
