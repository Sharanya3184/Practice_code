user_dict = {
    'name': "sharan",
    'password': "sri"
}
def login_verification(
    username : str, 
    passward : str
):
    if user_dict and user_dict['name'] == username and user_dict['password'] ==passward:
        return True
    else:
        return false

