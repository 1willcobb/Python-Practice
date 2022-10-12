import json

def get_user_name():
    user_name_store = 'number_store4.json'
    try:
        with open(user_name_store) as f:
            user_name = json.load(f)
    except FileNotFoundError:
        return None
    except NameError:
        return None
    else:
        return user_name

def prompt_new_user():
    user_name_store = 'number_store4.json'
    print("It doesn't seem like you are a user?")
    new_user_name = input("What would you like your user name to be? > ")
    print(f"Sweet! We will rememver you {new_user_name} for next time.")
    with open(user_name_store, 'w') as file:
        json.dump(new_user_name, file)
    return new_user_name

def program_interface():
    username = input("please input user name > ")
    saved_user = get_user_name()
    if saved_user == username:
            print(f"Welcome back {saved_user}!")
    else:
        prompt_new_user()

        

program_interface()