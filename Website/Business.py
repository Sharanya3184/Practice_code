def profile_info():

    profile_infos = []


    print("Welcome Please fill in the following details:")
    username              = input("Enter your name: ")
    password              = (input("Enter your password: "))
    age                   = int(input("Enter your age: "))
    gender                = input("male/female/other: ")
    mail_id               = input("Enter your email: ")
    phone                 = input("Enter your phone number: ")
    address_verification  = input("Enter your address [yes or no]: ")

    if address_verification.lower() == "yes":
        address = input("Enter your address: ")
        profile_infos.append([username, password, age, gender, mail_id, phone, address])
    else:
        profile_infos.append([username, password, age, gender, mail_id, phone, "Address not provided"])

    print("Form submitted successfully!")
    return profile_infos