# Exemplo 1:
class Person(object):
    greeting = '\nHello there!'


joe = Person()

print(joe.greeting)

print('\n')


# Exemplo 2:
# Método interno à classe utiliza self como 1º parâmetro, sempre.
class Something(object):
    def call_this_method(self):
        print('Verificação de john == john.call_this_method() resulta em:')
        return self


# Criando instância da classe 'Something'
john = Something()

# Verificação de igualdade
print(john == john.call_this_method())    # Logo, a instância 'john' é o próprio parâmetro 'self'!
