"""
Factorial Calculator with Input and Calculation Functions
"""

def get_non_negative_integer() -> int:
    """
    Obtains a non-negative integer input from the user.
    Prompts the user until a valid non-negative integer is entered.
    Returns:
        int: A valid non-negative integer.
    """
    while True:
        try:
            n = int(input("Enter a non-negative integer: "))
            if n >= 0:
                return n
            else:
                print("Please enter a non-negative integer.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def calculate_factorial(n: int) -> int:
    """
    Calculates the factorial of a given non-negative integer.
    Args:
        n (int): A non-negative integer.
    Returns:
        int: The factorial of n.
    """
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

def main():
    """
    Main program flow:
    - Gets a non-negative integer from the user.
    - Calculates the factorial of the input number.
    - Displays the result.
    """
    number = get_non_negative_integer()
    result = calculate_factorial(number)
    print(f"The factorial of {number} is: {result}")

if __name__ == "__main__":
    main()