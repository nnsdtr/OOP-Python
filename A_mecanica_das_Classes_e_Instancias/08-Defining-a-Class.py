print()


###################################################################################################
# Demonstração de que cada instância está ciente da classe de onde veio.

class MinhaClasse(object):
    pass


# Criando instâncias da classe 'MyClass'
this_obj = MinhaClasse()
that_obj = MinhaClasse()


# Instâncias da classe 'MyClass' e seus endereços na memória
print('this_obj address: ' + str(this_obj))
print('that_obj address: ' + str(that_obj))

print()


###################################################################################################
# Variáveis definidas na classe estão disponíveis nas instâncias através da sintaxe de atribuição
# a objetos. No entanto, o atributo não está localizado na instância, porém na Classe.

class MinhaClasse2(object):
    var = 10


this_obj2 = MinhaClasse2()
that_obj2 = MinhaClasse2()

print('this_obj2.var value: ' + str(this_obj2.var))   # Instâncias têm acesso ao valor da
print('that_obj2.var value: ' + str(that_obj2.var))   # variável inserida na classe

print()
