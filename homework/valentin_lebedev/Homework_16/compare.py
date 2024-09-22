import csv
import os
import pathlib

import dotenv
import mysql.connector as mysql

# Загружаем переменные окружения
dotenv.load_dotenv()

# Подключаемся к базе данных
db = mysql.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_NAME')
)

cursor = db.cursor()

# Определяем путь к CSV файлу
FILE_PATH = 'Nevilant/homework/eugene_okulik/Lesson_16/hw_data/data.csv'
FULL_PATH = pathlib.Path(os.getenv('BASE_PATH')).joinpath(FILE_PATH)

data_list = []

# Чтение данных из CSV файла
with open(FULL_PATH, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)  # Пропускаем заголовок

    for row in csvreader:
        student_name = row[0]
        student_second_name = row[1]
        group_title = row[2]
        book_title = row[3]
        subject_title = row[4]
        lesson_title = row[5]
        mark_value = row[6]

        query = """
        SELECT s.name, s.second_name, g.title, b.title, ss.title, l.title, m.value
        FROM students s
        JOIN `groups` g ON s.group_id = g.id
        JOIN books b ON s.id = b.taken_by_student_id
        JOIN marks m ON s.id = m.student_id
        JOIN lessons l ON l.id = m.lesson_id
        JOIN subjets ss ON l.subject_id = ss.id
        WHERE s.name = %s AND s.second_name = %s AND g.title = %s AND b.title = %s
        AND ss.title = %s AND l.title = %s AND m.value = %s
        """

        cursor.execute(
            query,
            (
                student_name,
                student_second_name,
                group_title, book_title,
                subject_title,
                lesson_title,
                mark_value
            )
        )
        result = cursor.fetchone()

        if not result:
            data_list.append(row)

cursor.close()
db.close()

if data_list:
    print('Отсутствуют следующие данные:')
    for row in data_list:
        print(row)
else:
    print('Все данные присутствуют')
