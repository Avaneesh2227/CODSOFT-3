import random
import string
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
password=[]
letters = string.ascii_letters

num_letters=input("How many letters do you want?: ")
num_numbers=input("How many numbers do you want?: ")
num_symbols=input("How many symbols do you want?: ")

for i in range(int(num_letters)):
    password.append(random.choice(letters))
for j in range(int(num_numbers)):
    password.append(str(random.randint(0,9)))
for k in range(int(num_symbols)):
    password.append(random.choice(symbols))
random.shuffle(password)
final_pw="".join(password)
print(f"Generated password is: {final_pw}")