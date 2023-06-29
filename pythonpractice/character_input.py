import datetime
# Create a program that asks the user to enter their 
# name and their age. Print out a message addressed to 
# them that tells them the year that they will turn 100 years old.

name = input('what is your name...  ')
age = int(input('what is your age..  '))
date = datetime.datetime.now()
dob = date.year - age
dihd = dob + 100
print('your name is', name, 'and your age is', age, 'we are in', date.year,' you were born in', dob, 'and your tuning 100 years by', dihd )