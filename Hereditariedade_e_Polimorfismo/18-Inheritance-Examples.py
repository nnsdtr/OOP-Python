
class Animal(object):
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print('{0} is eating {1}'.format(self.name, food))


class Dog(Animal):
    def fetch(self, thing):
        print('{0} goes after the {1}'.format(self.name, thing))


class Cat(Animal):
    def swat_string(self):
        print('{} shreds the string!'.format(self.name))


minigato = Cat('Minigato')
jujuba = Dog('Jujuba')

jujuba.fetch('ball')

minigato.swat_string()

minigato.eat('cat food')
jujuba.eat('dog food')

# jujuba.swat_string()   # AttributeError: 'Dog' object has no attribute 'swat_string'


