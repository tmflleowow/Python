#証明IEEE 754格式
print(float.hex(53.234375))

# 0.1 + 0.2 != 0.3
if 0.1 + 0.2 != 0.3:
    print("Yes")
else:
    print("No")

#除錯
if abs((0.1 + 0.2) - 0.3) < 0.000001:
    print("Yes")
else:
    print("No")


#無誤差函數
#char Decimal(int)
#char Decimal("int" / 'int')
    
import decimal
decimal.Decimal('0.1')

from decimal import *
Decimal("0.1")

#將數值轉換成Float
float(Decimal("0.1") + Decimal("0.2"))

#Python的預設精準度為小數點後28個位
from decimal import *
Decimal(2) / Decimal(3)


#取得目前的精準度
#getcontext()

#更變目前的精準度
#getcontext().prec = 2  <==小數點後2位
