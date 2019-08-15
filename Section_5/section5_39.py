# 39. while文
print('===============================')
print('Section 5_39')
print('---------------')
count = 0
# while count < 5:
#     print(count)
#     count += 1
#
while True:
    if (count >= 5):
        print('Break')
        break               # ループを抜ける
    if (count == 2):
        print('Now Count 2')
        count += 1
        continue            # ループの先頭にジャンプする
    print(count)
    count += 1


# 40. while else文
print('===============================')
print('Section 5_40')
print('---------------')

count = 0
while count < 5:
    if count == 2:
        break               # breakするとelseは通らない
    print(count)
    count += 1
else:                       # whileの最後に動く
    print('Done')

# 41. input関数
print('===============================')
print('Section 5_41')
print('---------------')

while True:
    word = input('Enter:')
    if word == 'ok':
        break
    print('next')
