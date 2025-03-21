#old_macdonald
#capitalize the first and fourth letter in a string

def old_macdonald(name):
    newname= ""
    for x, char in enumerate(name):
        if x == 0 or x == 3:
            newname += char.upper()
        else:
            newname += char
    print(newname)

def better_old_macdonald(name):
    first_half = name[:3]
    second_half = name[3:]
    print(first_half.capitalize() + second_half.capitalize())

better_old_macdonald("macdonald")