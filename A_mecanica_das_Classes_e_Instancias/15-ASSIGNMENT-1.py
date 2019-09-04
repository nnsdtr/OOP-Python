
class MaxSizeList(object):
    def __init__(self, max_size_value):
        self.max_size = max_size_value
        self.inner_list = []

    def push(self, value):
        self.inner_list.append(value)
        if len(self.inner_list) > self.max_size:
            self.inner_list.pop(0)

    def get_list(self):
        return self.inner_list


a = MaxSizeList(3)
b = MaxSizeList(1)

a.push('hey')
a.push('hi')
a.push("let's")
a.push('go')

b.push('hey')
b.push('hi')
b.push("let's")
b.push('go')

print(a.get_list())
print(b.get_list())
