class Pizza:
    """
    Базовый класс для пиццы.
    Можно задать рецепт виде словаря с названием ингредиентов
    и их количеством, а также размер пиццы.
    Рецепт можно вывести через dict().
    Можно сравнить две пиццы через магический метод __eq__().
    """

    def __init__(self, size='L'):
        if size == 'L':
            self.receipt = {
                'tomato sauce': 111,
                'mozzarella': 123,
            }
        elif size == 'XL':
            self. receipt = {
                'tomato sauce': 222,
                'mozzarella': 321,
            }
        else:
            raise ValueError('Size must be L or XL')
        self.size = size

    def dict(self):
        return self.receipt

    def __eq__(self, other):
        if not isinstance(other, Pizza):
            return False
        return self.__dict__ == other.__dict__
