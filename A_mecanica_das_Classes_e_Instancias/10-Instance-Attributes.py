
import random


class MyClass(object):
    def print_this(self):
        print('Printing this')

    def random_number(self):
        self.rand_val = random.randint(1, 10)


instance_1 = MyClass()

instance_1.print_this()

instance_1.random_number()
print(instance_1.rand_val)
