#取代,去除,分割,接合

#取代
print("This is a book".replace("book" , "cat"))

#去除
#去除字串中的左右兩則的空白
print(" This is a book ".strip())

#分割
#常用作分開CSV檔的欄位
print("This is a book".split(" "))

#接合
s = "This is a book".split(" ")
"-".join(s)
