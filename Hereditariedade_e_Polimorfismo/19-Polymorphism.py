
class Animal(object):
    def __init__(self, nome):
        self.nome = nome

    def comer(self, comida):
        print('{0} come {1}'.format(self.nome, comida))


class Cachorro(Animal):
    def pegar(self, thing):
        print('{0} vai atrás do(a) {1}'.format(self.nome, thing))

    def mostrar_afeto(self):
        print('{0} balança o rabo'.format(self.nome))


class Gato(Animal):
    def golpear_corda(self):
        print('{0} golpeia a corda'.format(self.nome))

    def mostrar_afeto(self):
        print('{0} ronrona'.format(self.nome))


for instancia in (Cachorro('Jujuba'), Gato('Minigato'), Gato('Zé droguinha'), Cachorro('Staney')):
    instancia.mostrar_afeto()
