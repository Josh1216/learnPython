
def yoloo(a,b,choose):
    if choose == "1":
        x=a-b
        return x
    elif choose == "2":
        y=a+b
        return y
    else:
        choose=input("請重新輸入1或2: ")
        yoloo(a,b,choose)

num1=int(input("輸入數字1: "))
num2=int(input("輸入數字2: "))
cho3=input("輸入1為n1-n2,2為n1+n2: ")
www=yoloo(num1,num2,cho3)
print(www)