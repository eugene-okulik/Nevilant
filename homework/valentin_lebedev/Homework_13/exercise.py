import datetime
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
data_file = os.path.join(BASE_DIR, '../../eugene_okulik/hw_13/data.txt')


with open(data_file, 'r', encoding='UTF-8') as file:
    lines = file.readlines()


for line in lines:
    if line[0] == '1':
        now_date = datetime.datetime.strptime(line[3:29], '%Y-%m-%d %H:%M:%S.%f')
        edit_now = now_date + datetime.timedelta(weeks=1)
        print(edit_now)
    elif line[0] == '2':
        now_date = datetime.datetime.strptime(line[3:29], '%Y-%m-%d %H:%M:%S.%f')
        day_of_week = now_date.strftime('%A')
        print(day_of_week)
    elif line[0] == '3':
        before_date = datetime.datetime.strptime(line[3:29], '%Y-%m-%d %H:%M:%S.%f')
        now_date = datetime.datetime.now()
        days = (now_date - before_date).days
        print(days)
