'''
# hangman 게임
- 단어의 각 글자 자리에 짧은 선이 그려진다.
- 글자 1개를 맞히면 글자가 표시되고, 추가로 계속 맞히면 글자가 표시됨.
- 틀리면 기회가 1번 줄어든다.
- 전체 글자를 입력하여 맞히면 프로그램 바로 종료됨
'''

import random

words = ['dog', 'cat', 'monkey', 'chicken', 'frog', 'horse']
lives_remaining = 10  # 남은 기회(전역 변수)

def pick_a_word():
    word = random.choice(words)
    return word

def get_guess():
    return 'a'   # 게이머가 항상 'a'를 추측한다고 가정

def process_guess(guess, word):
    global lives_remaining    # 지역변수인데 전역변수화 함(global)
    lives_remaining -= 1   # 기회가 1 줄어듦
    return False       # True를 반환하면 바로 종료

def paly():
    word = pick_a_word()
    while True:
        guess = get_guess()
        if process_guess(guess, word):       # 추측해서 맞혔을때
            print("You win! Well done!")
        else:   # 틀렸을 때
            print("You are Hung")
            print("The word was: " + word)
            break

play()
