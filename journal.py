import os
from datetime import datetime


def create_entry():
    date = datetime.now().strftime("%Y-%m-%d")
    filename = f"{date}.txt"
    
    print(f"\nCreating Journal Entry for {date}")
    entry = input("Write your journal entry:\n")
    
    with open(filename, "a") as file:
        file.write(entry + "\n")
    
    print(f" Entry saved in {filename}")


def view_entry():
    date = input("Enter the date to view entry (YYYY-MM-DD): ")
    filename = f"{date}.txt"
    
    if os.path.exists(filename):
        print(f"\n Journal Entry for {date}:")
        with open(filename, "r") as file:
            print(file.read())
    else:
        print(" No entry found for that date.")


def delete_entry():
    date = input("Enter the date to delete entry (YYYY-MM-DD): ")
    filename = f"{date}.txt"
    
    if os.path.exists(filename):
        os.remove(filename)
        print(f" Entry for {date} deleted.")
    else:
        print(" No entry found for that date.")


def main():
    while True:
        print("\n--- Daily Journal Entry store ---")
        print("1. Create Entry")
        print("2. View Entry")
        print("3. Delete Entry")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == '1':
            create_entry()
        elif choice == '2':
            view_entry()
        elif choice == '3':
            delete_entry()
        elif choice == '4':
            print(" Exiting... Have a great day!")
            break
        else:
            print(" Invalid choice. Please enter 1-4.")

if __name__ == "__main__":
    main()
