# 文字列の勉強

print('Hello')              # 文字列はシングル・クォート
print("Hello")              # ダブル・クオートもＯＫ

print("I don't know")       # ダブル・クォートの中にシングル・クオートが入れられる
print('I don\'t know')      # エスケープは'\'
print('say "I don\'t know"')
                            # シングル・クオートの中にダブル・クオートを入れられる
print("say \"I don\'t know\"")
                            # ダブル・クオートの中でダブル・クオートを使うときは、エスケープする
print('Hello.\nHow are you?')
                            # 改行は'\n'
print(r'C:\name\name')
                            # \nを文字列としｔ表示したいときは、"raw"の'r'を先頭につける
print("""
Hello
I am
Yoshu
Ohashi
""")                        # 複数行を改行して出力するには、"""ダブル・クオートを３つつなげる

# 複数行出力には、前後に空白行が出力される
print("#################")
print("""
line1
line2
line3
""")
print("#################")

# \を入れると、空白行は出ない
print("#################")
print("""\
line1
line2
line3\
""")
print("#################")

# 同じ文字を３回出力することができる
print('Hi.' * 3)

str = 'Hi.' * 5
print(str)
                        # 文字列を掛け算することもできる
str = str + 'Yoshu'
print(str)
                        # 文字列を足すこともできる

str2 = 'Py' 'thon'
print(str2)
                        # 文字列の結合は、並べるだけでもよい
str2 = ('Py' 'thon')
print(str2)
                        # かっこで括ろと見やすい
str2 = ('Py'
        'thon')
print(str2)
                        # かっこで括ろと複数行に分かれて結合できる
