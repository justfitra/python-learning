person = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "hobbies": ["reading", "traveling", "swimming"],
    "job": "Engineer",
    "married": True
}
person2 = person.copy()
person2 = person
person2 = dict(person)  # create a new dictionary from person
person["name"] = "Jane"  # update the name

print(person)
print(person2)  # print the type of person2, which is a string
