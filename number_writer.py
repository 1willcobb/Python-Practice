import json

def get_stored_name():
    """Gather the User Name from JSON file"""
    filename = 'username3.json'
    try: 
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username
    
def prompt_new_name():
    filename = 'username3.json'
    username = input("What is your name? > ")
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username
        

def greet_user():
    """greet user by name"""
    username = get_stored_name()
    if username:
        print(f"Welcome back {username}!")
    else:
        prompt_new_name()
        print(f"We'll remember you when you come back, {username}!")

def greet_2():
    print("hey")

greet_user()