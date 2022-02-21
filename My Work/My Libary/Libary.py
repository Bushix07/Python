def question(question, op1, op2, op3, op4, right, wrong, true_word, true):
    print(question)
    answer = input(f'1){op1}\n2){op2}\n3){op3}\n4){op4}\nAnswer: ')
    if answer == true or answer == true_word:
        print(right)
    else:
        print(wrong)


def iseven(num: int) -> bool:
    if num % 2 == 0:
        return True
    else:
        return False


def isodd(num: int) -> bool:
    if num % 2 == 1:
        return True
    else:
        return False

#summation
def sum_int(num: int) -> int:
    total = 0
    str_of_num = str(num)
    for digit in range(len(str_of_num)):
        total += int(str_of_num[digit])
    return total

def sum_str(num: str) -> int:
    total = 0
    for digit in range(len(num)):
        total += int(num[digit])
    return total

def sum_lst(lst: list) -> int:
    total = 0
    for digit in range(len(lst)):
        total += lst[digit]
    return total


#difference
def dif_int(num: int) -> int:
    total = 0
    str_of_num = str(num)
    for digit in range(len(str_of_num)):
        total -= int(str_of_num[digit])
    return total

def dif_str(num: str) -> int:
    total = 0
    for digit in range(len(num)):
        total -= int(num[digit])
    return total

def dif_lst(lst: list) -> int:
    total = 0
    for digit in range(len(lst)):
        total -= lst[digit]
    return total


#product (math)
def mult_int(num: int) -> int:
    total = 1
    str_of_num = str(num)
    for digit in range(len(str_of_num)):
        total *= int(str_of_num[digit])
    return total

def mult_str(num: str) -> int:
    total = 1
    for digit in range(len(num)):
        total *= int(num[digit])
    return total

def mult_lst(lst: list) -> int:
    total = 1
    for digit in range(len(lst)):
        total *= lst[digit]
    return total
