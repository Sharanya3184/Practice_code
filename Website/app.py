import verification as verify
import Bussiness as bus

def user_profile():

    user_profile_info = bus.profile_info()

    return user_profile_info

def account_verification(name, password):
    account_exist = verify.login_verification(name, password)

    if account_exist:

        user_profile_infos = user_profile()

        return user_profile_infos

    else:

        print("Account does not exist")


def main():

    print("Welcome to the user profile system")

    print("Please fill in the following details:")

    username = input("Enter your name: ")

    password = input("Enter your password: ")

    user_data = account_verification(username, password)

    if user_data is None:
        print("Account does not exist")
    else:
        print(f'{username}, you have successfully logged in with the password')
        print("Your profile details are:")
        print(user_data)


if __name__ == "__main__":
    main()

