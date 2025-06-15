person = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "hobbies": ["reading", "traveling", "swimming"],
    "job": "Engineer",
    "married": True
}
for key, value in person.items():
    # print the key and value of each item in the dictionary
    print(f'this key {key} : this value {value}')
# Loop through the dictionary keys
for key in person.keys():
    # print the value of each key
    print(f'this key {key} : this value {person[key]}')
# Loop through the dictionary values
for value in person.values():
    # print the value
    print(f'this value {value}')
for p in person:
    # print the value of each key in the dictionary
    print(f'this key {p} : this value {person[p]}')
