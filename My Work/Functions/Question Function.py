def question(question, op1, op2, op3, op4, right, wrong, true_word, true):
    print(question)
    answer = input(f'1){op1}\n2){op2}\n3){op3}\n4){op4}\nAnswer: ')
    if answer == true or answer == true_word:
        print(right)
    else:
        print(wrong)


#question(question='is it a great day ?', op1='yes', op2='no', op3='hell yea', op4='hell nah', right='You are right!',
         #wrong='You are wrong', true='2', true_word='no')
