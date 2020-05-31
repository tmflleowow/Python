#迴圈簡介
'''
迴圈的種類
while X <= 10:
    ...
    ...

for i in range(1, 11 , 1):
    ...
    ...
    

'''
#While迴圈
'''
x = 0
while x < 10:
    print("----------")
    x+=1
else:
    print(x)
'''

#隨機生成數字
'''    
import random

x = random.randint(1, 6)
while x != 6:
    print(x)
    x = random.randint(1, 6)
else:
    print(x)
'''

#猜數字遊戲
'''
import random
pc = random.randint(1 , 100)
player = eval(input("輸入1個數字"))

while player != pc:
    if player > pc:
        print("有點大哦")

    elif player < pc:    
        print("有點小哦")
        
    player = eval(input("輸入1個數字"))

else:
    print("你猜中了哦!")
'''

#for迴圈
for i in range(10):
    print(i)

#range(起始值,終點值,遞增遞減值)
range(5) # 0 - 4

#巢狀迴圈
for i in range(10):
    for j in range(10):
        print("{}x{}={}".format(i + 1 , j + 1 , (i + 1)*( j + 1)) , end = " ")
    print("\n")


#break continue

#break
    '''
pc_ac = "Leo"
pc_pw = 12345
while True:
    user_ac = input("輸入帳號:")
    user_pw = eval(input("輸入密碼:"))
    if (pc_ac == user_ac) and (pc_pw == user_pw):
        break
    else:
        print("Retry")
print("歡迎光臨")    
'''


#continue
for i in range(1 , 11):
    if i == 7:
        continue
    else:
        print("{}樓".format(i))










        
