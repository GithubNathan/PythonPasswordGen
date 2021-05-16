import string
import random
import sys
import string

print("Welcome to the random password generator.")
amount = input("How many characters would you like your password to be?")
charamount = int(amount)
otherCharList = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
sys.stdout = open('test.txt', 'w')

i = 0
password = "Password: "

while i < charamount:
    password += random.choice(otherCharList)
    password += random.choice(string.ascii_letters)
    i += 1

print(password)
sys.stdout.close()



