import random

print('Easy password generator')

symbols = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

password_len = int(input('password lenght: '))
password = ''

for i in range(password_len):
    password += random.choice(symbols)

print(f'Password: {password}')
