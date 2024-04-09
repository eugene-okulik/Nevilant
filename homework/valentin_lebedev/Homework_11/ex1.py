class Book:
    page_material = 'Бумага'
    availability_of_text = True

    def __init__(self, title, author, count_of_page, isbn, reserved=False):
        self.title = title
        self.author = author
        self.count_of_page = count_of_page
        self.isbn = isbn
        self.reserved = reserved

    def print_info(self):
        reserved_text = "зарезервирована" if self.reserved else ""
        return (
            f'Название: {self.title}, Автор: {self.author}, страниц: {self.count_of_page}, '
            f'материал: {self.page_material}, {reserved_text}'
            )


if __name__ == "__main__":
    first_book = Book(
        'Гарри Поттер и философский камень', 'Джоан Роулинг', 432, '978-5-389-07435-4',
    )
    second_book = Book(
        'Маленький принц', 'Антуан де Сент-Экзюпери', 80, '978-5-00214-076-3'
    )
    third_book = Book(
        'Властелин колец', 'Джон Толкин', 448, '978-5-17-133596-0', reserved=True
    )
    fourth_book = Book(
        'Повесть о двух городах', 'Чарльз Диккенс', 480, '978-5-4484-1521-0'
    )
    fifth_book = Book(
        'Дон Кихот', 'Сервантес Мигель де Сааведра', 1120, '978-5-04-156264-9'
    )

    list_books = [first_book, second_book, third_book, fourth_book, fifth_book]

    for book in list_books:
        print(book.print_info())
