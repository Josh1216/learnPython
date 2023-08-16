from connect import initial,servo_on,servo_off,end,designatedLocation

try:
    master = initial()
    while True:
        userInput = input("請輸入1為伺服啟動, 2為伺服關閉, 3為原點賦歸, 4為再輸入移動位置, 5為離開程式: ")
        if userInput == '1':
            servo_on(master)
        elif userInput == '2':
            servo_off(master)
        elif userInput == '3':
            print("原點賦歸")
        elif userInput == '4':
            loctionIn = input("請輸入位置: ")
        elif userInput == '5':
            end(master)
            break
        else:
            print("請重新輸入,1為伺服啟動,2為伺服關閉,3為原點賦歸,4為再輸入移動位置,5為離開程式: ")
except:
    print("eRRoR")