
# Nesta lição, veremos como os dados da classe se relacionam com
# os dados da instância e começaremos a falar sobre situações nas
# quais podemos querer armazenar dados na classe.


class InstanceCounter(object):
    count = 0

    def __init__(self, value):
        self.attribute = value
        InstanceCounter.count += 1

    def set_value(self, new_value):
        self.attribute = new_value

    def get_value(self):
        return self.attribute

    def get_count(self):
        return InstanceCounter.count


a = InstanceCounter(8)
b = InstanceCounter(15)
c = InstanceCounter(23)

print()

for obj in (a, b, c):
    print('Attribute value of obj: {}'.format(obj.get_value()))
    print('count: {}'.format(obj.get_count()))


print(InstanceCounter.count)
print(a.count)               # O valor é olhado primeiro na instância, depois na classe.


# Portanto, nesta lição, vimos um exemplo de atributos de classe, o que também chamamos
# de dados de classe, e como o Python nos permite definir valores na classe que são
# acessíveis através de cada uma das instâncias e também da própria classe.
#
# O que estamos construindo aqui nestas lições até agora é uma compreensão da estrutura
# que os desenvolvedores de software usam no mundo inteiro para criar código que usamos
# todos os dias. À medida em que aprendermos mais, começaremos a ver maneiras pelas quais
# podemos aplicar essa estrutura ao nosso próprio código.
#
# Mas há mais para aprender sobre o paradigma orientado a objetos.
