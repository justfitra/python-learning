dictionary = {
    "search": "for look to find something",
    "dictionary": "a book that lists the words of a language in alphabetical order and gives their meaning",
    "python": "a large heavy-bodied nonvenomous constrictor snake occurring throughout the Old World tropics",
    "programming": "the process of writing computer programs",
}

word = input("Enter a word to search in the dictionary: ").lower()

if word in dictionary:
    print(f'The meaning of "{word}" is: {dictionary[word]}')
else:
    print(f'The word "{word}" is not in the dictionary.')
