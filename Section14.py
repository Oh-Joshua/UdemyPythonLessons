# Section 14 文字の代入
Aisatsu  = 'a is {}'.format('a')
                    # formatメソッド:文字列に代入する
print(Aisatsu)

Aisatsu  = 'a is {}'.format('test')
                    # formatメソッド:文字列に代入する
print(Aisatsu)

Aisatsu  = 'a is {} {} {}'.format('First','Second','Third')
                    # formatメソッド:文字列に代入する
print(Aisatsu)

Aisatsu  = 'a is {0} {1} {2}'.format('First','Second','Third')
                    # 代入する時にインデックスを使う
print(Aisatsu)

Aisatsu  = 'a is {2} {1} {0}'.format('First','Second','Third')
                    # インデックスを逆に設定する
print(Aisatsu)

Aisatsu  = 'My name is {0} {1}\nWatashi ha {1} {0} desu'.format('Michael','Jackson')
                    # インデックスを逆に設定する
print(Aisatsu)

Aisatsu  = 'My name is {name} {family}\nWatashi ha {family} {name} desu'.format(name='Michael',family='Jackson')
                    # インデックスをシンボルにする
print(Aisatsu)

str1 = str(1)       # str()関数で数値を文字列に型変換できる
print(str1)
print(type(str1))
str2 = str(True)    # Booleanも文字列に型変換できる
type(str2)
print(type(str2))
