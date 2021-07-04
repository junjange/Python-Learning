# 커피 자판기 만들기

이전에 구현 했었던 계산기 프로그램을 참고하면서 커피자동주문기 버튼을 클릭하여 금액을 계산하는 GUI 프로그램을 구현해봤습니다. 프로그램 코드를 작성할 때 파트를 5개로 나누었고 순서대로 윈도우 객체 정의, Entry 위젯 정의, Button 위젯 정의, 클릭 이벤트 처리, mainloop() 메서드 순입니다. 그럼 이제 5가지 파트 순서대로 코드를 알아보고 결과 화면까지 실행시켜보도록 하겠습니다.  

## 1. 윈도우 객체 정의
<p align="center"><img src=https://blog.kakaocdn.net/dn/IRgrO/btq8MHLBwiW/bdKbK98NsAR87zNrUofseK/tfile.bmp
"></p>

tkinter 모듈을 내포하고, 윈도우 객체를 정의한다.
타이틀은 커피자동주문기로 만든다.
<p align="center"><img src=https://blog.kakaocdn.net/dn/eioCnd/btq8PuSH5xJ/hyTymO0WsIkWS5apxkNCP0/tfile.bmp
"></p>

위 사진처럼 타이틀은 프로그램 창에 제목이 된다.

## 2. Entry 위젯 정의

<p align="center"><img src=https://blog.kakaocdn.net/dn/dplNH3/btq8IEbUCSY/wOzVcFKbeIsI5p7kO99Lp0/tfile.bmp
"></p>

커피의 가격과 최종 결제 금액을 보여줄 Entry 위젯을 정의한다.
라벨의 너비(width)는 60으로, 라벨의 배경 색상(bg)은 black으로, 라벨의 문자열 색상(fg)은 white로, 라벨의 테두리두께(bd)는 5로 설정한다.
그리고 Entry 위젯을 윈도우에 배치할 때, 하단에 놓일 Button 위젯들을 한 행에 3개씩 격자 모양으로 배치시킬 것을 가정하여 columnspan을 3으로 설정한다. 첫 번째 위젯이므로 row(행)와 column(열)의 값은 모두 0으로 설정한다. 

## 3. Button 위젯
<p align="center"><img src=https://blog.kakaocdn.net/dn/bYumQl/btq8OkiuIZ7/p8trjkzc5ZctWGIcmbecyK/tfile.bmp
"></p>


버튼 목록은 위 코드처럼 원하는 이름으로 정의한다.
버튼은 행부터 만들어지기 때문에 행의 값을 1로 설정하고 열의 값은 0으로 설정한다.
<p align=><img src= https://blog.kakaocdn.net/dn/GiWkE/btq8KQWYIbg/kkhXsFkwiPASVum9k8niik/tfile.bmp
"></p>
<p align=><img src= https://blog.kakaocdn.net/dn/6VPOX/btq8KRauX7t/mbqI96asbrT9I9PhI7Sr11/tfile.bmp
"></p>

반복문을 통해 위에 정의 해놓은 버튼 목록을 하나씩 가져와서 버튼의 너비는 20, 높이는 3으로 하고 command를 통해 버튼을 눌렀을 때 클릭이라는 명령어가 쓰일 수 있게 한다. 버튼 위젯의 격자 모양은 행은 행을 받고 열은 열을 받아 정의한다. 따라서 조건문을 통해 행이 2보다 크면 열을 하나 증가시키고 행을 0으로 초기화 시켜준다. 즉, 행이 3일 때 마다 열이 다음 줄로 바뀌면서 다시 행이 쌓이는 형태이다. 

<p align="center"><img src=https://blog.kakaocdn.net/dn/szEDt/btq8Nv5Fn0D/gabA7fnkcvzu5DaEmBssc1/tfile.bmp
"></p>
위 그림처럼 버튼이 형성되는 것을 확인 할 수 있다.



