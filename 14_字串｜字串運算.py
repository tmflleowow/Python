#字串
ch = ""       #空字串
st = "dog"    #字串


#解包
'''分別指定'''
x,y,z = "abc"

'''只要頭尾'''
x,_,z = "abc"

'''剩下的給中間'''
x,*y,z = "abcde"



#重複
s = "abc" * 3
print("s = {}".format(s))




#比較
c = "cat"
d = "dog"
C = "Cat"

print(c <  d)
print(c <= d)
print(c == d)
print(c != d)
print(c >= d)
print(c >  d)

#字母相同時會以ASCII CODE 比較大小
print(c < C)
print()


#相接

print("abc" + "def")
print()


#包含
print("abc" in "abcd")
print("abc" in "abs")
print("abc" in "Abc")



