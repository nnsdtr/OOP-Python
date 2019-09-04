

# EXEMPLO 1:
class MyClass(object):
    def set_attrib(self, val):    # Method 1: attribute 'setter'
        self.attribute = val

    def get_attrib(self):         # Method 2: attribute 'getter'
        return self.attribute


a = MyClass()       # Instance 'a'
b = MyClass()       # Instance 'b'

a.set_attrib(10)
b.set_attrib(100)

print(a.get_attrib())
print(b.get_attrib())


# EXEMPLO 2:
# O motivo do uso de métodos 'set_attribute' e 'get_attribute', ao invés de fornecer
# atributos diretamente às instâncias, é que o uso desses métodos fornece um tipo
# de 'gateway' para qualquer operação relacionada ao estado das instâncias.
#
# E nesse 'gateway', podemos garantir a integridade dos atributos das instâncias.
# Ao usar esses métodos, estamos encapsulando a instância e garantindo a
# integridade de seus dados. Veja:

class MyInt(object):
    def set_attribute(self, value):
        try:
            attribute = int(value)
        except ValueError:
            return
        else:
            self.attribute = attribute

    def get_attribute(self):
        return self.attribute

    def increment_attrib_value(self):
        self.attribute += 1


i = MyInt()
i.set_attribute(9)
print(i.get_attribute())

j = MyInt()
j.set_attribute('hello')      # ERRO: " 'MyInt' object has no attribute 'attribute' ".  O atributo 'hello' não é passado
print(j.get_attribute())      # para a instância 'j'. Logo, não é possível imprimi-lo, pois ele não existe.


# Ao invés de fornecermos o valor através do método 'set_attribute()', vamos
# tentar passá-lo diretamente ao atributo 'attribute'. Vejamos o que ocorre:

k = MyInt()
k.attribute = 'hello'           # Conseguimos, sim, fornecer uma 'str' ao atributo.
print(k.get_attribute())        # Porém, estamos quebrando o encapsulamento.


# Agora, se tentarmos utilizar o método increment_attrib_value(), vejamos o que ocorre:

k.increment_attrib_value()      # ERRO: " can only concatenate str (not 'int') to str "

# O Encapsulamento, então, confere integridade aos dados presentes
# nas instâncias, portanto, não é recomendado quebrá-lo.
