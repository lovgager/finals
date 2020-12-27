import base_pizza


class Margherita(base_pizza.Pizza):
    """Класс для пиццы Маргарита"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.receipt['tomatoes'] = 222
        if self.size == 'XL':
            self.receipt['tomatoes'] = 333
        self.emoji = '🧀'


class Pepperoni(base_pizza.Pizza):
    """Класс для пиццы Пепперони"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.receipt['pepperoni'] = 222
        if self.size == 'XL':
            self.receipt['tomatoes'] = 333
        self.emoji = '🍕'


class Hawaiian(base_pizza.Pizza):
    """Класс для гавайской пиццы"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.receipt['chicken'] = 111
        self.receipt['pineapples'] = 123
        if self.size == 'XL':
            self.receipt['chicken'] = 222
            self.receipt['pineapples'] = 345
        self.emoji = '🍍'
