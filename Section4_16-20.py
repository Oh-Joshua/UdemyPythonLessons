# Section4:データ構造
# 16.リスト型
l = [1, 20, 4, 50, 2, 1, 2]
                    # リストは文字列と同じ考え方
print(l)            # リスト全体を表示
print(l[0])         # リストの先頭
print(l[-1])        # リストの最後
print(l[0:2])       # リストの0番目～2番目
print(l[:2])        # 0:は省略できる
print(l[2:5])       # 2~5番目
print(l[2:])        # 2以降
print(len(l))       # リストの要素数
print(type(l))      # Typeを見てみる

print('-----------------------------------')

n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(n[::2])       # リストから一つ飛ばしに取り出す
nn = n[1::2]        # リストの２番目から一つ飛ばしに取り出す
print(nn)
print(n[::-1])      # リストの後ろから取り出す

print('-----------------------------------')
# ネストした配列
a = ['a', 'b', 'c'] # 文字のリスト
n = [1, 2, 3]       # 数字のリスト
x = [a, n]          # 二つのリストをリストにする
print(x)
print(x[0])
print(x[0][1])      # リスとの要素を取り出す

print('-----------------------------------')
l = {1, 20, 4, 50, 2, 1, 2}
print(l)

# 17.リストの操作
s = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(s)
s[0] = 'X'          # リストの要素は書き替え可能（文字列は書き替え不可）
print(s)
s[2:5] = ['C', 'D', 'E']
                    # リストの要素は書き替え可能（文字列は書き替え不可）
print(s)
s[2:5] = []         # リストの要素を空にすることができる
print(s)
print(type(s))
s[:] = []           # リスト全体を空にする
print(s)

# リストのメソッドを使って操作する
print('-----------------------------------')
n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(n)
n.append(100)       # append:リストの最後に追加
print(n)
n.insert(0,200)     # insert:リストの中に追加
print(n)
nn = n.pop()        # pop:リストの最後の要素を取り出す
print(nn)           # 取り出した値を表示
print(n)            # 取り出した後のリストを表示
nn = n.pop(0)       # pop:リストの先頭の要素を取り出す
print(nn)           # 取り出した値を表示
print(n)            # 取り出した後のリストを表示
print('-----------------------------------')
a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]
print(a)
print(b)
x = a + b
print(x)
a += b              # 二つのリストをつなげる
print(a)
a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]
a.extend(b)         # extend:リスとをつなげる
print(a)

#18.リストのメソッド
print('===================================')
r = [1, 2, 3, 4, 5, 1, 2, 3]
print(r.index(3))   # index:リストの中で3がある場所を返す
print(r.index(3, 3))
                    # index:リストの3番目以降で3がある場所を捜す
print(r.index(1, 2))
                    # index:リストの2番目以降で1がある場所を捜す
print(r.count(3))   # count:3の件数をカウントする

if 5 in r:          # もし、rのリスとに5がある場合
    print('exist')

if 100 in r:        # もし、rのリスとに100がある場合
    print('exist')

r.sort()            # リストrの要素をソートする
print(r)
r.sort(reverse=True)
                    # リストrを逆順にそーとする
print(r)
r.reverse()         # reverse:リストrを逆に並べる
print(r)

print('-----------------------------------')
a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]
print(a)
print(b)
x = a + b
print(x)

x.reverse()
print(x)

# ネストした配列
a = ['a', 'b', 'c'] # 文字のリスト
n = [1, 2, 3]       # 数字のリスト
x = [a, n]          # 二つのリストをリストにする
print(x)
a.reverse()
n.reverse()
x = [a, n]          # 二つのリストをリストにする
print(x)
# ネストした配列
x = [a, n]          # 二つのリストをリストにする

s = 'My name is Mike'
                    # 文字列を定義する
to_split = s.split(' ')
                    # 区切り文字' 'でリストに代入する
print(s)
print(to_split)

x = ' '.join(to_split)
                    # 区切り文字' 'でリストを結合する
print(x)
x = '----'.join(to_split)
                    # 区切り文字'----'でリストを結合する
print(x)

# print(help(list))   # help関数でリストのヘルプを表示できる

# 19.リストのコピー
print('===================================')
i = [1, 2, 3, 4, 5] # リストiを作る
j = i               # リストjにiをコピーする
print('i = ', i)
print('j = ', j)
# iの最初を100に書き換えると、jの最初も書き換わる
# iのポインターを渡しているため
i[0] = 100
print('i = ', i)
print('j = ', j)

print('-----------------------------------')
x = [1, 2, 3, 4, 5] # リストxを作る
y = x.copy()        # リストの要素をコピーする
y = x[:]            # リストの要素をコピーする(この書き方でも同じ動きになる# )
y[0] = 100          # リストyの0番目に100を代入する
print('x = ', x)    # xの値は変らない
print('y = ', y)    # yの値だけ変わる

# リストの値渡しと参照渡し
X = 20
Y = X               # 数値データの場合、値を代入する
print(X)
print(Y)
Y = 5
print(X)
print(Y)

# XとYは、違うobjectになっている
print(id(X))
print(id(Y))

X = ['a', 'b']
Y = X               # 配列の場合、object参照を渡す
Y[0] = 'p'
print(X)
print(Y)
# XとYは同じobjectになっている
print(id(X))
print(id(Y))
