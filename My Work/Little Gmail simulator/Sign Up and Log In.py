import time
print('Time to create you gmail account')
time.sleep(0.5)
username = input('Enter your username')
time.sleep(0.5)
print('Great')
time.sleep(0.5)
print('We are moving to the gmail name!')
time.sleep(1)
print('Instructions:\nneed @gmail.com at the end\n gmail has to be at least 4 characters long')
gmail = input("Gmail's name:")
if gmail.endswith('@gmail.com') and len(gmail) >= 4:
    print('Ok great!')
else:
    print('Gmail is Invalid!')
    exit()
time.sleep(0.5)

print('next is to create a password')
print('Instructions:\nneeds to contain at least one number\nhas to contain this character:!\nfirst letter of the '
      'password must be uppercase')
password = input(f'Enter your password:')
contain_digit = False
for digit in password:
    if digit.isdigit():
        contain_digit = True
if password.find('!') != -1 and contain_digit and password[0].isupper() and len(password) >= 6:
    print('Great')
else:
    print('Password is Invalid')
    exit()
time.sleep(1)
user_info = {
    'username': username,
    'user_gmail': gmail,
    'user_password': password
}
print('Time to Log in into the gmail account you just created!')
user_gmail = input('Enter your gmail: ')
if user_info.get('user_gmail') == user_gmail:
    pass
else:
    print("Gmail doesn't exist in the data")
user_password = input('Enter your password: ')
if user_info.get('user_password') == user_password:
    pass
else:
    print("Password is wrong!")
    exit()
print(f"Welcome{user_info.get('username')} you are in!")
