"""
 Project : 파이썬 프로그램 Homework 10.3
 Author  : 21611845 이승준
 Date of last update : 2020 11 18
 Update list : 
      
"""
#Procedure 중복되지 않는 정수형 난수 30000개를 포함하여 
#          selection Sort,merge Sort, quick Sort를 측정 후, 걸리는 시간 측정.

# import os,sys,random,time
# import numpy as np
# import operator

# def genRandList(aList,size): # 랜덤하고 중복 되지 않는 정수 생성.
#     for x in range(0,size):
#         aList.append(x)
#     random.shuffle(aList)

    
# def printListSample(aList,per_line =10,sample_lines = 3): # 출력 틀
#     count =0
#     size = len(aList)
#     for i in range(0,sample_lines):
#         s=""
#         for j in range(0,per_line):
#             if count>size:
#                 break
#             s+="{0:>7}".format(aList[count])
#             count+=1
#         print(s)
#         if count>=size:
#             break
#     if count<size:
#         print('                          .................')   
#         if count < (size - per_line*sample_lines):
#             count = size - per_line*sample_lines
#         for i in range(0,sample_lines):
#             s=""
#             for j in range(0,per_line):
#                 if count>=size:
#                     break
#                 s+="{0:>7}".format(aList[count])
#                 count+=1
#             print(s)
#             if count>=size:
#                 break
        
# def selectionSort(aList,size): # 선택 정렬
#     for i in range(0,size-1):
#         min=i
#         for j in range(i+1,size):
#             if(aList[min]>aList[j]): # min의 값 보다 j 값이 더 작으면 min을 j로 변경
#                 min=j
#         if(min != i):
#             aList[i],aList[min]=aList[min],aList[i]
        
# def merge(aList_left,aList_right,compare): # 병합(재귀호출로 받은 값을 사용)
#     aList_result = []
#     i, j = 0, 0
#     while i < len(aList_left) and j < len(aList_right):   
#         if compare(aList_left[i], aList_right[j]): # aList_left[i] < aList_right[j] 
#             aList_result.append(aList_left[i]) # 리스트 왼쪽 값을 추가.
#             i += 1
#         else: # aList_left[i] >= aList_right[j]
#             aList_result.append(aList_right[j]) # 리스트 오른쪽 값을 추가. 
#             j += 1
            
#     while (i < len(aList_left)):
#         aList_result.append(aList_left[i])
#         i += 1
        
#     while (j < len(aList_right)):
#         aList_result.append(aList_right[j])
#         j += 1
        
#     return aList_result
        
# def mergeSort(aList,compare=operator.lt): # 병합정렬 (lt = <)
#     if len(aList)<2:
#         return aList[:] # 재귀함수 호출로 부터 반환
#     else:
#         middle = len(aList)//2  # 리스트의 절반을 나눠 재귀호출.
#         left = mergeSort(aList[:middle],compare)
#         right = mergeSort(aList[middle:],compare)
#         return merge(left,right,compare)

# def _partition(aList,left,right,pi): # 퀵정렬의 partition
#     pv = aList[pi] #pivot from pivot_index
#     aList[pi],aList[right] = aList[right], aList[pi] # 피봇 인덱스 위치 원소를 배열 맨 오른쪽으로 변경
#     new_pi = i = left  # 새 피봇을 left로 설정.
#     while (i<=right-1): 
#         if(aList[i]<=pv): # pv보다 작거나 같은 원소가 있으면
#             aList[new_pi],aList[i] = aList[i],aList[new_pi] # 변경.
#             new_pi += 1
#         i+=1
#     aList[new_pi],aList[right] = aList[right],aList[new_pi]
#     return new_pi

# def _quickSortLoop(aList,left,right): # 주어진 리스트에 대해 재귀함수 호출을 반복적으로 사용
#     if(left>=right):
#         return
#     pi=(left+right)//2 # pivot_index
#     new_pi = _partition(aList,left,right,pi)
#     # 정렬할 대상이 남아 있다면, 다시 재귀함수 ㄱ
#     if(left<new_pi -1):
#         _quickSortLoop(aList,left,new_pi-1)
#     if(new_pi+1<right):
#         _quickSortLoop(aList,new_pi+1,right)

# def quickSort(aList):
#     size =len(aList)
#     _quickSortLoop(aList,0,size-1)
    
# while True:
#     A = []
#     print("\nComparisons of sorting algorithms")
#     aList_size = int(input("List Size (‐1 to quit)( < 50000) = "))
#     if aList_size == -1:
#         break
    
#     genRandList(A,aList_size)
    
