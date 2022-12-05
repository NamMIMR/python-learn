# print('Get those dogs ready')


# def bark(name, weight):
#     if weight > 20:
#         print(name, 'says WOOF WOOF')
#     else:
#         print(name, 'says woof woof')


# bark('Codie', 40)
# bark('Sparky', 9)
# bark('Jackson', 12)
# bark('Fido', 65)

# print("OK, We're all done")

def get_bark(weight):
    if weight > 20:
        return 'WOOF WOOF'
    else:
        return 'woof woof'

codies_bark = get_bark(40)
print("Codie's bark is", codies_bark)