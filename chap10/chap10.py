import json

store_user_data = 'chap10/txt_files/programing_pole.txt'

user_data = {}
user_data_json = f"{user_data}"

with open(store_user_data, 'a') as data:
    required_user_data = 0
    y = jason.loads(user_data_json)
    print(f"welcome back {y['name']}")
    while required_user_data < 3:
        name = input("*required* User Full Name > ").title().strip()
        user_data["name"] = name
        data.write(f"User: {name}\n")
        required_user_data += 1
        age = int(input("*required* User Age > "))
        data.write(f"Age: {str(age)}\n")
        required_user_data += 1
        email = input("*required* User email > ").lower().strip()
        data.write(f"Email: {email}")
        required_user_data += 1
        data.write("\n\n")



print(user_data)
print("finished capturing peoples information")
