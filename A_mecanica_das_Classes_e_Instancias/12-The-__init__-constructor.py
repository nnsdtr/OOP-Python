
# O construtor __init__ é um método especial que nos permite inicializar atributos
# no momento em que uma instância é construída. Como vimos no script anterior, os
# atributos são tradicionalmente configurados usando um método set_attribute_val().


class MyNumber(object):
    def __init__(self, value):                # Duplos 'underscores' antes e depois dos nomes são utilizados para
        print('Calling __init__ method')      # métodos chamados 'private' ou 'magic'. 'Private', porque não têm
        try:                                  # a intenção de serem usados pelo usuário e, 'magic', porque são
            attribute = int(value)            # automaticamente chamados quando um determinado evento acontece.
        except ValueError:
            print('\nWARNING: You cannot use \'str\' values in \'MyNumber\' class.\n'
                  'Setting value to 0.')
            self.attribute = 0
        else:
            self.attribute = attribute

    def get_value(self):
        return self.attribute

    def increment(self):
        self.attribute += 1


num = MyNumber(10)               # __init__ é chamada durante a inicialização de uma instância.
print(num.get_value())

num.increment()
num.increment()
print(num.get_value())


num2 = MyNumber('hello')
print(num2.get_value())

num2.increment()
num2.increment()
print(num2.get_value())

