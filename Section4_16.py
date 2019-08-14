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
