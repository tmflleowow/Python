#讀取指令 intput("提示文字")
#input() 讀入的數據一律以字串方式回傳


'''
name = input("Input your name:")
print(name)
'''

#回傳值型態轉換
'''
print("Please Input X and Y")
x = int(input("x :"))
y = int(input("y :"))
print("{} + {} = {}" . format(x , y , x + y))
'''

#自動轉為合適的型態
#eval()
'''
print("Please Input X and Y")
x = eval(input("x :"))
y = eval(input("y :"))
print("{} + {} = {}" . format(x , y , x + y))
'''

#OP寫法
expression = input("輸入一個公式")
print(expression , " = " , eval(expression))
