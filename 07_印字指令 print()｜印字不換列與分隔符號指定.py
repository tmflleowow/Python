#印字指令 print()｜印字不換列與分隔符號指定


print("Processing, please wait")
print(".........")
print("DONE")


#令程式停頓
import time
print("Processing, please wait")
time.sleep(1)
print(".........")
time.sleep(1)
print("DONE")


#不換行輸出
#在輸出字串的後方加上end = " "
import time
print("Processing, please wait",end = " ")
time.sleep(1)
print(".........", end = " ")
time.sleep(1)
print("DONE")

#分割多批資料的顯示方法
#在輸出字串的後方加上 sep = "分開的字元"
print("台灣","香港","日本" , sep = " => ")


