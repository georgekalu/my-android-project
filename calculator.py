import os

def clear():
    os.system('clear')

print("🧮 Enhanced Calculator")
print("=====================\n")

while True:
    print("\n" + "="*40)
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print("\nChoose operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Power (^)")
    print("6. Clear screen")
    print("7. Exit")

    choice = input("\nEnter your choice (1-7): ")

    if choice == "1":
        result = num1 + num2
        print(f"\n{num1} + {num2} = {result}")
    elif choice == "2":
        result = num1 - num2
        print(f"\n{num1} - {num2} = {result}")
    elif choice == "3":
        result = num1 * num2
        print(f"\n{num1} * {num2} = {result}")
    elif choice == "4":
        if num2 == 0:
            print("\nError: Cannot divide by zero!")
        else:
            result = num1 / num2
            print(f"\n{num1} / {num2} = {result}")
    elif choice == "5":
        result = num1 ** num2
        print(f"\n{num1} ^ {num2} = {result}")
    elif choice == "6":
        clear()
        continue
    elif choice == "7":
        print("\nGoodbye! Thanks for using the calculator 💪")
        break
    else:
        print("\nInvalid choice! Please enter 1-7.")

    input("\nPress Enter to continue...")
