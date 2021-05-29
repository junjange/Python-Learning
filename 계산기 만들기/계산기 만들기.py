from tkinter import *
from math import * # 삼각함수를 표현하기 위해 수학 모듈 사용

# 윈도우 객체 정의
window = Tk()
window.title("계산기 만들기")

# Entry 위젯 정의
e = Entry(window, width=40, bg="black", fg="white", bd=5)
e. grid(row=0, column=0, columnspan=5)

# 버튼 목록의 초기화
buttons = ['0', '1', '2', 'sin', '+', '%',
           '3', '4', '5', 'cos', '-', '//',
           '6', '7', '8', 'tan', '*', '**',
           '9', '.', '=', 'log', '/', 'C']

row = 1 # 버튼의 행
col = 0 # 버튼의 열

# 클릭 이벤트 처리
for char in buttons:
    # 어떤 버튼이 클릭 되었는지 확인
    def click(key = char):

        # 지금까지 입력한 문자열들을 eval() 함수의 매개변수로 정의해 결과값 계산
        if key == '=':
            result = eval(e.get())
            s = str(result)
            e.delete(0, END)
            e.insert(0, s)

        # delete() 함수로 삭제
        elif key == 'C':
            e.delete(0, END)

        # 지금까지 입력한 문자열들을 eval() 함수의 매개변수로 정의해 결과값을 sin()으로 계산
        elif key == "sin":
            result = eval(e.get())
            s = str(sin(result))
            e.delete(0, END)
            e.insert(0, s)
        # 지금까지 입력한 문자열들을 eval() 함수의 매개변수로 정의해 결과값을 cos()으로 계산
        elif key == "cos":
            result = eval(e.get())
            s = str(cos(result))
            e.delete(0, END)
            e.insert(0, s)
        # 지금까지 입력한 문자열들을 eval() 함수의 매개변수로 정의해 결과값을 tan()로 계산
        elif key == "tan":
            result = eval(e.get())
            s = str(tan(result))
            e.delete(0, END)
            e.insert(0, s)
        # 지금까지 입력한 문자열들을 eval() 함수의 매개변수로 정의해 결과값을 log()로 계산
        elif key == "log":
            result = eval(e.get())
            s = str(log(result))
            e.delete(0, END)
            e.insert(0, s)

        # 클릭한 것을 계속해서 뒤에 넣는다.
        else:
            e.insert(END, key)

    # 버튼 위젯 초기화
    b = Button(window, text=char, width=7, height=3, command=click)
    b.grid(row=row, column=col)
    col += 1

    # 열인 col 변수의 값이 6이 되면, 한 행이 버튼 6개로 꽉찼음을 의미
    # 다음 행으로 가기 위해 변수 row를 1 증가시키고, 변수 col은 0으로 초기화
    if col > 5:
        row += 1
        col = 0

window.mainloop()
