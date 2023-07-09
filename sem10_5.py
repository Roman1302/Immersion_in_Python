'''Задание №5
📌 Создайте три (или более) отдельных классов животных. Например рыбы, птицы и т.п.
📌 У каждого класса должны быть как общие свойства, например имя, так и специфичные для класса.
📌 Для каждого класса создайте метод, выводящий информацию специфичную для данного класса.
📌 Вынесите общие свойства и методы классов в класс Животное.
📌 Остальные классы наследуйте от него.
📌 Убедитесь, что в созданные ранее классы внесены правки.'''


class Animal:

    def __init__(self, name, weigth, age):
        self.name = name
        self.weigth = weigth
        self.age = age

    def __str__(self):
        return f'{self.name = }, {self.weigth = }, {self.age = }'

    def move(self):
        pass

    def say(self):
        pass


class Bird(Animal):

    def __init__(self, name, weigth, age, vid_bird, sound):
        super().__init__(name, weigth, age)
        self.vid_bird = vid_bird
        self.sound = sound

    def __str__(self):
        return f'{super().__str__()}, {self.vid_bird = }, {self.move() = }, {self.say() = }'

    def move(self):
        return "fly"

    def say(self):
        return self.sound


class Dog(Animal):

    def __init__(self, name, weigth, age, vid_dog):
        super().__init__(name, weigth, age)
        self.vid_dog = vid_dog

    def move(self):
        return "run"

    def say(self):
        return 'гав-гав'

    def __str__(self):
        return f'{super().__str__()}, {self.vid_dog = }, {self.move() = }, {self.say() = }'


class Fish(Animal):

    def __init__(self, name, weigth, age, vid_fish):
        super().__init__(name, weigth, age)
        self.vid_fish = vid_fish

    def move(self):
        return "swim"

    def say(self):
        return 'буль-буль'

    def __str__(self):
        return f'{super().__str__()}, {self.vid_fish = }, {self.move() = }, {self.say() = }'


if __name__ == '__main__':
    bird_solov = Bird('Соловей', 3, 5, 'Птицы', 'тру-ля-ля')
    dog_shpic = Dog('Терьер', 30, 15, 'Собаки')
    fish_fish = Fish('Гупи', 0, 2, 'Рыбы')

    print(bird_solov)
    print(dog_shpic)
    print(fish_fish)
