class ListCalculate:
    def __init__(self, lst):
        self.list_data = lst

    def add_1(self):
        new_list = []
        for num in self.list_data:
            new_list.append(num + 1)
        return new_list

a = [1, 5, 8, 10]
cal = ListCalculate(a)
b = cal.add_1()
print(b)