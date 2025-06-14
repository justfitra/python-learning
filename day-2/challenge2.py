name_list = ["alya", "dimas", "rani", "eko"]
name_input = input("Enter your name: ")
for name in name_list:
    if name == name_input :
        print("username is valid")
        break
    if name != name_input :
        print("username is invalid")
        break
    else: 
        print("username is not found")
        break
