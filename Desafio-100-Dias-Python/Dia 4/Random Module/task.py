import random
# import my_module

# random_integer=random.randint(1,3)
# print(random_integer)

# my_number = my_module.my_favourite_number
# print(my_number)


for x in range(10):
    variable = random.randint(0,1)
    if variable == 0:
        print("Heads")
    else:
        print("Tails")