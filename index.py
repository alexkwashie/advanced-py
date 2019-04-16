#################-Working with Random()################
'''
import random


def ask_number():
    u_input = int(input("Guess the number"))
    if u_input in magic_numbers:
        print("You are in!")
    else:
        return "You are out"



magic_numbers= [3,8]

chances = 4

num_of = int(input("Enter number of times prog should run: "))

def loop_num(i):
    for ie in range(i):
        print("This is you  number {}".format(ie))
        ask_number()

loop_num(num_of);

print("This is then End")
'''




# min = 100

# for i in range(10):
#     ran = random.randint(0,100)
#     print(ran)
#     if ran <= min:
#         min = ran

# print(min)



#################-Split()################
'''
num =[]
pop = 0
pll = 5
for i in range(int(pll)):
    num1 = input("Enter number")
    num.append(num1)
    pop=pop+1

print(num)




#OR#



num1 = input("Enter numbers, seperate by a comma: ")

print(num1.split(","))

print(num1)
'''


#################-Python Set()################
number = [3,2,2,4,2,13]

number = set()

number.add(2)
number.add(1)
number.add(2)

print(number) #{1,2}


number1 = {3,4,4,1,3,4}
number2 = {8,4,6,3,2,5}
number3 = {12,2,6,4,2,5}
#intersecting 2 sets
neww = number1.intersection(number2)
print(neww.intersection(number3))


#egxamples

winning_num = [4,8,3,2,5]

#User can pick 6 numbers
def get_user_number():
        user_num = input("Please enter six number: ")

        numlist = user_num.split(",")

        num_set = {int(numb) for numb in numlist}

        return (num_set)

print(get_user_number())



#Lottery calculates 6 numbers (between 1 and 20)
import random

listz = set()  #Note: Cannot initalise like so: {}
def create_lottery_numbers():
        for num in range(6):
                listz.add(random.randint(1,20))
        return listz



#create_lottery_numbers()

#Then we match the user numbers to the lottery
#Calculate the winnings based on how many numbers user matched

