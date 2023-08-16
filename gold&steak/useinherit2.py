#選擇print黃金or牛排克數 輸入1為黃金 輸入2為牛排
class OzToGram:
    def set_oz(self,oz):
        self.value = int(oz)
class GoldOz(OzToGram):   #31g
    def get_gram(self):
        goldGram = self.value*31
        return goldGram
class SteakOz(OzToGram):   #28g
    def get_gram(self):
        steakGram = self.value*28
        return steakGram
while True:
    stOrgo = input("輸入1為黃金算法,輸入2為牛排算法: ")
    if stOrgo == "1": #使用黃金算法
        ozTogram = GoldOz()
        break
    elif stOrgo == "2": #使用牛排算法
        ozTogram = SteakOz()
        break
num =input("請輸入幾oz: ")
ozTogram.set_oz(num)
print("為",ozTogram.get_gram(),"克")



