#計算黃金牛排克數
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
goldCount = GoldOz()
steakCount = SteakOz()
num =input("請輸入幾oz")
goldCount.set_oz(num)
steakCount.set_oz(num)
print("以黃金算法為",goldCount.get_gram(),"G")
print("以牛排算法為",steakCount.get_gram(),"G")