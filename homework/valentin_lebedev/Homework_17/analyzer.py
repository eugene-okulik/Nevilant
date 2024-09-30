import argparse
import os


parser = argparse.ArgumentParser(description="Поиск текста в логах.")

# Позиционный аргумент
parser.add_argument("dir", help="указать полный путь до папки с логами")
# Опциональные аргументы
parser.add_argument("-t", "--text", help="указать текст, который будем искать")
parser.add_argument("-o", "--one",
                    action="store_true",
                    help="вывести только первый найденный результат")
parser.add_argument("-b", "--before",
                    type=int,
                    default=5,
                    help="указать сколько слов показать до искомого слова")
parser.add_argument("-a", "--after",
                    type=int,
                    default=5,
                    help="указать сколько слов показать после искомого слова")

args = parser.parse_args()
search_text = args.text
before = args.before
after = args.after

for filename in os.listdir(args.dir):
    print(f"Analyzing {filename}...", end="\n")
    flag = False
    with open(os.path.join(args.dir, filename), "r") as file:
        for index, line in enumerate(file):
            string_list = line.split()
            if search_text in string_list:
                our_index = string_list.index(search_text)
                print(f"---The string: '{search_text}' found in file: '{filename}' on line: {index + 1}:")
                print(
                    f"---{' '.join(string_list[max(0, our_index - before):our_index])} {' '.join(string_list[our_index:our_index + after])}",
                    end="\n")
                if args.one:
                    flag = True
                    break
    if flag:
        break

    print(f"File analysis '{filename}' finished!", end="\n\n")
