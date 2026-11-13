from baseball_utils import *

MAX_TRY = 20

answer = make_answer()

tries = 0
win = False
print("⚾숫자 야구! 1~9의 서로 다른 숫자 3개를 맞혀보세요")

while tries < MAX_TRY:
    text = input(f"{tries+1}/{MAX_TRY} 세자리 수:")
    error = check_input(text)
    if error != '':
        print(error)
        continue # 횟수는그대로, 다시입력
    tries += 1
    guess = to_number(text)
    strike = count_strike(answer, guess)
    ball = count_ball(answer, guess)
    print(' →', result_text(strike, ball))
    if strike == 3:
        win = True
        break

if win:
    print('정답!', tries, '번만에맞혔습니다.')
else:
    print('실패! 정답은', answer)