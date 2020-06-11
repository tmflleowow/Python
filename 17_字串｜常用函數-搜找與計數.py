#搜找與計數


#從前找到後
#找不到會回傳-1
print("This is a book".find("is"))

#找不到會回傳 ValueError
print("This is a book".index("is"))

#從後找到前

#找不到會回傳-1
print("This is a book".rfind("is"))

#找不到會回傳 ValueError
print("This is a book".rindex("is"))

#是否由特定字眼開頭
print("This is a book".startswith("This"))

#是否由特定字眼結尾
print("This is a book".endswith("book"))

#計算該文字的出現次數
print("This is a book".count("is"))

