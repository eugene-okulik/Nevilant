import mysql.connector as mysql


db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = db.cursor(dictionary=True)


query_add_student = '''
    INSERT INTO students (name, second_name)
    VALUES (%s, %s)
'''
values_student = ('Nevi', 'Lant')
cursor.execute(query_add_student, values_student)
student_id = cursor.lastrowid

query_add_books = '''
    INSERT INTO books (title, taken_by_student_id)
    VALUES (%s, %s)
'''
values_books = [
    ('Python for dummies', f'{student_id}'),
    ('SQL for dummies', f'{student_id}'),
    ('QA for dummies', f'{student_id}'),
]
cursor.executemany(query_add_books, values_books)

query_groups = '''
    INSERT INTO `groups` (title, start_date, end_date)
    VALUES (%s, %s, %s)
'''
values_groups = ('AQA', '12.03.2024', '05.10.2024')
cursor.execute(query_groups, values_groups)
group_id = cursor.lastrowid

query_update_students = '''
    UPDATE students
    SET group_id = %s
    WHERE id = %s
'''
values_update_students = (group_id, student_id)
cursor.execute(query_update_students, values_update_students)

query_subjects = '''
    INSERT INTO subjets (title)
    VALUES (%s)
'''
values_subjects = [
    ('Python',),
    ('SQL',),
    ('Theory of QA',)
]
cursor.executemany(query_subjects, values_subjects)

cursor.execute('''
    SELECT id, title
    FROM subjets
    WHERE title IN ('Python', 'SQL', 'Theory of QA')
''')
subject_ids = {row['title']: row['id'] for row in cursor.fetchall()}

query_lessons = '''
    INSERT INTO lessons (title, subject_id)
    VALUES (%s, %s)
'''
values_lessons = [
    ('Based Python', subject_ids['Python']),
    ('Advanced Python', subject_ids['Python']),
    ('Based SQL', subject_ids['SQL']),
    ('Advanced SQL', subject_ids['SQL']),
    ('Based Theory of QA', subject_ids['Theory of QA']),
    ('Advanced Theory of QA', subject_ids['Theory of QA']),
]
cursor.executemany(query_lessons, values_lessons)
cursor.execute('''
    SELECT id, title
    FROM lessons
    ORDER BY id DESC
    LIMIT 6
''')
lesson_ids = {row['title']: row['id'] for row in cursor.fetchall()}

query_marks = '''
    INSERT INTO marks (value, lesson_id, student_id)
    VALUES (%s, %s, %s)
'''
values_marks = [
    ('A', lesson_ids['Based Python'], student_id),
    ('B', lesson_ids['Based SQL'], student_id),
    ('C', lesson_ids['Based Theory of QA'], student_id),
    ('D', lesson_ids['Advanced Python'], student_id),
    ('E', lesson_ids['Advanced SQL'], student_id),
    ('F', lesson_ids['Advanced Theory of QA'], student_id),
]
cursor.executemany(query_marks, values_marks)

db.commit()

db.close()
