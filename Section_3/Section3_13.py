# 文字のメソッド
s = 'My name is Mike. Hi Mike'
print(s)

is_start = s.startswith('My')
                    # 文字が'My'から始まるか
print(is_start)
is_start = s.startswith('X')
                    # 文字が'X'から始まるか
print(is_start)

print('----------------------')
print(s.find('Mike'))
                    # 文字列の先頭から探して、最初に'Myke'が見つかる場所
print(s.rfind('Mike'))
                    # 文字列の後ろから探して、最初に'Myke'が見つかる場所
print(s.count('Mike'))
                    # 文字列の中に'Myke'が何回入っているか
print('----------------------')
print(s.capitalize())
                    # 文字列の先頭だけ大文字にする
print(s.title())    # 文字列の各単語を大文字にする
print(s.upper())    # 文字列の各文字を大文字にする
print(s.lower())    # 文字列の各文字を小文字にする
print(s.replace('Mike','Nancy'))
                    # 文字列の'Myke'を'Nancy'に置き換える
