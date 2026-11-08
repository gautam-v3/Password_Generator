import random
import string

# 1. Individual character categories
letters = list(string.ascii_letters)       # 'a'-'z' and 'A'-'Z' (52 chars)
digits = list(string.digits)               # '0'-'9' (10 chars)
symbols = list(string.punctuation)         # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ (32 chars)


no_letter=int(input("enter how many letters you want in the Password \n"))
no_digits=int(input("enter how many digits you want in the Password \n"))
no_symbols=int(input("enter how many symbols you want in the Password \n"))

password=[]
for char in range(0,no_letter):
    password.append(random.choice(letters))
for char in range(0,no_digits):
    password.append(random.choice(digits))
for char in range(0,no_symbols):
    password.append(random.choice(symbols))  

print(password)
random.shuffle(password)
final_password=''
for char in password:
    final_password+=char
print(f"your password is ={final_password}")
