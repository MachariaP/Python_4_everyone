# The meaning of the argument is dictated by its name, not its position

def introduction(first_name, last_name):
    print(f"Hello, my name is {first_name} {last_name}")

# Example usage
introduction(first_name="Skywalker", last_name="Luke")  # Hello, my name is Skywalker Luke
introduction(last_name="Quick", first_name="Jesse")  # Hello, my name is Quick Jesse
introduction(last_name="Kent", first_name="Clark")  # Hello, my name is Kent Clark