## 4. 클릭 이벤트 처리
  <p align="center"><img src=https://blog.kakaocdn.net/dn/ctrROy/btq8Ndc5ZrG/UTZKzvlV2PZLFQgkZ9ZYik/tfile.bmp
"></p>
  
반복문을 통해 위에 정의 해놓은 버튼 목록을 하나씩 가져와 함수 click()으로 어떤 버튼이 클릭되었고 해당 문자가 무엇인지 매개변수로 받아들여 key 값으로 확인한다. 이때 조건문을 통해 key 값에 따라 문제를 수행한다.
if문을 통해 key 값이 ‘주문’이면 지금까지 입력한 문자열들을 eval()함수의 매개변수로 정의해 결과값을 계산한다. 여기서 eval()함수는 문자열을 입력받아 문자열을 숫자의 형태로 바꾼 후 산술 연산을 하는 함수이다. 다시 코드를 보게 되면 delete()함수를 통해 모든 값을 제거하고 insert()함수를 통해 먼저 계산한 결과값을 다시 출력하여 사용자에게 보여준다. 그리고 elif문을 통해 key 값이 ‘지움’이면 지금까지 입력한 모든 문자열을 지우라는 것이다.  
<p align="center"><img src=https://blog.kakaocdn.net/dn/pZBsy/btq8KXumcAT/83Npalb1xw8hxKz0bXyFak/tfile.bmp
"></p>
  

다음으로 elif문을 통해 key 값이 ‘아메리카노\n(핫)’일 때 아메리카노의 가격인 3000원을 문자열의 입력하는 코드를 작성한다. 이때 커피를 더해주는 +연산을 입력창에 넣기 위해 커피를 처음에 주문하는 경우와 그렇지 않은 경우를 나누어서 코드를 수행한다. if e.get():을 통해 Entry 값이 있으면 즉, 입력한 문자열이 있으면 “+3000”을 통해 입력한 문자열에 +연산을 통해 커피 값을 계산한다. 반대로 Entry 값이 없으면 가격만 출력하여 초기 값을 만든다. 핫초코도 아메리카노와 가격이 같으므로 똑같이 코드를 작성한다.
아메리카노와 핫초코를 뺀 나머지는 가격이 동일함으로 else문을 통해 나머지 커피를 클릭한 경우에 위 코드와 똑같이 Entry 값이 있으면 “+4000”을 입력하고 Entry 값이 없으면 가격 그대로만을 출력하여 초기값을 만든다. 
## 5. mainloop() 메서드
<p align="center"><img src=https://blog.kakaocdn.net/dn/J34FT/btq8Qqie2J4/J4k0PoGYTwSdyxKfjwBU40/tfile.bmp
"></p>
  

마지막에 mainloop() 메서드를 작성하여 윈도우 창을 윈도우가 종료될 때까지 실행시킨다.
## 6. 최종 실행 화면

<p align="center"><img src=https://blog.kakaocdn.net/dn/nmGjq/btq8H412RSF/3URYcE2bZViaTaUcTHiD4k/tfile.bmp
"></p>
아메리카노(핫)을 클릭해서 주문하면 주문창에 3000원이 생긴다.
  <p align="center"><img src=https://blog.kakaocdn.net/dn/b0d8Kq/btq8Ndc57P3/4KMTB1AiJ6EZKCLB2mmIsK/tfile.bmp
"></p>
카페라떼(핫)을 클릭해서 주문하면 주문창에 4000을 더한 3000+4000이 생긴다.
 <p align="center"><img src=https://blog.kakaocdn.net/dn/cabrBi/btq8KczfWt0/esRYJwFDwMy17Xcywkaq41/tfile.bmp
"></p>

마지막에 주문 버튼을 누르면 주문창에 있던 금액을 더한 결제 금액인 7000원이 주문창에 나오는 것을 위 사진처럼 확인 할 수 있다. 
