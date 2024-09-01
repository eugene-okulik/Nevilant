import mysql.connector as mysql

db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = db.cursor(dictionary=True)

student_id = 2063


query = '''
    SELECT value
    FROM marks
    WHERE student_id = %s
'''
value = (student_id,)
cursor.execute(query, value)
print(cursor.fetchall())

query = '''
    SELECT title
    FROM books
    WHERE taken_by_student_id = %s
'''
value = (student_id,)
cursor.execute(query, value)
print(cursor.fetchall())

query = '''
    SELECT
        s.name,
        s.second_name,
        g.title as 'group',
        b.title as 'title_book',
        m.value as 'mark',
        l.title as 'lesson',
        s2.title as 'subject'
    FROM students as s
    JOIN `groups` as g ON s.group_id = g.id
    JOIN books as b ON s.id = b.taken_by_student_id
    JOIN marks as m ON s.id = m.student_id
    JOIN lessons as l ON m.lesson_id = l.id
    JOIN subjets as s2 ON l.subject_id = s2.id
    WHERE s.id = %s
'''
value = (student_id,)
cursor.execute(query, value)
print(cursor.fetchall())

db.close()