#     # testing selctionSorting
#     np.random.shuffle(A)
#     print("\nBefore Selection‐Sort of A :")
#     printListSample(A, 10, 3)
#     t1 = time.time()
#     selectionSort(A, aList_size)
#     t2 = time.time()
#     print("After Selection‐Sort of A .....")
#     printListSample(A, 10, 3)
#     time_elapsed = t2 - t1
#     print("Selection sorting took {} sec\n".format(time_elapsed))
    
#     # testing MergeSorting
#     np.random.shuffle(A)
#     print("\nBefore mergeSort of A :")
#     printListSample(A, 10, 3)
#     t1 = time.time()
#     A = mergeSort(A)
#     t2 = time.time()
#     print("After mergeSort of A :")
#     printListSample(A, 10, 3)
#     time_elapsed = t2 - t1
#     print("Merge sorting took {} sec\n".format(time_elapsed))
    
#     # testing Quick Sorting
#     np.random.shuffle(A)
#     print("\nBefore quickSort of A :")
#     printListSample(A, 10, 3)
#     t1 = time.time()
#     quickSort(A)
#     t2 = time.time()
#     print("After quickSort of A :")
#     printListSample(A, 10, 3)
#     time_elapsed = t2 - t1
#     print("Quick sorting took {} sec\n".format(time_elapsed))


"""
 Project : 파이썬 프로그램 Homework 10.4
 Author  : 21611845 이승준
 Date of last update : 2020 11 18
 Update list : 
      
"""
#Procedure 중복되지 않는 정수형 난수 30000개를 포함하여 
#          우선순위큐를 사용하여 정렬하는 heap sort구현.

# import os,sys,random,time
# import numpy as np
# import operator

# def genRandList(aList,size): # 랜덤한 정수 생성 후 리스트에 넣음.
#     for x in range(0,size):
#         aList.append(x)
#     random.shuffle(aList)

# def printListSample(aList,per_line =10,sample_lines = 3): # 출력 틀ㅇㅇ
#     count =0
#     size = len(aList)
#     for i in range(0,sample_lines):
#         s=""
#         for j in range(0,per_line):
#             if count>size:
#                 break
#             s+="{0:>7}".format(aList[count])
#             count+=1
#         print(s)
#         if count>=size:
#             break
#     if count<size:
#         print('                          .................')   
#         if count < (size - per_line*sample_lines):
#             count = size - per_line*sample_lines
#         for i in range(0,sample_lines):
#             s=""
#             for j in range(0,per_line):
#                 if count>=size:
#                     break
#                 s+="{0:>7}".format(aList[count])
#                 count+=1
#             print(s)
#             if count>=size:
#                 break

# def heapify(alist,index,heap_size): # 힙 성질 만족 여부 검증 후, 재정렬
#     largest = index # 부모 노드(루트 노드)
#     left_index = 2*index + 1 # 왼쪽 자식 노드
#     right_index = 2*index + 2 # 오른쪽 자식 노드

#     # 왼쪽 자식 노드가 부모 노드 보다 클 때
#     if left_index < heap_size and alist[left_index] > alist[largest]:
#         largest = left_index # 부모노드를 왼쪽 자식 노드로 변경.
        
#     # 오른쪽 자식 노드가 부모 노드 보다 클 때
#     if right_index < heap_size and alist[right_index] > alist[largest]:
#         largest = right_index # 부모노드를 오른쪽 자식 노드로 변경.
        
#     if largest != index:
#         alist[largest],alist[index] =alist[index],alist[largest]
#         heapify(alist,largest,heap_size)
        
# def heapSort(alist): # 힙 정렬 
#     n = len(alist)
#     for i in range(n//2-1,-1,-1):
#         heapify(alist,i,n)
#     #after max heap
#     for i in range(n-1,0,-1):
#         alist[0],alist[i] = alist[i],alist[0]
#         heapify(alist,0,i)
#     return alist

# while True:
#     A = []
#     print("\nComparisons of sorting algorithms")
#     aList_size = int(input("List Size (‐1 to quit)( < 50000) = "))
#     if aList_size == -1:
#         break
    
#     genRandList(A,aList_size)
    
#     # testing heapSorting
#     np.random.shuffle(A)
#     print("\nBefore Heap‐Sort of A :")
#     printListSample(A, 10, 3)
#     t1 = time.time()
#     heapSort(A)
#     t2 = time.time()
#     print("After Heap‐Sort of A .....")
#     printListSample(A, 10, 3)
#     time_elapsed = t2 - t1
#     print("Heap‐Sorting took {} sec\n".format(time_elapsed))

"""
 Project : 파이썬 프로그램 Homework 10.5
 Author  : 21611845 이승준
 Date of last update : 2020 11 18
 Update list : 
      
"""
#Procedure 학생 이름을 key로 한 hash map 구현.

class Entry:
    def __init__(self, k, v):
        self._key = k # 엔트리의 키 값  = name
        self._value = v # 엔트리의 value
    def __str__(self):
        return str(self._value)

