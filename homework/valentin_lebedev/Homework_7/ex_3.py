text_1 = 'результат операции: 42'
text_2 = 'результат операции: 514'
text_3 = 'результат работы программы: 9'
text_4 = 'результат: 2'


def ex_3(text):
    for i in text.split():
        if i.isdigit():
            return int(i) + 10


print(ex_3(text_1), ex_3(text_2), ex_3(text_3), ex_3(text_4), sep='\n')
