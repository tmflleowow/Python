#變數
'''
變數的四個定義
1.名稱
2.內容值
3.起始地址
4.記憶體大小
'''

#關鍵字
import keyword
keyword.kwlist


#數值的型態
x = 1
type(x)

#變數的地址
x = 1
id(x)

#python 中數值一樣的變數會其用同一份記憶體
x = y = 1
id(x)
id(y)

#取得變數空間大小
import sys
x = 2
sys.getsizeof(x)

#python會自動重新分配空間
x = 18
sys.getsizeof(x)
x += 2000000000
sys.getsizeof(x)


