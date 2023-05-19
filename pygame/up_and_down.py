# 숫자 추측 게임

'''
게임이 시작되면 컴퓨터가 난수(정답)을 생성한다
사용자의 추측값이 정답과 같으면 '정답!'
       추측값이 정답보다 크면  '너무 커요!'
       추측값이 정답보다 작으면 '너무 작아요!' 출력
'''

import random


# 컴퓨터의 난수 생성
min_v = 1
max_v = 50
com = random.randint(min_v, max_v)

for i in range(0, 10):
    guess = int(input(f"맞혀보세요([{i+1}회]{min_v}~{max_v}) > "))
    if guess > 50 or guess < 1:
        print('입력 범위가 아니에요. 다시 입력해 주세요')
    elif guess > com:
        print('너무 커요!')
        max_v = guess
    elif guess < com:
        print('너무 작아요!')
        min_v = guess
    elif guess == com:
        print(f"정답! {com}")
        break



