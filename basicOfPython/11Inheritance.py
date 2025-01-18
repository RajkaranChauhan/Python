from OppsClassConstructorAndObeject import Calculator


class InheritanceChild(Calculator):
    num3 = 700

    def __init__(self):
        Calculator.__init__(self, 22, 33)

    def getData(self):
        return self.num3 + self.num + self.addition()


obj3 = InheritanceChild()
print(obj3.getData())
