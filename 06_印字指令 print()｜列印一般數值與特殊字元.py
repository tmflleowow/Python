#印字指令 print()｜列印一般數值與特殊字元
'''
sys.stdin -> program -> sys.stdout
input()                 print()
'''
print(123)
print(1.23)
print("ACB")
print(True)

print("C:\\new project\\refeernce")

'''
\n = new line
\r = carriage return
\t = tab
\100 = ASCII code(8進)
\x40 = ASCII code(16進)
'''

#印出原整字串  在字串前加上一個"r" (raw)
#壞處是字串中的所有特殊字元都會無效
print(r"C:\new project\refeernce")
