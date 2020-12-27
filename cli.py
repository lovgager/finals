import click
import inspect
import pizza_menu
from base_pizza import *
from random import randint


@click.group()
def cli():
    pass


@cli.command()
@click.option('--delivery', default=False, is_flag=True)
@click.argument('pizza', nargs=1)
def order(pizza: str, delivery: bool):
    """Готовит и доставляет пиццу"""
    
    pizza_dict = dict(get_menu())
    pizza_names = pizza_dict.keys()
    if pizza not in pizza_names:
        print('Такой пиццы нет в меню')
        return
    bake(pizza_dict[pizza])
    if delivery:
        delivery_func(pizza_dict[pizza]())
    else:
        pickup(pizza_dict[pizza]())


def get_menu():
    """Возвращает список всех имеющихся видов пиццы
    в виде кортежа (название_пиццы, тип_класса)"""
    
    pizzas = [
        (cls_name.lower(), cls_obj) for cls_name, cls_obj
        in inspect.getmembers(pizza_menu)
        if inspect.isclass(cls_obj)
    ]
    return pizzas


@cli.command()
def menu():
    """Выводит меню с помощью извлечения
    всех классов из модуля pizza_menu"""

    pizzas = get_menu()
    for pizza in pizzas:
        pizza_obj = pizza[1]()
        print(
            ' -',
            pizza[0].title(),
            pizza_obj.emoji,
            ':',
            ', '.join(pizza_obj.dict())
        )


def log(template: str):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            print(template.format(randint(1, 20)))
            return result
        return wrapper
    return decorator


@log("🍕‍Приготовили за {}с!")
def bake(pizza: Pizza):
    pass


@log("🛵 Доставили за {}с!")
def delivery_func(pizza: Pizza):
    pass


@log("🏠 Забрали за {}с!")
def pickup(pizza: Pizza):
    pass


if __name__ == '__main__':
    cli()
