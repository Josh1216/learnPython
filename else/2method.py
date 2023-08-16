class ListLeave:
    def __init__(self, lst):
        self.list_data = lst
    def leave(self):
        new_list1=[]
        new_list2=[]
        count=0
        length_of_list =len(self.list_data)
        for i in self.list_data:            
            if count < length_of_list/2:
                new_list1.append(i)
            elif count >= length_of_list/2:
                new_list2.append(i)                
            count+=1
        return new_list1,new_list2       
a = [1, 5, 8, 10, 45, 43, 2, 4, 1, 4, 2, 4, 2, 32, 3, 3]
cal = ListLeave(a)
b = cal.leave()
print(b)