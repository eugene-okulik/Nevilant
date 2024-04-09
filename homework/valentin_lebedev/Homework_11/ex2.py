from ex1 import Book


class SchoolBook(Book):
    availability_of_task = True

    def __init__(self, title, author, count_of_page, subject, school_class, reserved=False):
        super().__init__(title, author, count_of_page, reserved)
        self.subject = subject
        self.school_class = school_class


first_sb = SchoolBook('Биология', 'Соловьева', 320, 'Зоология', 8)
second_sb = SchoolBook('Геометрия', 'Иванова', 180, 'Математика', 9)
third_sb = SchoolBook(
    'Алгебра', 'Баранова', 250, 'Математика', 10, reserved=True
)

list_sb = [first_sb, second_sb, third_sb]

for sb in list_sb:
    print(sb.print_info())
