import math


def menu():
    print("\n" + "=" * 60)
    print("            SCIENTIFIC CALCULATOR")
    print("=" * 60)
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Square Root")
    print("7. Cube Root")
    print("8. Factorial")
    print("9. Sine")
    print("10. Cosine")
    print("11. Tangent")
    print("12. Log Base 10")
    print("13. Natural Log (ln)")
    print("14. Exponential (e^x)")
    print("15. Absolute Value")
    print("16. Ceiling")
    print("17. Floor")
    print("18. Degrees → Radians")
    print("19. Radians → Degrees")
    print("20. Value of π")
    print("21. Value of e")
    print("22. Exit")
    print("=" * 60)


while True:

    menu()

    choice = input("Enter your choice: ")

    try:

        if choice == "22":
            print("\nThank you for using Scientific Calculator!")
            break

        elif choice == "20":
            print(f"\nπ = {math.pi}")

        elif choice == "21":
            print(f"\ne = {math.e}")

        elif choice in ["6", "7", "8", "9", "10", "11",
                        "12", "13", "14", "15",
                        "16", "17", "18", "19"]:

            num = float(input("Enter number: "))

            if choice == "6":
                if num < 0:
                    print("Cannot calculate square root.")
                else:
                    print("Result =", math.sqrt(num))

            elif choice == "7":
                print("Result =", num ** (1/3))

            elif choice == "8":
                if num < 0:
                    print("Factorial not possible.")
                else:
                    print("Result =", math.factorial(int(num)))

            elif choice == "9":
                print("Result =", math.sin(math.radians(num)))

            elif choice == "10":
                print("Result =", math.cos(math.radians(num)))

            elif choice == "11":
                print("Result =", math.tan(math.radians(num)))

            elif choice == "12":
                if num <= 0:
                    print("Log undefined.")
                else:
                    print("Result =", math.log10(num))

            elif choice == "13":
                if num <= 0:
                    print("Natural log undefined.")
                else:
                    print("Result =", math.log(num))

            elif choice == "14":
                print("Result =", math.exp(num))

            elif choice == "15":
                print("Result =", abs(num))

            elif choice == "16":
                print("Result =", math.ceil(num))

            elif choice == "17":
                print("Result =", math.floor(num))

            elif choice == "18":
                print("Result =", math.radians(num))

            elif choice == "19":
                print("Result =", math.degrees(num))

        else:

            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == "1":
                print("Result =", num1 + num2)

            elif choice == "2":
                print("Result =", num1 - num2)

            elif choice == "3":
                print("Result =", num1 * num2)

            elif choice == "4":
                if num2 == 0:
                    print("Division by zero not allowed.")
                else:
                    print("Result =", num1 / num2)

            elif choice == "5":
                print("Result =", num1 ** num2)

            else:
                print("Invalid Choice.")

    except ValueError:
        print("Please enter valid numeric values.")

    except Exception as e:
        print("Unexpected Error:", e)