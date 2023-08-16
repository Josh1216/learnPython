class Calculator:
    def set_value(self,a,b):
        self.value1 = a
        self.value2 = b

class AddCalculator(Calculator):
    def add(self):
        print(self.value1+self.value2)

calculatel = AddCalculator()
calculatel.set_value(3,4)
calculatel.add()