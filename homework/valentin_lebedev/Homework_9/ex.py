import datetime


# Задание 1

my_time = "Jan 15, 2023 - 12:05:33"
python_date = datetime.datetime.strptime(my_time, "%b %d, %Y - %H:%M:%S")
month = python_date.strftime("%B")
human_date = python_date.strftime("%d.%m.%Y, %H:%M")
print(python_date)
print(month)
print(human_date)

# Задание 2

temperatures = [20, 15, 32, 34, 21,
                19, 25, 27, 30, 32,
                34, 30, 29, 25, 27,
                22, 22, 23, 25, 29,
                29, 31, 33, 31, 30,
                32, 30, 28, 24, 23]

hot_days = list(filter(lambda x: x > 28, temperatures))
print(hot_days)
average = sum(hot_days) / len(hot_days)
print(max(hot_days))
print(min(hot_days))
print(round(average))
