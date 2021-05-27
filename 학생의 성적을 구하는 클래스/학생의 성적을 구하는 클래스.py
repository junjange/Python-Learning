class Score(object):
    def __init__(self, name, middle, end, assignment):
        self.name = name
        self.middle = middle
        self.end = end
        self.assignment = assignment

    def name_print(self):
        print("학생의 이름은 {0} 입니다.".format(self.name))

    def total_print(self):
        print("{0} 학생의 총점은 {1}점 입니다.".format(self.name, self.middle + self.end + self.assignment))

    def average_print(self):
        print("{0} 학생의 평균은 {1} 입니다.".format(self.name, (self.middle + self.end + self.assignment)/3))


A = Score("조준장", 90, 80, 70)


A.name_print()
A.total_print()
A.average_print()