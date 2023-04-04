#디버깅 할때는 확실한 부분을 지우면서 틀린 부분을 찾아나가 수정한다.
answer1, answer2, answer3 = 1, 5, 9

for i in range (0, 10):
    strike, ball = 0, 0
    value1 = input()
    value2 = input()
    value3 = input()
    value1 = int(value1)
    value2 = int(value2)
    value3 = int(value3)

    if answer1 == value1:
        strike += 1
    else:
        ball += 1
    if answer2 == value2:
        strike += 1
    else:
        ball += 1
    if answer3 == value3:
        strike += 1
    else:
        ball += 1

    if strike == 3:
        print("Correct")
        break
    else:
        print(strike, " Strikes And ", ball, " Balls", sep="")
        if i == 9:
            print("\nYou Fail")

