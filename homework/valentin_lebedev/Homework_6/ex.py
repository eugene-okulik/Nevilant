# Задание 1

text = ("Etiam tincidunt neque erat, quis molestie enim imperdiet vel. "
        + "Integer urna nisl, facilisis vitae semper at, dignissim vitae libero")
list_text = text.split()
edit_text = []

for word in list_text:
    if word[-1] in [",", "."]:
        edit_word = word[:-1] + "ing" + word[-1]
    else:
        edit_word = word + "ing"
    edit_text.append(edit_word)

print(' '.join(edit_text))

# Задание 2

for i in range(1, 100):
    if i % 15 == 0:
        print("FuzzBuzz")
    elif i % 3 == 0:
        print("Fuzz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
