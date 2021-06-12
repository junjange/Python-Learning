# math, sympy 모듈 호출
# sympy 모듈은 https://docs.sympy.org/latest/tutorial/index.html#tutorial 들어가 다운
from math  import *
from sympy import *

import numpy as np
import cmath
 
x, y, z, t = symbols('x y z t')
f, g, h = symbols('f, g, h', cls=Function)

# 쥬피터에서 가능 파이참과 같은 프로그램에서는 다른 방법 사용
init_printing()
%matplotlib inline 

# 함수 f(t)의 라플라스 변환을 정의
# sympy의 라플라스 변환과 역변환 모듈을 도입, 변수  s  와 상수들을 선언
from sympy.integrals.transforms import laplace_transform
from sympy.integrals.transforms import inverse_laplace_transform

s = symbols('s')
a, ω = symbols('a ω', constant=True, positive=True)

# (라플라스 변환, 수렴조건들)
# 라플라스 변환만 출력하고 싶으면 noconds=True를 작성
# f(t) = 1
laplace_transform( 1, t, s )

# f(t) = t^2 * e^at
laplace_transform( (t**2)*exp(a*t), t, s, noconds=True )

# f(t) = e^at * sin(ωt)
laplace_transform(exp(a*t) * sin(ω*t), t, s, noconds=True )

# f(t) = e^-at * cos(ωt)
laplace_transform(exp(-a*t) * cos(ω*t), t, s, noconds=True )

# f(t) = t* e^-at
laplace_transform( (t)*exp(-a*t), t, s, noconds=True )

# f(t) = t^2
laplace_transform(t*t, t, s, noconds=True )

# f(t) = sin(ωt + x)
laplace_transform(sin(ω*t +x), t, s, noconds=True )

