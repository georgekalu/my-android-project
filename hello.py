print("🚀 Welcome to Acode Python Terminal!")
print("====================================\n")

name = input("What is your name? ")

print(f"\nHello, {name}! 👋")
print("You're now coding on your Android phone like a pro.\n")

print("What would you like to do?")
print("1. Show current date and time")
print("2. Tell a fun fact")
print("3. Say goodbye")

choice = input("\nEnter your choice (1/2/3): ")

if choice == "1":
    import datetime
    now = datetime.datetime.now()
    print(f"\nCurrent date and time: {now.strftime('%Y-%m-%d %H:%M:%S')}")
elif choice == "2":
    print("\nFun fact: Did you know? The first computer bug was an actual moth stuck in a relay in 1947!")
elif choice == "3":
    print(f"\nGoodbye, {name}! Keep coding and have a great day! 💪")
else:
    print("\nInvalid choice. Next time pick 1, 2, or 3.")
