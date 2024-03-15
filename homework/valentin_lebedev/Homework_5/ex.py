# Задание 1

person = ['John', 'Doe', 'New York', '+1372829383739', 'US']

a, b, c, d, e = person

# Задание 2

text_1 = 'результат операции: 42'
text_2 = 'результат операции: 514'
text_3 = 'результат работы программы: 9'
slice_text_1 = int(text_1[-2:]) + 10
slice_text_2 = int(text_2[-3:]) + 10
slice_and_index_text_3 = int(text_3[text_3.index(':') + 2:]) + 10

print(slice_text_1, slice_text_2, slice_and_index_text_3, sep='\n')

# Задание 3

students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']

sentence = f'Students {", ".join(students)} study these subjects: {", ".join(subjects)}'

print(sentence)
