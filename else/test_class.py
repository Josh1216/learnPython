
class Email:
    def set_address(self,address):
        print(address)
    def set_name(self,firstName,lastName):
        print(firstName+lastName)

# toTaichungMail = Email()
# toTaichungMail.set_address("台中市西屯區")
# toTaichungName = Email()
# toTaichungName.set_name("小憨","包")

class Game:
    def set_blood(self,b1):
        self.blood = b1
    def set_atk(self,a1):
        self.atk = a1
    def showB(self):
        return self.blood
    def showA(self):
        return self.atk
if __name__ == "__main__" :
    inBlood = input("輸入血量: ")
    inAtk = input("輸入攻擊力: ")
    minin = Game()
    minin.set_blood(inBlood); minin.set_atk(inAtk)
    print("血量為:", minin.showB(),"攻擊力為: ", minin.showA())
