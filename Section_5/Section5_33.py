# 33. if文
print('===============================')
print('---------------')

x = 100

if x < 0:
    print('negative')
elif x == 0:
    print('zero')
else:
    print('positive')

# ifの中にifを入れられる
a = 10
b = 20
if a > 0 :
    print('a is positive')
    if b > 0:
        print('b is positive')

# 34.論理演算子
if a > 0 and b > 0 :
    print('a and b is positive')

if a > 0 or b > 0 :
    print('a or b is positive')

# 36. in と not の使い方
print('===============================')
print('---------------')
y = [1, 2, 3]
x = 1

if x in y:
    print('in')

if 100 not in y:
    print('not in')

#  boolean をnotで否定すると、パイソンらしいコードになる
is_ok = False

if not is_ok:
    print('It\'s not OK.')

# 38. None を判定する場合
print('===============================')
print('---------------')

is_empty = None
print(is_empty)
