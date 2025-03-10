def get_non_negative_integer() -> int:
    while True:
        try:
            num = int(input("Enter a non-negative integer: "))
            if num >= 0:
                return num
            print("Error: Please enter a non-negative integer.")  # No need for else
        except ValueError:
            print("Error: Invalid input. Please enter a valid integer.")

def calculate_factorial(n: int) -> int:
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

def main():
    number = get_non_negative_integer()
    result = calculate_factorial(number)
    print(f"The factorial of {number} is: {result}")

if __name__ == "__main__":
    main()