def CyclicShiftHashCode(str_key): # str_key를 받아 한글자씩 아스키 코드 변환 
    mask = (1 << 32) - 1 # limit to 32‐bit integers
    h = 0
    for ch in str_key:
        h = (h << 5 & mask) | (h >> 27) # cyclic shift hash code
        h += ord(ch)
    return h

class Bucket(Entry): # 버킷 클래스
    def __init__(self): # 초기화 
        self._bucket=[] # implement bucket using list
    def _getitem(self,k): # key를 가지고 value를 찾음.
        for item in self._bucket:
            if k == item._key:
                return item._value
        return None
    def _setitem(self,k,v): # key와 value를 가지고 설정.
        for item in self._bucket:
            if k == item._key:
                item._value = v
                return
        self._bucket.append(Entry(k,v)) # 버켓에 추가.
    def _delitem(self,k): # 삭제
        for j in range(len(self._bucket)):
            if k == self._bucket[j]._key:
                self._bucket.pop(j)
                return 1
            return None
    def __len__(self): # 버켓의 길이
        return len(self._bucket)
    def __iter__(self): # provides iterator as generator fucnction
        for item in self._bucket:
            yield item._key
            
class HashMap_Bucket(Bucket): # 해쉬 맵(버켓을 사용.)
    def __init__(self,table_size=11,prm = 109345121):
        self._hash_tbl = table_size * [None]
        self._hash_tbl_size = table_size
        self._num_entry = 0
        self._prime = prm
    def _hash_value(self, k):
        return CyclicShiftHashCode(k) % self._prime % self._hash_tbl_size
    def __len__(self):
        return self._num_entry
    def _getitem(self, k): # key를 이용해 hashmap에서 찾음.
        hv = self._hash_value(k)
        print("key({}) => hash_tbl[{}]".format(k, hv))
        bucket = self._hash_tbl[hv]
        return bucket._getitem(k)
    def _setitem(self, k, v): # hashmap을 설정
        hv = self._hash_value(k)
        if self._hash_tbl[hv] is None:
            self._hash_tbl[hv] = Bucket()
        bucket = self._hash_tbl[hv]
        bucket._setitem(k, v)
    def _delitem(self, k):
        hv = self._hash_value(k)
        bucket = self._hash_tbl[hv]
        bucket._delitem(k)
        self._num_entry-=1
    def __str__(self):
        s = ''
        for h in range(len(self._hash_tbl)):
            bucket = self._hash_tbl[h]
            if bucket is not None:
                s += "bucket[{:2d}] :".format(h)
                for item in bucket:
                    s+=str(item) +", "
                s+="\n"
        return s

# main
HashMap_Capacity = 7
print("Creating a HashMap_Bucket of capacity ({})".format(HashMap_Capacity))
hsMap = HashMap_Bucket(table_size = HashMap_Capacity)

L_students = [("Kim Y-S", 21611802, "ICE",4.2), ("Park S-J", 21911012, "CS",3.9),\
                ("Hong C-H", 21611222, "EE",3.8), ("Lee W-S", 21811851, "ME",4.0),\
                ("Yoon C-M", 21611123, "ICE",4.1), ("Moon J-K", 21711702, "CHEM",3.7),
                ("Lee Y-S", 21511501, "ICE",4.1), ("Lee S-J", 21611845, "CS",4.5),
                ("Moon C-H", 21911005, "CHEM",3.3), ("Park W-S", 21611855, "ICE",4.0),  
                ("Kim S-S", 21611945, "EE",3.0), ("Park S-W", 21911875, "CS",3.9),
                ("Hong C-L", 21411665, "CHEM",3.8), ("Lee K-S", 21611825, "ME",4.2),
                ("Kim Y-S", 21711845, "CS",2.7), ("Park S-L", 21711815, "CHEM",2.9),
                ("Yoon G-G", 21611999, "EE",3.3), ("Lee S-O", 21511815, "ME",3.7),
                ("Yoon Y-S", 21911845, "ICE",4.2), ("Park S-P", 22011845, "CS",4.4)]
                
for i in range(len(L_students)):
    st_record = L_students[i]
    st_name = L_students[i][0]
    hsMap._setitem(st_name,st_record) # L_students 리스트를 해쉬 맵으로 세팅.
print("Current HashMap Internal Structure:\n",hsMap)
# print("Checking entry searching in HashMap")
# for i in range(len(L_students)):
#     st_name = L_students[i][0]
#     st_record = hsMap._getitem(st_name)
#     print("key ({}) : Value ({})".format(st_name, st_record))

while True:
        search_std = input('\ninput Students name:')
        if search_std == 'stop':
            break
        
        print("key({}) : Value({})".format(search_std, hsMap._getitem(search_std)))

