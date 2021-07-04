# n진수를 10진수로 변환


<p align="center"><img src=https://blog.kakaocdn.net/dn/df6xnL/btq8JisRQJ9/KwYhJcLrBD5qpc5Bn8e5E0/img.png
"></p>
  
- n진수를 역수로 바꾸어 반복문을 통해 10진수로 바꾼다.
- n진수가 n보다 클 경우 입력을 잘 못 받았으므로 반복을 멈춘다.
- n의 제곱승을 계산해주기 위해 s = 1부터 n씩 곱하여 계산한다.
  

## 하지만
int()함수를 통해서 쉽게 n진수를 10진수로 변환시키는 방법을 알게되었다.
- int(string, base)
- string에는 바꾸고 싶은 수, base에는 진법을 넣으면 된다.
- 예시) int("111", 2) 라고 코드를 작성하면 위 그림과 같이 정답이 7이 나오는 것을 확인할 수 있다.
