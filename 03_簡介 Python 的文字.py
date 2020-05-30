#字串
'''
英文:ASCII
繁中:BIG5
簡中:GB
全球:Unicode
'''

#用" " , ' '包住就可以
'''
ASCII
48 = 0 +17
65 = A +32
97 = a
'''

#ord(char)
#查字元的ASCII CODE
ord("A")

#chr(int)
#查ASCII CODE的字元
chr(65)

# "一" Big5的編碼    @ = 40
"一".encode("big5")

#反轉由代碼找出文字 b'\xa4@'.decode("big5")
b'\xa4@'.decode("big5")

#GB = "阿".encode("gb2312")
"阿".encode("gb2312")

#Unicode  = "我".encode("utf-8")


#字串長度  len("你好")
len("你好")
