
user_credentials = {
    'user_1': "password1"
}

def authenticate(username: str=None, password: str=None):
    if username in user_credentials and user_credentials[username] == password:
        return True
    else:
        return False

def main():
    username = input("enter your username")
    password = input("enter your password")

    if authenticate(username, password):
        print("Authentication SUCCESSFUL")
    else:
        print("Authentication FAIL")

if __name__ == "__main__":
    main()