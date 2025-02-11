T = int(input("Input number of inputs: "))

names = []

for i in range(0,T):
    name_array = []
    name_string = input("Please input the name: ")
    split_name = name_string.split()
    names.append(split_name)

for full_name in names:
    first_name = full_name[0]
    last_name = full_name[1]

    first_name_character_array = []
    last_name_character_array = []

    for char in first_name:
        if char not in first_name_character_array:
            first_name_character_array.append(char)
    
    for char in last_name:
        if char not in last_name_character_array:
            last_name_character_array.append(char)

    if len(first_name_character_array) > len(last_name_character_array):
        print(last_name)
    elif len(first_name_character_array) < len(last_name_character_array):
        print(first_name)
    else:
        print("EQUALLY COMMON")
