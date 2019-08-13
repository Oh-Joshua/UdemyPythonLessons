# Pythonの基礎

## 変数
print('\n\n=== Program Start ===\n\n')
num = 1
name  = 'Myke'
is_ok = True

# print (num, type(num))
# print (name, type(name))
# print (is_ok, type(is_ok))
# print('\n')


name = '1'
new_num = int(name)
print ('new_num is ',new_num, type(new_num))

num2 = str(name)
print ('num2 is ',num2, type(num2))

## 演算
print('\n\n== Calc lesson')

print(17/3)         # 割り算
print(17//3)        # 商（整数部分）
print(17%3)         # 剰余（あまり）

print(5 ** 5)       # べき乗

pie = 3.14459216
print('Befor round:',pie)
print('Ater round',round(pie, 2))
                    # 有効桁数２桁で四捨五入

## 数学ライブラリの練習
print('\n\n== math lesson')

import math
result = math.sqrt(25)
                    # 平方根
print(result)

y = math.log2(10)
                    # 対数
print(y)

# ライブラリのヘルプを出力する関数：help
print(help(math))



