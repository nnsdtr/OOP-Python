
import random


class Animal(object):
    def __init__(self, nome):
        self.nome = nome


class Cachorro(Animal):
    def __init__(self, nome):
        """Superclass constructor:
           - super(Classe, instância_self).método(valor)
           Pegue a superclasse de 'Cachorro' - ou seja, 'Animal' - e passe a
           instância de 'Cachorro' para qualquer método, como por exemplo
           o construtor __init__"""

        print(super(Cachorro, self))
        super(Cachorro, self).__init__(nome)
        self.pedigree = random.choice(['Vira-lata', 'Beagle', 'Mutt'])

    def pegar(self, coisa):
        print('{0} está indo atrás do(a) {1}'.format(self.nome, coisa))


d = Cachorro('Jujuba')

print(d.nome)
print(d.pedigree)
