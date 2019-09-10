

class A(object):
    def do_this(self):
        print('do_this() in A')


class B(A):
    pass


class C(A):
    def do_this(self):
        print('do_this() in C')


class D(B, C):
    pass


D_instance = D()

D_instance.do_this()

print(D.mro())   # Method resolution order