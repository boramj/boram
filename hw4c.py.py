# Assignment Numeber..: 4
# Author..............: Boram Jeong
# File name...........: hw4c.py
# Written Date........: 2017-07-04
# Program Description.: #1 함수를 정의하고 함수 내용을 return 값으로 정한다. 변수를 대입하여 print 로 출력한다.
						#2 range 함수를 이용해서 한 점의 n차원까지의 값을 인덱스 최대값으로 설정한다. 
						#두 점에서 대칭좌표끼리의 길이 차를 구한뒤 제곱한다. 모든 차이의 제곱에 루트를 적용해 출력한다.
						#3 함수를 정의하고 값이 0 이 될 때 까지 -1를 해준다. 0일때 문자열을 출력하여 종료한다.
						#4 lambda함수를 생성한다.

						 


def area_triangle(h,w):									#함수를 정의한다
	return 0.5*h*w 										#삼각형넓이 구하는 공식을 return값으로 설정한다
print(area_triangle(10,15))								#값을 출력한다




import math												#매쓰라이브러리를 불러온다

def distance(a,b): 										#새 함수를 정의한다
	t=0
	for i in range(len(a)):								
		t += (a[i]-b[i])**2								#두 점에서 대칭좌표끼리의 길이 차를 구한뒤 제곱한뒤 모든값을 더한다.

	return math.sqrt(t)									#루트를 적용한뒤 값을 반환한다

print(distance((1,2),(5,7)))



def count(n):											#count함수를 정의한다
	if n>0:												#n보다 큰경우 그대로 함수값에 다시 넣어 -1을 해준다
		print(n)
		return count(n-1)
	else:
		return 'zero!!'									#0이되면 'zero!!'로 출력한다

print(count(5))
 


area_triangle_id = lambda h, w : 0.5*h*w 				#삼각형 넓이 구하는 공식으로 새 lambda 함수를 만든다.
print(area_triangle_id(10, 15))							#값을 출력한다