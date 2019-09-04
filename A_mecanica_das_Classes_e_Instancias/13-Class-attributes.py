
# Neste script, vamos fazer uma comparação entre 'atributos de Classe' e 'atributos de Instâncias'.
# Vamos mostrar como a instância pode acessar ambos.


class ThisClass(object):
    class_attribute = 10

    def set_val(self):
        self.inst_attribute = 100


instc = ThisClass()
instc.set_val()

print('\nTest number 1:')
print(instc.class_attribute)
print(instc.inst_attribute)


# Vamos fazer um segundo teste:
class ThatClass(object):
    class_attrib = 'Class attribute value!'


print('\nTest number 2:')

instance1 = ThatClass()
print(instance1.class_attrib)


# Podemos modificar o valor do atributo, mas ele passa a ser armazenado, na instância
# não na classe. O valor da classe é imutável.
instance1.class_attrib = 'Instance attribute value!'
print(instance1.class_attrib)


# Novas instâncias não sofrem com a modificação gerada anteriormente. O valor do atributo
# da classe é mantido, o que nos revela que modificações são guardadas no âmbito da instância.
instance2 = ThatClass()
print(instance2.class_attrib)


# Se deletarmos o atributo modificado, seu valor retorna à configuração original presente na classe.
del instance1.class_attrib
print(instance1.class_attrib)


# Com isso, podemos perceber que os atributos são primeiro vistos no âmbito da
# instância e, logo depois, no âmbito da classe. A instância tem preferência.
