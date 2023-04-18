def get_grade(gpa):
    match gpa:
        case 'A+':
            return 4.5
        case 'A':
            return 4.0
        case 'B+':
            return 3.5
        case 'B':
            return 3.0
        case 'C+':
            return 2.5
        case 'C':
            return 2.0
        case 'D+':
            return 1.5
        case 'D':
            return 1.0
        case 'F':
            return 0.0


def inputting():
    print("과목명을 입력하세요:")
    name = input()
    print("학점을 입력하세요:")
    credit = input()
    print("평점을 입력하세요:")
    grade = input()
    print("입력되었습니다")

    return name, credit, grade, (subject_count, credit, grade)


def retake(origin_grade, new_grade, code, credit):
    # 재수강 시 원래 학점과 입력받은 학점을 비교하여 더 높은 학점과 학점 변화율을 반환해줌
    if get_grade(origin_grade) > get_grade(new_grade):
        grade = origin_grade
        changerate = 0
    else:
        grade = new_grade
        changerate = get_grade(new_grade) - get_grade(origin_grade)

    return (code, credit, grade), changerate


credit_submit = credit_open = 0
grade_submit = grade_open = 0.0
subject_dict = {}
subject_list = []
subject_count = 10000

while True:
    print("\n작업을 선택하세요.\n1. 입력\n2. 출력\n3. 계산")
    work = input()

    if work == '1':
        isoverlap = False
        subject_dict[subject_count], credit, grade, list = inputting()

        # 입력받은 과목명이 같은 지 아닌 지 판단한 후 retake 함수를 통해 학점을 비교하고 학점이 더 높아졌다면 오른 점수만큼 저장
        for i in range(len(subject_list)):
            if subject_dict[subject_count] == subject_dict[subject_list[i][0]]:
                new_list, changerate = retake(subject_list[i][2], grade, subject_list[i][0], credit)

                subject_list.remove(subject_list[i])
                subject_list.append(new_list)

                grade_submit += changerate * int(credit)
                grade_open += changerate * int(credit)

                isoverlap = True

        # 입력받은 과목명이 같지 않다면 새로 list에 저장
        if isoverlap == False:
            subject_count += 1
            subject_list.append(list)
            if get_grade(grade) > 0.0:
                credit_submit += int(credit)
                credit_open += int(credit)
                grade_submit += get_grade(grade) * int(credit)
                grade_open += get_grade(grade) * int(credit)
            else:
                credit_open += int(credit)
                grade_open += get_grade(grade) * int(credit)

    elif work == '2':
        count = 0

        for i in range(len(subject_list)):
            print('[', subject_dict[subject_list[count][0]], '] ', subject_list[count][1], '학점: ',
                  subject_list[count][2], sep='')
            count += 1

    elif work == '3':
        print("제출용: ", credit_submit, "학점 (GPA:", grade_submit / credit_submit, ")", sep="")
        print("열람용: ", credit_open, "학점 (GPA:", grade_open / credit_open, ")", sep="")
        print("\n프로그램을 종료합니다.")

        break
