class Flower:
    def __init__(self, name, color, stem_length, freshness, cost, lifespan):
        self.name = name
        self.color = color
        self.stem_length = stem_length
        self.freshness = freshness
        self.cost = cost
        self.lifespan = lifespan

    def __repr__(self):
        return (f"{self.name}(Цвет: {self.color}, Длина стебля: {self.stem_length}, Свежесть: {self.freshness}, "
                f"Стоимость: {self.cost}, Срок жизни: {self.lifespan})")


class Rose(Flower):
    def __init__(self, color, stem_length, freshness, cost, lifespan):
        super().__init__('Роза', color, stem_length, freshness, cost, lifespan)


class Tulip(Flower):
    def __init__(self, color, stem_length, freshness, cost, lifespan):
        super().__init__('Тюльпан', color, stem_length, freshness, cost, lifespan)


class Lily(Flower):
    def __init__(self, color, stem_length, freshness, cost, lifespan):
        super().__init__('Лилия', color, stem_length, freshness, cost, lifespan)


class Bouquet:
    def __init__(self):
        self.flowers = []

    def add_flower(self, flower: object) -> None:
        """
        Добавляем цветок в букет.
        :param flower: Указываем название цветка (цветок - созданный экземпляр класса)
        """
        self.flowers.append(flower)

    def total_cost(self) -> int:
        """
        :return: Возвращаем цену букета
        """
        return sum(flower.cost for flower in self.flowers)  # Суммируем цену каждого цветка в букете

    def average_lifespan(self):
        """
        :return: Возвращаем среднюю продолжительность жизни цветка в букете
        """
        return sum(flower.lifespan for flower in self.flowers) / len(self.flowers)

    def sort_by(self, attribute):
        """
        Сортирует цветы в букете по указанному атрибуту.

        :param attribute: Атрибут для сортировки (например, 'freshness', 'color', 'stem_length', 'cost', 'name').
        """
        if attribute in ['freshness', 'color', 'stem_length', 'cost', 'name']:
            self.flowers.sort(key=lambda x: getattr(x, attribute))
        else:
            print(f"Невозможно отсортировать по параметру: {attribute}")

    def find_flowers(self, attribute, value):
        return [flower for flower in self.flowers if getattr(flower, attribute) == value]

    def __repr__(self):
        return f"Букет: {self.flowers}"


# Создаем экземпляры цветов
rose1 = Rose(color='Красный', stem_length=50, freshness=10, cost=150, lifespan=7)
rose2 = Rose(color='Белый', stem_length=45, freshness=9, cost=130, lifespan=6)
tulip1 = Tulip(color='Желтый', stem_length=35, freshness=8, cost=70, lifespan=5)
lily1 = Lily(color='Розовый', stem_length=40, freshness=10, cost=100, lifespan=8)

# Создаем букет
bouquet = Bouquet()
bouquet.add_flower(rose1)
bouquet.add_flower(rose2)
bouquet.add_flower(tulip1)
bouquet.add_flower(lily1)

# Выводим информацию о букете
print(bouquet)

# Определяем общую стоимость букета
print("Общая стоимость букета:", bouquet.total_cost())

# Определяем среднее время жизни букета
print("Среднее время жизни букета:", bouquet.average_lifespan())

# Сортируем цветы по стоимости
bouquet.sort_by('cost')
print("Букет после сортировки по стоимости:", bouquet)

# Ищем цветы по цвету
print("Цветы в букете с цветом 'Красный':", bouquet.find_flowers('color', 'Красный'))
