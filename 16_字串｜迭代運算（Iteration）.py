#迭代運算

#用for  理由:簡單
'''
for c in "abcdefg":
    print(c, end = " ")
'''

#用iter() 理由:可自定迭代順序
iterator = iter("abcdefg")  # ==> ['a' , ''b' , 'c', ... , 'g']
for i in iterator:
    print(i)


#用enumerate() 理由:有索引值與內容
iterator = enumerate("abcdefg")
for i , j in iterator:
    print(i , j)
