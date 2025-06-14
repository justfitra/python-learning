age_list = [5, 13, 19, 25, 65]

for age_list in age_list:
    if age_list < 12 :
        print(age_list, "is a child")
    elif age_list > 12 and age_list < 17:
        print(age_list, "is a teenager")
    elif age_list > 18 and age_list < 59:
        print(age_list, "is an adult")
    elif age_list >= 60:
        print(age_list, "is a senior citizen")
    else:
        print(age_list, "is an invalid age")