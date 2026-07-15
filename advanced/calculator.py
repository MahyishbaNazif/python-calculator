import math


# ---------------- FUNCTIONS ---------------- #

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b


def modulus(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a % b


def floor_division(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a // b


def power(a, b):
    return a ** b


def square_root(a):
    if a < 0:
        return "Square root of a negative number is not possible."
    return math.sqrt(a)


def factorial(a):
    if a < 0:
        return "Factorial of a negative number is not possible."
    return math.factorial(int(a))


def percentage(a, b):
    if b == 0:
        return "Percentage cannot be calculated."
    return (a / b) * 100


def maximum(a, b):
    return max(a, b)


def minimum(a, b):
    return min(a, b)


# ---------------- MAIN PROGRAM ---------------- #

while True:

    print("\n" + "=" * 50)
    print("         ADVANCED PYTHON CALCULATOR")
    print("=" * 50)

    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Floor Division")
    print("7. Power")
    print("8. Square Root")
    print("9. Factorial")
    print("10. Percentage")
    print("11. Maximum")
    print("12. Minimum")
    print("13. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "13":
        print("\nThank you for using Python Calculator.")
        break

    try:

        if choice == "8":
            num = float(input("Enter a number: "))
            print(f"\nResult = {square_root(num)}")

        elif choice == "9":
            num = float(input("Enter a number: "))
            print(f"\nResult = {factorial(num)}")

        else:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == "1":
                print(f"\nResult = {add(num1, num2)}")

            elif choice == "2":
                print(f"\nResult = {subtract(num1, num2)}")

            elif choice == "3":
                print(f"\nResult = {multiply(num1, num2)}")

            elif choice == "4":
                print(f"\nResult = {divide(num1, num2)}")

            elif choice == "5":
                print(f"\nResult = {modulus(num1, num2)}")

            elif choice == "6":
                print(f"\nResult = {floor_division(num1, num2)}")

            elif choice == "7":
                print(f"\nResult = {power(num1, num2)}")

            elif choice == "10":
                print(f"\nPercentage = {percentage(num1, num2)} %")

            elif choice == "11":
                print(f"\nMaximum = {maximum(num1, num2)}")

            elif choice == "12":
                print(f"\nMinimum = {minimum(num1, num2)}")

            else:
                print("\nInvalid Choice!")

    except ValueError:
        print("\nPlease enter valid numbers only.")

    except Exception as e:
        print(f"\nUnexpected Error: {e}")