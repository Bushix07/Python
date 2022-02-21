#Q1
def power(num1, num2):
    power = num1 ** num2
    return f'power is: {power}'
num1 = 2
num2 = 5
print(power(num1, num2))

#Q2
def minus(num1, num2):
    minus = 0
    if num1 > num2:
        minus = num1 - num2
    else:
        minus = num2 - num1
    return f'minus of the big number and the small number is: {minus}'

print(minus(num1, num2))


#Q3
def str1(string) -> str:
    if string[0].isupper():
        return 'yes'
    else:
        return 'no'

string = 'Hello'
print(str1(string))

#Q4
def str2(string) -> str:
    if string.find('!') != -1:
        return 'The string has the character:! in it.'
    else:
        return "The string doesn't have the character:! in it"

string2 = 'hi!'
print(str2(string2))

#Q4 (Alternative way)
def str2alt(string) -> str:
    if '!' in string:
        return 'alt The string has the character:! in it.'
    else:
        return " alt The string doesn't have the character:! in it"

string2alt = 'hi'
print(str2alt(string2alt))

#Q5
def check_password(password) -> str:
    found_digit = False
    for char in password:
        if char.isdigit():
            found_digit = True

    if password[0].isupper() and found_digit == True:
        return 'Valid'
    else:
        return 'Invalid'

password = 'Ido12'
print(check_password(password))






