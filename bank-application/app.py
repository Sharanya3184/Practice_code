import buss

def user_detail(username, account_number, balance=0):
    user = []
    
    if balance:
        user.append([username, account_number, balance])
    else:
        user.append([username, account_number])

    return user

def main():
    username = input("Enter your name: ")
    account_number = input("Enter your account number: ")

    check = input("Do you want to check your balance [yes/no]: ")
    if check == "yes":
        balance = int(input("Enter your account balance: "))
        user = user_detail(username, account_number, balance)
    else:
        user = user_detail(username, account_number)
    print("user_details", user)

    withdraw = input("Do you want to withdraw any amount from your account [yes/no]: ")
    if withdraw == "yes":
        amount = int(input("Enter the amount to withdraw: "))
        balance = buss.withdraw(balance, amount)
        print(f"Amount {amount} withdrawn successfully.")
        print(f"Total Balance: {balance}")
    
    deposit = input("Do you want to deposit any amount [yes/no]: ")
    if deposit == "yes":
        print(f"Your total account balance: {balance}")
        amount = int(input("Enter the amount to deposit: "))
        balance = buss.deposit(balance, amount)
        print(f"{amount} rupees deposited successfully.")
        print(f"Total Balance: {balance}")

if __name__ == "__main__":
    main()m