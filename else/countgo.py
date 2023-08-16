
class CountGo:
    def __init__(self,a,b):
        self.value1 = a
        self.value2 = b
    def add(self):
        c = self.value1 + self.value2
        return c
    def subtract(self):
        c = self.value1 - self.value2
        return c
    def multiply(self):
        c = self.value1 * self.value2
        return c
    def divide(self):
        c = self.value1 / self.value2
        return c
        
num1 = int(input("輸入數字1: "))
num2 = int(input("輸入數字2: "))
c = CountGo(num1,num2)

print("兩數相加為",c.add())
print("兩數相減為",c.subtract())
print("兩數相乘為",c.multiply())
print("兩數相除為",c.divide())

