# 28.集合型
print('===============================')
print('---------------')

a = {1, 4, 5, 2, 3, 4, 4, 3, 5}
                    # {}で括った、キーのない辞書的なもの
print('集合a:', a)
print(type(a))

b  = {2, 3, 3, 6, 7}
print('集合b:', b)

print('a - b', a - b)        # 集合の引き算(重複する値を取り除く)
print('b - a', b - a)        # 集合の引き算(重複する値を取り除く)
print('a & b', a & b)        # 論理積(aにもbにもあるもの)
print('a | b', a | b)        # aまたはbにあるもの
print('a ^ b', a ^ b)        # 排他：aまたはbのどちらかにしかないもの

# 29.集合のメソッド
print('===============================')
print('---------------')
s = {1, 2, 3, 4, 5}
print(s)
s.add(10)                   # add:集合に値を追加する
print(s)
s.remove(3)                 # remove:集合から値を取り除く
print(s)


# 30.集合の使いどころ
# 自分の友達と他人の友達の共通点を見つける
print('===============================')
print('---------------')
my_friends = {'A', 'B', 'C', 'D'}
A_friends = {'X', 'Y', 'A', 'D'}
print(my_friends & A_friends)

fruits = ['Apple']          # fruitsのリストを作る
fruits.append('Banana')     # リストにフルーツを追加する
fruits.append('Orange')
fruits.append('Apple')
print(fruits)
fruits_set = set(fruits)    # fruits_setを集合にする
print(fruits_set)
