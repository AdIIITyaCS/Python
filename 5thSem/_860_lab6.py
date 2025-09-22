class SumGreaterThanTenException(Exception):
    pass

try:
    try:
        # Try block 1
        num = int(input("Enter a number a=: "))
        if num < 0:
            raise ValueError("Number cannot be negative")       
    except ValueError as e:
        print(f"Invalid input: {e}")

    try:
        # Try block 2
        value = int(input("Enter another number b=: "))
        if value == 0:
            raise ValueError("Don't put zero here")
    except ValueError as e:
        print(f"Invalid input: {e}")

    try:
        # Adding two numbers with a condition
        result = num + value
        if result > 10:
            raise SumGreaterThanTenException(f"Sum of {num} and {value} is greater than 10")
    except SumGreaterThanTenException as e:
        print(f"SumGreaterThanTenException occurred: {e}")

except Exception as e:
    print(f"An unexpected error occurred: {e}")
