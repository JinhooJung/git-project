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

credit_submit = credit_open = 0
grade_submit = grade_open = 0.0
subject_dict = {}
subject_list = []
subject_count = 10000

while(True):
    print("\n작업을 선택하세요.\n1. 입력\n2. 출력\n3. 계산")
    work=input()

    if work=='1' :
        subject_dict[subject_count], credit, temp_grade, list = inputting()
        subject_count += 1
        grade = get_grade(temp_grade)
        subject_list.append(list)

        if grade > 0.0:
            credit_submit += int(credit)
            credit_open += int(credit)
            grade_submit += grade * int(credit)
            grade_open += grade * int(credit)
        else:
            credit_open += int(credit)
            grade_open += grade * int(credit)

    elif work=='2':
        n = len(subject_list)
        count = 0

        for i in range(n):
            print('[', subject_dict[subject_list[count][0]], '] ', subject_list[count][1], '학점: ', subject_list[count][2], sep='')
            count += 1

    elif work=='3':
        print("제출용: ", credit_submit, "학점 (GPA:", grade_submit / credit_submit, ")", sep="")
        print("열람용: ", credit_open, "학점 (GPA:", grade_open / credit_open, ")", sep="")
        print("\n프로그램을 종료합니다.")

        break