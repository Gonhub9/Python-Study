import random
TRY = 0
baseball = random.sample(range(0, 10), 3)

while True:
    A, B, C = map(int, input().strip().split(' '))
    TRY += 1
    print(f"{TRY}번째 시도 : {A}{B}{C}")

    Ball = 0
    Strike = 0

    if baseball[0] == A:
        Strike += 1
    if baseball[1] == B:
        Strike += 1
    if baseball[2] == C:
        Strike += 1

    if A in baseball and baseball[0] != A:
        Ball += 1
    if B in baseball and baseball[1] != B:
        Ball += 1
    if C in baseball and baseball[2] != C:
        Ball += 1

    print(f"{Ball}B{Strike}S")

    if Strike == 3:
        print('게임을 종료합니다.')
        break