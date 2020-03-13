# http://www.practicepython.org/exercise/2014/01/29/01-character-input.html

name = input('Enter Name: ')
age = int(input('Enter Age: '))
copies = int(input('Copies: '))

diff = 100 - age

if age >= 100:
    print("You already reached 100!")

else:
    print(copies * f"{name} will turn 100 in {diff} years.\n")
