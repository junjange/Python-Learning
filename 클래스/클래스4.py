# 연습문제 2

class MaxLimitCalculator(Calculator):
    def add(self, val):
        super().add(val)
        if self.value >= 100:
            self.value = 100


cal = MaxLimitCalculator()

cal.add(50)
print(cal.value)

cal.add(60)
print(cal.value)