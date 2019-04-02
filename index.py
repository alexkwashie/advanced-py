import random


def ask_number():
    u_input = int(input("Guess the number"))
    if u_input in magic_numbers:
        print("You are in!")
    else:
        print("You are out")



magic_numbers= [3,8]

chances = 4

num_of = int(input("Enter number of times prog should run: "))

def loop_num(i):
    for ie in range(i):
        print("This is you  number {}".format(ie))
        ask_number()

loop_num(num_of);

print("This is then End")







# min = 100

# for i in range(10):
#     ran = random.randint(0,100)
#     print(ran)
#     if ran <= min:
#         min = ran

# print(min)


