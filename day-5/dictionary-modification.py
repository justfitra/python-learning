person = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "hobbies": ["reading", "traveling", "swimming"]
}

# update dictionary value
person.update({"hobbies": ["racing", "gaming", "cooking"]})
# add new key-value pairs to the dictionary
person.update({"job": "Engineer", "married": True})

if person["married"]:
    print("This person is married.")
else:
    print("This person is not married.")

if "hobbies" in person:
    print(f'this person exists')
else:
    print(f'this person does not exist')
print(person)
