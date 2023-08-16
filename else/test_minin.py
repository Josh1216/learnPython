from test_class import Game
inBlood = input("輸入血量: ")
inAtk = input("輸入攻擊力: ")
minin = Game()
minin.set_blood(inBlood); minin.set_atk(inAtk)
print("血量為:", minin.showB(),"攻擊力為: ", minin.showA())