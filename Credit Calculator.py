class Subject:
    def __init__(self):
        self.credit_open = self.credit_submit = self.grade_open = self.grade_submit = 0
        self.subject_dict = {}
        self.subject_list = []
        self.subject_count = 10000

    def get_grade(self, gpa):
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

    def inputting(self):
        print("과목명을 입력하세요:")
        name = input()
        print("학점을 입력하세요:")
        credit = input()
        print("평점을 입력하세요:")
        grade = input()
        print("입력되었습니다")

        return name, credit, grade

    def retake(self, code, credit, origin_grade, new_grade):
        # 재수강 시 원래 학점과 입력받은 학점을 비교하여 더 높은 학점과 학점 변화율을 반환해줌
        if self.get_grade(origin_grade) > self.get_grade(new_grade):
            grade = origin_grade
        else:
            grade = new_grade

        return (code, credit, grade)

    def plus_calculate(self, credit, grade):
        if grade != 'F':
            self.credit_open += int(credit)
            self.credit_submit += int(credit)
            self.grade_open += self.get_grade(grade) * int(credit)
            self.grade_submit += self.get_grade(grade) * int(credit)
        else:
            self.credit_open += int(credit)
            self.grade_open += self.get_grade(grade) * int(credit)

    def minus_calculate(self, credit, grade):
        if grade != 'F':
            self.credit_open -= int(credit)
            self.credit_submit -= int(credit)
            self.grade_open -= self.get_grade(grade) * int(credit)
            self.grade_submit -= self.get_grade(grade) * int(credit)
        else:
            self.credit_open -= int(credit)
            self.grade_open -= self.get_grade(grade) * int(credit)

    def input_process(self):
        self.subject_dict[self.subject_count], credit, grade = self.inputting()

        # 입력받은 과목명이 같은 지 아닌 지 판단한 후 retake 함수를 통해 학점을 비교하고 학점이 더 높아졌다면 오른 점수만큼 저장
        for i in range(len(self.subject_list)):
            if self.subject_dict[self.subject_count] == self.subject_dict[self.subject_list[i][0]]:
                new_list = self.retake(self.subject_count, credit, self.subject_list[i][2], grade)

                self.minus_calculate(self.subject_list[i][1], self.subject_list[i][2])
                self.plus_calculate(new_list[1], new_list[2])

                del self.subject_dict[self.subject_list[i][0]]
                self.subject_list.remove(self.subject_list[i])
                self.subject_list.append(new_list)

                self.subject_count += 1

                return


        # 입력받은 과목명이 같지 않다면 새로 list에 저장
        self.subject_list.append((self.subject_count, credit, grade))
        self.subject_count += 1
        self.plus_calculate(credit, grade)

    def output_process(self):
        for i in range(len(self.subject_list)):
            print('[', self.subject_dict[self.subject_list[i][0]], '] ', self.subject_list[i][1], '학점: ',
                  self.subject_list[i][2], sep='')

    def check_process(self):
        check_subject = input("과목명을 입력하세요\n")
        is_exist = False

        for i in range(len(self.subject_list)):
            if check_subject == self.subject_dict[self.subject_list[i][0]]:
                is_exist = True
                print('[', self.subject_dict[self.subject_list[i][0]], '] ', self.subject_list[i][1], '학점: ',
                      self.subject_list[i][2], sep='')
        if is_exist == False:
            print("해당하는 과목이 없습니다.")

    def calculate_process(self):
        print("제출용: ", self.credit_submit, "학점 (GPA:", self.grade_submit / self.credit_submit, ")", sep="")
        print("열람용: ", self.credit_open, "학점 (GPA:", self.grade_open / self.credit_open, ")", sep="")

    def end_process(self):
        print("\n프로그램을 종료합니다.\n")

        exit()


subject = Subject()

while True:
    print("\n작업을 선택하세요.\n1. 입력\n2. 출력\n3. 조회\n4. 계산\n5. 종료")
    work = input()

    if work == '1':
        subject.input_process()
    if work == '2':
        subject.output_process()
    if work == '3':
        subject.check_process()
    if work == '4':
        subject.calculate_process()
    if work == '5':
        subject.end_process()
