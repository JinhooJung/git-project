credit_submit = 0
credit_open = 0
grade_submit = 0.0
grade_open = 0.0
count_submit = 0
count_open = 0

while(True):
    print("작업을 선택하세요.\n1. 입력\n2. 계산")
    work=input()

    if work=='1' :
        print("학점을 입력하세요:")
        credit=input()
        print("평점을 입력하세요:")
        grade=input()
        print("입력되었습니다")

        match grade:
            case 'A+':
                grade1 = 4.5
            case 'A':
                grade1 = 4.0
            case 'B+':
                grade1 = 3.5
            case 'B':
                grade1 = 3.0
            case 'C+':
                grade1 = 2.5
            case 'C':
                grade1 = 2.0
            case 'D+':
                grade1 = 1.5
            case 'D':
                grade1 = 1.0
            case 'F':
                grade1 = 0.0
                credit_submit -= int(credit)
                grade_submit -= grade1
                count_submit -= 1

        credit_submit += int(credit)
        credit_open += int(credit)
        grade_submit += grade1
        grade_open += grade1
        count_submit += 1
        count_open += 1

    elif work=='2':
        print("제출용: ", credit_submit, "학점 (GPA:", grade_submit / count_submit, ")", sep="")
        print("열람용: ", credit_open, "학점 (GPA:", grade_open / count_open, ")", sep="")
        print("\n프로그램을 종료합니다.")

        break