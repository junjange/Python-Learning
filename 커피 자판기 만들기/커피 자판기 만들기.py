from tkinter import *

# 윈도우 객체 정의
window = Tk()
window.title("커피자동주문기")

# Entry 위젯 정의
e = Entry(window, width=60, bg="black", fg="white", bd=5)
e.grid(row=0, column=0, columnspan=3)

# 버튼 목록의 초기화
buttons = ['아메리카노\n(핫)', '카페라떼\n(핫)', '카푸치노\n(핫)',
           '아메리카노\n(아이스)', '카페라떼\n(아이스)', '카푸치노\n(아이스)',
           '핫초코', '주문', '지움']

row = 1 # 버튼의 행
col = 0 # 버튼의 열

# 클릭 이벤트 처리
for char in buttons:
    # 어떤 버튼이 클릭 되었는지 확인
    def click(key = char):

        # 지금까지 입력한 문자열들을 eval() 함수의 매개변수로 정의해 결과값 계산
        if key == '주문':
            result = eval(e.get())
            s = str(result)
            e.delete(0, END)
            e.insert(0, s)

        # delete() 함수로 삭제
        elif key == '지움':
            e.delete(0, END)

        # Entry 값이 있으면 이미 있는 값에서 더하기를 해야하기 때문에 +가격을 출력
        # 없으면 가격만 출력
        elif key == '아메리카노\n(핫)':
            if e.get():
                e.insert(END, "+3000")
            else:
                e.insert(END, "3000")

        elif key == '핫초코':
            if e.get():
                e.insert(END, "+3000")
            else:
                e.insert(END, "3000")

        # 아메리카노와 핫초코를 뺀 나머지는 가격이 동일하다.
        else:
            if e.get():
                e.insert(END, "+4000")
            else:
                e.insert(END, "4000")


    # 버튼 위젯 초기화
    b = Button(window, text=char, width=20, height=3, command=click)
    b.grid(row=row, column=col)
    col += 1

    # 열인 col 변수의 값이 3이 되면, 한 행이 버튼 3개로 꽉찼음을 의미
    # 다음 행으로 가기 위해 변수 row를 1 증가시키고, 변수 col은 0으로 초기화
    if col > 2:
        row += 1
        col = 0

window.mainloop()
