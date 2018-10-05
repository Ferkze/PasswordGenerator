import random, string

def generatePassword(length):
    password = str()
    chars = "abcdefghijklmnopqrstuvwxyz"+"0123456789"
    for i in range(length):
        password = password + random.choice(chars)
    return password

my_password = generatePassword(50)
print(my_password)

#how many letters are there in the password?

password_complex = {}
for chr in my_password:
    if chr in string.ascii_letters:
        if chr in password_complex:
            password_complex[chr] += 1
        else:
            password_complex[chr] = 1

print(password_complex)
