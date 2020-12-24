"""
 Project : 파이썬 프로그램 Homework 9.1
 Author  : 21611845 이승준
 Date of last update : 2020 11 12
 Update list : 
      
"""
#Procedure normal 함수 사용하여 정규분포의 난수 10000개 생성하여, ndarray G에 저장.

# import numpy as np

# def printNumpySample(L,per_lines,sample_lines,size): #10개의 원소를 두줄씩 출력하는 함수
#     for i in range(per_lines*sample_lines): # 두 줄씩
#         print("{:10.3f}".format(L[i]), end = '')
#         if ((i+1) % sample_lines) == 0: # 10개씩 줄 바꿈
#             print()

#     print("\n     . . . . . .\n")

#     for i in range(size-per_lines*sample_lines,size): # 두 줄씩
#         print("{:10.3f}".format(L[i]), end = '')
#         if ((i+1) % sample_lines) == 0: # 10개씩 줄 바꿈
#             print()
# while True: 
#     input_data_float =input("mu and sigma (in float): ")
#     mu_sigma = input_data_float.split(" ")
#     (mu,sigma) = tuple(map(float,mu_sigma))

#     size = int(input("size of array: "))
#     print("mu = {}, sigma = {}".format(mu,sigma))
#     G = np.random.normal(mu,sigma,size) # 난수로 만든 정규 분포
#     print("Sample of G = np.random.normal({}, {}, {}) = ".format(mu,sigma,size))

#     printNumpySample(G,2,10,size)

#     avg = np.average(G) #G의 평균
#     var = np.var(G)     #G의 분산
#     std = np.std(G)     #G의 표준편차

#     print("mean of G = ",avg)
#     print("var  of G = ",var)
#     print("std  of G = ",std)


"""
 Project : 파이썬 프로그램 Homework 9.2
 Author  : 21611845 이승준
 Date of last update : 2020 11 12
 Update list : 
      
"""
#Procedure 직병렬 전자회로 선형시스템 해를 Numpy solve()를 이용해 풀기.

# import numpy as np

# A = np.array([[10,10,0,0,0],[1,-1,-1,0,0],[0,0,1,-1,-1],[0,10,-5,-10,0],[0,0,0,10,-10]])
# B = np.array([100,0,0,0,0])

# X = np.linalg.solve(A,B) #A와 B의 행렬을 이용해 X를 구함.
# B_pr = np.matmul(A,X) # 위에서 구한 X를 이용해 A와 X를 곱해 B를 구함.

# print("A = \n",A)
# print("B = ", B)
# print("X = np.linalg.solve(A)")
# print("X = ", X)
# print("B_pr = np.matmul(A, X) = ", B_pr)


"""
 Project : 파이썬 프로그램 Homework 9.3
 Author  : 21611845 이승준
 Date of last update : 2020 11 12
 Update list : 
      
"""
#Procedure 텍스트 파일에 7x7개수 정수 저장한뒤, 2차원 A생성
#          inv()를 이용해 A의 역행렬 구한뒤, matmul()함수를 써서 증명


# import numpy as np

# A = np.loadtxt("npArray_A.txt")
# print("Loaded A : \n", A) # npArray_A의 텍스트를 읽어옴

# det = np.linalg.det(A)
# print("det = ",det) # A의 determinet를 구함

# inv_A = np.linalg.inv(A)
# print("inv_A = \n",inv_A) # A의 역행렬을 구함

# E = np.matmul(A,inv_A) # A와 A의 역행렬을 곱해 단위행렬을 만듬
# print("\nE = np.matmul(A,inv_A) :")
# print(E)


"""
 Project : 파이썬 프로그램 Homework 9.4
 Author  : 21611845 이승준
 Date of last update : 2020 11 12
 Update list : 
      
"""
#Procedure 공식으로 주어지는 싸인파 그래프를 Matplotib 패키지의 pylpot 모듈을 사용해 그래프 그려라.

# import numpy as np
# import matplotlib.pyplot as plt

# def sine_graph(amp,freq,theta,pattern):
#     x = np.linspace(0, 2*np.pi, num=41) # 0부터 2pi까지 40등분하여 구간 기준값 원소 1차원 배열 x 생성.
#     sin_x = amp*np.sin(freq*x + theta)  # Amp*sine(x*freq + theta)
#     plt.plot(x,sin_x,"k--",x,sin_x,pattern) # 검정색 실선으로 표시
#     xmin, xmax, ymin, ymax = x[0], x[-1], -1, 1
#     plt.axis([xmin, xmax, ymin, ymax])

# sine_graph(1,2,0,"ro")       # 진폭이 1이고, freq가 2고, red 점의 패턴
# sine_graph(1,2,np.pi/2,"bo") # 진폭이 1이고, freq가 2고, blue 점의 패턴
# sine_graph(1,2,np.pi,"go")   # 진폭이 1이고, freq가 2고, green 점의 패턴

# plt.xlabel("x")
# plt.ylabel("sin(freq*x + theta)")
# plt.title("Example of matplotlib -sin(freq*x + theta)")
# plt.grid(True)
# plt.savefig("21611845_sin.png")
# plt.show()


"""
 Project : 파이썬 프로그램 Homework 9.5
 Author  : 21611845 이승준
 Date of last update : 2020 11 12
 Update list : 
      
"""
#Procedure 배열 x 주어진 평균(mu)와 표준편차(sima)를 인수로 전달 받아,
    #x에 대한 정규 분포 y를 생성하는 gauss 함수 구현

import numpy as np
import matplotlib.pyplot as plt

def gauss(mu, sigma, X):
    y = 1.0/(sigma*np.sqrt(2*np.pi))*np.exp(-((X - mu)**2)/(2*sigma**2))
    return y

X = np.linspace(-8, 8, num=101) # -8~+8구간을 100개의 등 간격으로 나눈 X(1차원 배열)

"""mu가 0이고, sigma가 각각 0.5,1,2일 때"""
mu, sigma = 0, 0.5 # sigma가 0.5일때
y1 = gauss(mu, sigma, X)
plt.plot(X, y1, color="red", label="sigma=0.5")

mu, sigma = 0, 1 # sigma가 1일때
y2 = gauss(mu, sigma, X)
plt.plot(X, y2, color="blue", label="sigma=1")

mu, sigma = 0, 2 # sigma가 2일때
y3 = gauss(mu, sigma, X)
plt.plot(X, y3, color="green", label="sigma=2")

plt.title("Normal_Distribution_Graph-1 ,mu=0.0, sigma = [0.5, 1, 2]")
plt.legend(loc="best")
plt.grid(True)
plt.savefig("21611845_GaussDist.png")
plt.show()

"""sigma가 1이고, mu가 각각 -2.0,0.0,+2.0일 때"""
mu, sigma = -2.0, 1 # mu가 -2.0일때
y1 = gauss(mu, sigma, X)
plt.plot(X, y1, color="red", label="sigma=-2.0")

mu, sigma = 0.0, 1 # mu가 0.0일때
y2 = gauss(mu, sigma, X)
plt.plot(X, y2, color="blue", label="sigma=0.0")

mu, sigma = 2.0, 1 # mu가 +2.0일때
y3 = gauss(mu, sigma, X)
plt.plot(X, y3, color="green", label="sigma=+2.0")

plt.title("Normal_Distribution_Graph-2 ,mu = [-2.0, 0.0, 2.0], sigma = 1")
plt.legend(loc="best")
plt.grid(True)
plt.savefig("21611845_GaussDist2.png")
plt.show()