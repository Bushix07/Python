# Q1
def even_to_number(number) -> int:
    for i in range(2, number + 1, 2):
        print(i)


even_to_number(30)


# Q1 (Alternative)

def alternative_even_to_number(number) -> int:
    for i in range(number + 1):
        if i % 2 == 0:
            print(i)

alternative_even_to_number(30)


#Q2
def find_average():
    total_of_input = 0
    total = 0
    number = int(input('Enter a number'))
    while number != -2:
        total = total + number
        total_of_input += 1
        number = int(input('Enter a number'))
    print('-2 was found!')
    print('The average of all the numbers is:', total / total_of_input)

find_average()

#Q3
def sum_digit1(number) -> int:
    total = 0
    string_of_number = str(number)
    for i in range(len(string_of_number)):
        total = total + int(string_of_number[i])

    return total
number = 123
print(sum_digit1(number))

def sum_digit2(number) -> str:
    total = 0
    for i in range(len(number)):
        total = total + int(number[i])
    return total

number1 = '123'
print(sum_digit2(number1))

def sum_digit3(lst) -> list:
    return sum(lst)

lst = [1, 2, 3]
print(sum_digit3(lst))


#Q4
def largest_1(lst) -> list:
    max = lst[0]
    for i in range(len(lst)):
        if max < lst[i]:
            max = lst[i]
    return max

lst = [5, 3, 10, 99, -1]
print(largest_1(lst))

def largest_2(lst1) -> list:
    lst2 = lst.copy()
    first_max = max(lst2)
    lst2.remove(first_max)
    second_max = max(lst2)
    return [first_max, second_max]

print(largest_2(lst))

lst = [5, 3, 10, 99, -1]
def largest_3(lst1) -> list:
    first_max = max(lst1)
    lst1.remove(first_max)
    second_max = max(lst1)
    lst1.remove(second_max)
    third_max = max(lst1)
    return [first_max, second_max, third_max]

print(largest_3(lst))