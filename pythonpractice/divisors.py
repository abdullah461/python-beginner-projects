# Create a program that asks the user for a number and then
#  prints out a list of all the divisors of that number. (If 
# you don’t know what a divisor is, it is a number that divide
#  evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

numbers = range(1,100)
input = int(input('write a number between 1 to 100..'))
for number in numbers:
    if input % number==0:
        print(number)