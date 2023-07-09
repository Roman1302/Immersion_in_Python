'''Доработаем задачи 5-6. Создайте класс-фабрику.
○ Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
○ Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.'''

from sem10_5 import Dog, Bird, Fish


class Fabric:

    def make_animal(self, animal_type, *args, **kwargs):
        new_animal = self._get_maker(animal_type)
        return new_animal(*args, **kwargs)

    def _get_maker(self, animal_type):
        types = {"dog": Dog, "bird": Bird, "fish": Fish}
        return types[animal_type.lower()]


if __name__ == '__main__':
    fabric = Fabric()
    animal_from_fabric = fabric.make_animal('Bird', 'Соловей', 3, 5, 'соловейки', 'тру-ля-ля')
    print(animal_from_fabric)
