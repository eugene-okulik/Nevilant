# Задание 1

person = ['John', 'Doe', 'New York', '+1372829383739', 'US']

a, b, c, d, e = person

# Задание 2

text_1 = 'результат операции: 42'
text_2 = 'результат операции: 514'
text_3 = 'результат работы программы: 9'


def slice_text(text):
    return int(text[text.index(':') + 2:]) + 10


print(slice_text(text_1) + 10, slice_text(text_2), slice_text(text_3), sep='\n')

# Задание 3

students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']

sentence = f'Students {", ".join(students)} study these subjects: {", ".join(subjects)}'

print(sentence)
