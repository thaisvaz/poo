class Numero:

    def __init__(self, value):

        self.value = value

    # def __str__(self):
        # return str(self.value)

    def __add__(self, other):

        return Numero(self.value / other.value)

a = Numero(5)
print(a)

b = Numero(7)
print(b)

c = a + b

print(c)