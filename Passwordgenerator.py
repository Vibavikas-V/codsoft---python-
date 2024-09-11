import random 

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*_"

while True:
    password_length = int(input('Enter the length of password: '))
    password_count = int(input('How many passwords do you want: '))

    for i in range(password_count):
        password = ''
        for j in range(password_length):
            password += random.choice(characters)
        print('Here is your password:', password)
    
    repeat = input('Do you want to generate another password? (Y/N): ').lower()
    if repeat == 'n':
        break
