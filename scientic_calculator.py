import math

while True:
    print("\n--- Scientific Calculator ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Square Root")
    print("6. Power")
    print("7. Sine")
    print("8. Cosine")
    print("9. Tangent")
    print("10. Logarithm (base 10)")
    print("11. Exit")

    choice = input("Enter your choice (1-11): ")

    if choice == "11":
        print("Calculator closed.")
        break

    if choice in ["1", "2", "3", "4", "6"]:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == "1":
            print("Result:", num1 + num2)

        elif choice == "2":
            print("Result:", num1 - num2)

        elif choice == "3":
            print("Result:", num1 * num2)

        elif choice == "4":
            if num2 != 0:
                print("Result:", num1 / num2)
            else:
                print("Error! Division by zero.")

        elif choice == "6":
            print("Result:", math.pow(num1, num2))

    elif choice in ["5", "7", "8", "9", "10"]:
        num = float(input("Enter a number: "))

        if choice == "5":
            if num >= 0:
                print("Result:", math.sqrt(num))
            else:
                print("Error! Negative number.")

        elif choice == "7":
            print("Result:", math.sin(math.radians(num)))

        elif choice == "8":
            print("Result:", math.cos(math.radians(num)))

        elif choice == "9":
            print("Result:", math.tan(math.radians(num)))

        elif choice == "10":
            if num > 0:
                print("Result:", math.log10(num))
            else:
                print("Error! Logarithm only for positive numbers.")

    else:
        print("Invalid choice! Try again.")