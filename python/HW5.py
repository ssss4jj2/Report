
"""
 Project : 파이썬 프로그램 Homework 5.1
 Author  : 21611845 이승준
 Date of last update : 2020 10 7
 Update list : 
      
"""
#Procedure MyList.py 모듈을 이용하여, 정수형 난수 출력
#User- defined package/module
#C:/MyPyPackage/myModules/
# MyList.py at C:/MyPyPackage/myModules/MyList.py

# import sys
# myPyPackage_dir = "C:/"
# sys.path.append(myPyPackage_dir)
# print("sys.path : ", sys.path)

# from MyPyPackage.myModules import MyList # 내가 만든 모듈을 불러온다.

# L = [] # 빈 리스트 생성
# n = 100 # 100개의 정수 

# L=MyList.genRandList(L, n) # myList 모듈안의 난수 생성 함수 사용
# MyList.printListSample(L, 5, 10) # myList 모듈안의 출력 함수 사용


"""
 Project : 파이썬 프로그램 Homework 5.2  
 Author  : 21611845 이승준
 Date of last update : 2020 10 7
 Update list : 
      
"""
#Procedure MySorting.py 모듈을 이용해 선택 정렬 알고리즘 구현
#User- defined package/module
#C:/MyPyPackage/myModules/
# MySorting.py at C:/MyPyPackage/myModules/MySorting.py

# import sys
# myPyPackage_dir = "C:/"
# sys.path.append(myPyPackage_dir)
# from MyPyPackage.myModules\
#     import MyList, MySortings # 내 모듈 내의 MyList와 MySortings 사용

# L = []
# n = 100

# L = MyList.genRandList(L, n)
# print("Before Sorting :")
# MyList.printListSample(L, 3, 10)

# MySortings.selectionSort(L) # 선택 정렬 실행
# print("\nAfter Sorting :")
# MyList.printListSample(L, 3, 10)




"""
 Project : 파이썬 프로그램 Homework 5.3
 Author  : 21611845 이승준
 Date of last update : 2020 10 7
 Update list : 
      
"""
#Procedure 50000개의 난수를 array 원소 배열에 포함시키고, 선택정렬을 이용해, 시간 측정. 
# Comparison of List and Array with user-defined modules (part1)

# import random, time, sys
# from array import*
# sys.path.append("C:/")
# from MyPyPackage.myModules import MyList, MySortings

# AR = array('i') # signed int 정수
# L = []
# size = 50000

# L = MyList.genRandList(L,size) # List에 50000개의 정수형 난수 생성

# for x in L: # array 모듈을 사용하여, List의 원소를 AR배열에 포함
#     AR.append(x) 
    
# print("Array (size : {}) before sorting : ".format(size))
# MyList.printListSample(AR, 2, 10)

# """ 선택정렬 (array) """
# t1 = time.time()
# MySortings.selectionSort(AR) # array 배열의 선택 정렬
# t2 = time.time()

# print("Array (size : {}) after sorting : ".format(size))
# MyList.printListSample(AR, 2, 10)
# print("Selection sorting for array of {} integers took {} sec"\
#     .format(size, t2-t1))

# print("\nList (size : {}) before sorting : ".format(size))
# MyList.printListSample(L, 2, 10)

# """ 선택정렬 (list) """
# t1 = time.time()
# MySortings.selectionSort(L) # list 배열의 선택정렬
# t2 = time.time()

# print("\nList (size : {}) after sorting : ".format(size))
# MyList.printListSample(L, 2, 10)
# print("Selection sorting for list of {} integers took {} sec"\
#     .format(size, t2-t1))

"""
 Project : 파이썬 프로그램 Homework 5.4
 Author  : 21611845 이승준
 Date of last update : 2020 10 7
 Update list : 
      
"""
#Procedure MySortings.py에 mergeSort(병합정렬)을 추가, 
#선택정렬과 병합정렬 실행후 경과시간 측정

# Comparison of mergeSort and selectionSort with user‐defined modules
# import random, time, sys
# sys.path.append("C:/")
# from MyPyPackage.myModules import MyList, MySortings

# while True:
#     size = int(input("\nsize of list (0 to terminate) = ")) # 랜덤하게 만들 정수 갯수 입력 받음
    
#     L = []
#     L = MyList.genRandList(L, size) # size에 해당하는 정수형 난수 생성
    
#     print("List (size : {}) before merge sorting : ".format(size))  
#     MyList.printListSample(L, 2, 10)
    
#     """ 합병정렬 """
#     t1 = time.time()
#     L = MySortings.mergeSort(L)
#     t2 = time.time()
    
#     print("\nList (size : {}) after merge sorting : ".format(size))
#     MyList.printListSample(L, 2, 10)
#     print("Merge sorting for list of {} integers took {} sec".format(size, t2-t1))
    
#     """ 리스트 다시 뒤섞기 """
#     L = MyList.shuffleList(L)
#     print("\nList (size : {}) before selection sorting : ".format(size))
#     MyList.printListSample(L, 2, 10)
    
#     """ 선택정렬 """
#     t1 = time.time()
#     MySortings.selectionSort(L)
#     t2 = time.time()
    
#     print("\nList (size : {}) after selection sorting : ".format(size))
#     MyList.printListSample(L, 2, 10)
#     print("Selection sorting for list of {} integers took {} sec".format(size, t2-t1))



"""
 Project : 파이썬 프로그램 Homework 5.5
 Author  : 21611845 이승준
 Date of last update : 2020 10 7
 Update list : 
      
"""
#Procedure MyMatrix.py 모듈을 사용하여 행렬의 덧셈, 뺄셈, 곱셈 연산 수행
# Testing user‐defined module MyMatrix

import random, time, sys
myPyPackage_dir = "C:/"
sys.path.append(myPyPackage_dir)
from MyPyPackage.myModules import MyMatrix

A = [[1,2,3], [4,5,6], [7,8,9]]
B = [[1,0,0], [0,1,0], [0,0,1]]

print("A = ", A)
print("B = ", B)

""" 덧셈 연산 """
C = MyMatrix.mtrxAdd(A, B)
print("C = A + B = ", C)

""" 뺄셈 연산 """
D = MyMatrix.mtrxSub(A, B)
print("D = A ‐ B = ", D)

""" 곱셈 연산 """
E = MyMatrix.mtrxMul(A, B)
print("E = A * B = ", E)