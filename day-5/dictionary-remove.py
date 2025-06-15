person = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "hobbies": ["reading", "traveling", "swimming"]
}

person.pop("age")  # remove the key "age" from the dictionary
person.popitem()  # remove the last inserted key-value pair
del person["city"]  # delete the key "city" from the dictionary
person.clear()  # clear all items from the dictionary
print(person)
