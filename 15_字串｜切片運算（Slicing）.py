#切片運算
#公式[start , end , step] => 會取[start] - [end - 1],每隔step個的字元
s = "abcdefghij"

#單一
print(s[0])

#範圍
print(s[2 : 7])   #實際上是由[2 - 6]

#從後面開始
print(s[-6 : -3]) #最左邊系-10 最右邊系-1

#省略終點代表去到底
print(s[2:])

#省略起點代表由頭開始
print(s[:7])


#從[2]到[6],每隔幾個字元取1次
print(s[2:7:2])

#切片模版
sc = slice(3, 12, 3)
print(s[sc])
