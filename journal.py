import os
from datetime import datetime

while True:
    print("\n--- Daily Journal Entry Store ---")
    print("1. Create Entry")
    print("2. View Entry")
    print("3. Delete Entry")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == '1':
        # Create Entry
        date = datetime.now().strftime("%Y-%m-%d")
        filename = f"{date}.txt"

        print(f"\nCreating Journal Entry for {date}")
        entry = input("Write your journal entry:\n")

        with open(filename, "w") as file:
            file.write(entry + "\n")

        print(f"Entry saved in {filename}")

    elif choice == '2':
        # View Entry
        date = input("Enter the date to view entry (YYYY-MM-DD): ")
        filename = f"{date}.txt"

        if os.path.exists(filename):
            print(f"\n Journal Entry for {date}:")
            with open(filename, "r") as file:
                print(file.read())
        else:
            print(" No entry found for that date.")

    elif choice == '3':
        # Delete Entry
        date = input("Enter the date to delete entry (YYYY-MM-DD): ")
        filename = f"{date}.txt"

        if os.path.exists(filename):
            os.remove(filename)
            print(f" Entry for {date} deleted.")
        else:
            print(" No entry found for that date.")

    elif choice == '4':
        print(" Exiting... Have a great day!")
        break


    else:
        print(" Invalid choice. Please enter 1-4.")
