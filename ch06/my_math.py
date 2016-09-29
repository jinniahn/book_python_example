# 파일명: my_math.py
""" 
My Math
=======

이 모듈을 나만의 전용 수학 모듈이다.
"""
__all__ = ['fib']
# 모듈 버전
__version__ = 1.0

# 원주률
PI = 3.1415

def fib(n):
    "피보나치 수열 생성"
    a, b = 0, 1
    while b < n:
        yield b
        a, b = b, a+b
