# Using the return keyword without an expression

def happy_new_year(wishes=True):
    print("Three...")
    print("Two...")
    print("One...")
    if not wishes:
        return
    
    print("Happy New Year!")

# Example usage
happy_new_year()  # Happy New Year!