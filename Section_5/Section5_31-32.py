# 31.コメント
print('===============================')
print('---------------')
# シャープを入れるとコメントになる
"""
ダブルクォートをで囲むと、２行以上のコメントが書ける
"""

# パイソン的には、コメントはソース行の前に入れる
Apple_Price = 100           # リンゴの値段
                            # リンゴの値段
print(Apple_Price)


# 32.行が長くなる時
print('===============================')
print('---------------')

S = \
    'aaaaaaaaaaaaaaaa' + \
    'bbbbbbbbbbbbbbb'
print(S)

# Python的には一行は80文字。超えるときには改行する
#234567890#234567890#234567890#234567890#234567890#234567890#234567890#234567890

# ()で括ってもよい。
s = (
        'aaaaaaaaaaaaaaaa' +
        'bbbbbbbbbbbbbbb'
    )
print(s)
