class Num:
    def __init__(self, a, b):
        if type(a) == 'int':
            self.a = a
        else:
            self.a = int(a)

        if type(b) == 'int':
            self.b = b
        else:
            self.b = int(b)

    def raz(self):
        return (self.a - self.b)

    def __add__(self, other):
        newa = self.a + other.a
        newb = self.b + other.b
        return Num(newa, newb)

    def __str__(self):
        return "(%f, %f)" %(self.a, self.b)

f = Num(3, 4)
d = Num(2, 5)

print(f + d)


