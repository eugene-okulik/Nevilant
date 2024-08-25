insert into students (name, second_name) 
values 
	('Nevi', 'Lant');

insert into books (title, taken_by_student_id) 
values 
	('Harry Potter 1', 412),
	('Harry Potter 2', 412),
	('Harry Potter 3', 412);

insert into `groups` (title, start_date, end_date) 
values 
	('QA Automation', '12.03.2024', '05.10.2024');

update students 
set group_id=402 
where id=412;

insert into subjects (title)
values
	('MySQL'),
	('PostgreSQL'),
	('MariaDB');

insert into lessons (title, subject_id)
values
	('Based MySQL', 443),
	('Advanced MySQL', 443),
	('Based PostgrSQL', 444),
	('Advanced PostgeSQL', 444),
	('Based MariaBD', 445),
	('Advanced MariaBD', 445);

insert into marks (value, lesson_id, student_id)
values
	('A', 712, 412),
	('B', 713, 412),
	('A+', 714, 412),
	('A', 715, 412),
	('A', 716, 412),
	('C', 717, 412);

select value
from marks
where student_id = 412;

select title
from books
where taken_by_student_id = 412;

select 
	s.name, 
	s.second_name, 
	g.title as 'group',
	b.title as 'title_book',
	m.value as 'mark',
	l.title as 'lesson',
	s2.title as 'subject'
from students s
join `groups` g on s.group_id = g.id
join books b on s.id = b.taken_by_student_id
join marks m on s.id = m.student_id
join lessons l on m.lesson_id = l.id
join subjects s2 on l.subject_id = s2.id
where s.id = 412;

