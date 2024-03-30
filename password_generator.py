import random

letters = ['A','B','c','D','E','F','G','H','I','J','K','L','M','N','M','O',
        'P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f',
        'g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','#','$','%','&','(',')','*','+']
print("welcome to py password generator")

n_letters = int(input("How many letters would you like in you password: "))
n_numbers = int(input("How many numbers would you like: "))
n_symbols = int(input("How many symbols would you like: "))

password = []
for i in range(n_letters):
    j = random.randint(0,len(letters) - 1)
    password.append(letters[j])

for i in range(n_numbers):
    j = random.randint(0,len(numbers) - 1)
    password.append(numbers[j])

for i in range(n_symbols):
    j = random.randint(0,len(symbols) - 1)
    password.append(symbols[j])

random.shuffle(password)

for i in range(len(password)):
    print(password[i],end='')