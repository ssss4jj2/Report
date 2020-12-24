"""
 Project : 파이썬 프로그램 Homework 7.1
 Author  : 21611845 이승준
 Date of last update : 2020 10 21
 Update list : 
      
"""
#Procedure 10개의 국가 기본 정보를 받고, 국가의 인구 순으로 내림 차순

# import io

# with open("demography.txt",'w') as f1:
#     f1.write("Korea  Seoul  51780579  220918\n")
#     f1.write("USA  W.DC  329479633  983517\n")
#     f1.write("Canada  Ottawa  36488800  9984670\n")
#     f1.write("China  Beijing  1402727120  9596960\n")
#     f1.write("India  NewDelhi  1360657785  3287263\n")
#     f1.write("Brazil  Brazilia  211349952  8515767\n")
#     f1.write("Russia  Moscow  146727405  17098246\n")
#     f1.write("UK  London  64800000  243610\n")
#     f1.write("Japan  Tokyo  125960000  377975\n")
#     f1.write("France  Paris  67348000  551695\n")
# f1.close()

# f2 = open("demography.txt",'r')

# while True : 
#     read_data = f2.read()
#     if read_data == '':
#         break
    
# #print("f2.tell() = ",f2.tell())
# f2.seek(0) # 입력 및 출력 기능이 실행되는 시점으로 간다.
# #print("after f2.seek(0), f2.tell() = ", f2.tell())

# list_Country = []
# list_Capital = []
# list_Population = []
# list_Area = []

# # 국가의 정보를 한 줄단위로 읽어 각각의 리스트에 넣는다.
# for line in f2.readlines():
#     country, capital, population, area = line.split("  ")
#     list_Country.append(country)
#     list_Capital.append(capital)
#     list_Population.append(int(population))
#     list_Area.append(int(area))
# f2.close()

# # 각각의 나라 정보 list들을 zip을 이용해 묶는다.
# Country_records = list(zip(list_Country,list_Capital,list_Population,list_Area))

# print("List of Countries :")
# i = 0
# for x in Country_records: # country_records의 원소 x
#     print("Country[{:2}] = ('{:10}', '{:10}', '{:10}', '{:10})'"\
#         .format(i, x[0],x[1],x[2],x[3]))   # x의 원소 중 0,1,2,3(이름,수도,인구,면적)
#     i+=1
# # sorted함수를 이용. key 값을 country_records 의 3번째인 인구를 기준, reverse=True내림차순
# Country_records = sorted(Country_records, key = lambda Country_records: Country_records[2], reverse=True)

# print("\nList of Countries sorted by demography(number of people) :")
# i = 0
# for x in Country_records:
#     print("Country[{:2}] = ('{:10}', '{:10}', '{:10}', '{:10}')"\
#         .format(i, x[0],x[1],x[2],x[3]))   
#     i+=1

"""
 Project : 파이썬 프로그램 Homework 7.2
 Author  : 21611845 이승준
 Date of last update : 2020 10 21
 Update list : 
      
"""
#Procedure 10명의 학생 정보를 데이터파일로 받고, 학생들의 평균점수 계산 하여 추가
#          output.txt에 출력

#-*-coding:utf-8-*-
# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')

# with open("student_records.txt",'w',encoding = 'utf-8') as f1:
#     f1.write("이승준  21611845  95  95  95  95\n")
#     f1.write("이동현  21611835  85  95  80  85\n")
#     f1.write("박준형  21711051  85  95  80  90\n")
#     f1.write("윤종용  22011541  65  90  95  75\n")
#     f1.write("정성욱  21301231  55  45  85  90\n")
#     f1.write("김진영  21654321  95  85  70  65\n")
#     f1.write("원종필  21100153  45  55  95  80\n")
#     f1.write("김정현  21511825  95  45  95  75\n")
#     f1.write("김유정  21811725  95  65  80  85\n")
#     f1.write("김나은  21813542  95  75  65  85\n")
# f1.close()

# f2 = open("student_records.txt",'r',encoding = 'utf-8')

# while True : 
#     read_data = f2.read()
#     if read_data == '':
#         break
#     print(read_data)
    
# f2.seek(0)

# list_Name = []
# list_ID = []
# list_Kor = []
# list_Eng = []
# list_Mat = []
# list_Sci = []

# # 국가의 정보를 한 줄단위로 읽어 각각의 리스트에 넣는다.
# for line in f2.readlines():
#     name, student_id, sub_kor, sub_Eng, sub_Mat, sub_Sci = line.split("  ")
#     list_Name.append(name)
#     list_ID.append(int(student_id))
#     list_Kor.append(int(sub_kor))
#     list_Eng.append(int(sub_Eng))
#     list_Mat.append(int(sub_Mat))
#     list_Sci.append(int(sub_Sci))
# f2.close()

# student_records = list(zip(list_Name, list_ID, list_Kor, list_Eng, list_Mat, list_Sci))

# f3 = open("output.txt",'w',encoding = 'utf-8') # utf-8 = 한글 사용 가능
# f3.write("After calculate_scores(students)\n")
# f3.write(" name   [st_id]      kor  eng  math  sci  SUM  AVG\n")
# for x in student_records: # student_records의 원소 x
#     sub_sum = x[2] + x[3] + x[4] + x[5]
#     sub_avg = sub_sum/4
#     f3.write("{} [{}] =  {:3}, {:3}, {:3}, {:3}  {:4}, {:4}\n"\
#         .format(x[0],x[1],x[2],x[3],x[4],x[5],sub_sum,sub_avg ))
#     # 이름, 학번, 국어, 영어, 수학, 과학, 총점, 평균
    
# # 과목들의 평균
# Avg_kor = sum(list_Kor)/10
# Avg_Eng = sum(list_Eng)/10
# Avg_Mat = sum(list_Mat)/10
# AVg_Sci = sum(list_Sci)/10


# f3.write("\nAverage Score of each Class\n")
# f3.write("Kor_avg = {:5}\n".format(Avg_kor))
# f3.write("Eng_avg = {:5}\n".format(Avg_Eng))
# f3.write("Mat_avg = {:5}\n".format(Avg_Mat))
# f3.write("Sci_avg = {:5}\n".format(AVg_Sci))
# f3.close()



"""
 Project : 파이썬 프로그램 Homework 7.3
 Author  : 21611845 이승준
 Date of last update : 2020 10 21
 Update list : 
      
"""
#Procedure 행렬의 초기화 및, 덧셈, 뺄셈, 출력기능 클래스

# class Mtrx:
#     def __init__(self, name, n_row, n_col, L_data): # 행렬들의 값들을 초기화
#         self.name = name
#         self.n_row = n_row
#         self.n_col = n_col
#         self.rows = []
#         index = 0
#         for i in range(0,self.n_row):
#             L_row = []
#             for j in range(0,self.n_col):
#                 L_row.append(L_data[index])
#                 index = index+1
#             self.rows.append(L_row)
      
#     def __str__(self): # 리스트를 행렬로 표현
#         s='\n'
#         for i in range(0,self.n_row):
#             for j in range(0,self.n_col):
#                 s += "{:3d}".format(self.rows[i][j],end="")
#             s += "\n"
#         return s
                    
#     def __add__(self, other): # operator overloading of '+'
#         L_res =[]
#         for i in range(0,self.n_row):
#             for j in range(0,self.n_col):
#                 r_ij = self.rows[i][j] + other.rows[i][j]
#                 L_res.append(r_ij)
#         return Mtrx(self.name,self.n_row,self.n_col,L_res)   
         
#     def __sub__(self, other): # operator overloading of '-'
#         L_res =[]
#         for i in range(0,self.n_row):
#             for j in range(0,self.n_col):
#                 r_ij = self.rows[i][j] - other.rows[i][j]
#                 L_res.append(r_ij)
#         return Mtrx(self.name,self.n_row,self.n_col,L_res) 
    
#     def __mul__(self, other): # operator overloading of '*'
#         L_res =[]
#         for i in range(0,self.n_row):
#             for j in range(0,self.n_col):
#                 r_ij=0
#                 for k in range(0,self.n_col):
#                     r_ij = r_ij + self.rows[i][k]*other.rows[k][j]
#                 L_res.append(r_ij)
#         return Mtrx(self.name,self.n_row,self.n_col,L_res) 
            



"""
 Project : 파이썬 프로그램 Homework 7.4
 Author  : 21611845 이승준
 Date of last update : 2020 10 21
 Update list : 
      
"""
#Procedure 행렬의 크기를 지정하여 텍스트파일의 행렬을 읽어, 
#          행렬의 뺄셈, 곱셈, 덧셈을 출력
#          행렬 A를 json.dump를 사용해 mA_json.txt에 저장  

# Application Program of myClassMtrx
# import json,pickle
# import os, os.path
# import MyClassMtrx
# import CustomJsonEncoder

# def main():
#     #prepare mA,mB
#     data_1 = [] # data A
#     data_2 = [] # data B

#     f2 = open("mtrx.data.txt",'r') # 텍스트 파일 읽기
#     while True:
#         read_data = f2.read()
#         if read_data == '':
#             break     
#     f2.seek(0)
#     # 텍스트 파일을 한줄씩 읽으며, 정보를 데이터에 저장 #
#     line_num = 0
#     for line in f2.readlines():
#         if line_num == 0: # 행렬의 행과 열의 정보
#             A_row, A_col = map(int,line.split())
#         elif line_num == 6: # 행렬의 행과 열의 정보
#             B_row, B_col = map(int,line.split())
#         elif 0 < line_num < 6: # 행렬의 데이터를 한 행씩 저장
#             n0,n1,n2,n3,n4 = map(float, line.split())
#             hang = [n0,n1,n2,n3,n4]
#             data_1.append(hang)
#         else:
#             m0,m1,m2,m3,m4 = map(float, line.split())
#             hang = [m0,m1,m2,m3,m4]
#             data_2.append(hang)
#         line_num += 1
        
#     print("n_row = {}, n_col = {}".format(A_row,A_col))
#     mA = MyClassMtrx.Mtrx("mA", A_row, A_col, data_1)
#     print("mA = ",mA)
    
#     print("n_row = {}, n_col = {}".format(B_row,B_col))
#     mB = MyClassMtrx.Mtrx("mB", B_row, B_col, data_2)
#     print("mB = ",mB)
  
#     #operations for mC,mD,mE
#     mC = mA - mB
#     print("mC = mA - mB =", mC)
#     mD = mA + mB
#     print("mD = mA + mB =", mD)
#     mE = mA * mB  
#     print("mE = mA * mB =", mE)
    
#     #json파일을 생성한다.
#     f_json = open("mA_json.txt",'w')
#     json.dump(mA,f_json,indent=4,cls=CustomJsonEncoder.CustomEncoder)
#     f_json.close()
#     size_f_json=os.path.getsize("mA_json.txt")
#     print("size of mA_json.txt = ",size_f_json)
    
# if __name__ == "__main__":
#     main()






"""
 Project : 파이썬 프로그램 Homework 7.5
 Author  : 21611845 이승준
 Date of last update : 2020 10 21
 Update list : 
      
"""
#Procedure 7.4를 이용해 mA를 pickle로 저장하고, mA_json과 비교
# Application Program of myClassMtrx
import json,pickle
import os, os.path
import MyClassMtrx
import CustomJsonEncoder

def main():
    #prepare mA,mB
    data_1 = [] # data A
    data_2 = [] # data B

    f2 = open("mtrx.data.txt",'r') # 텍스트 파일 읽기
    while True:
        read_data = f2.read()
        if read_data == '':
            break     
    f2.seek(0)
    # 텍스트 파일을 한줄씩 읽으며, 정보를 데이터에 저장 #
    line_num = 0
    for line in f2.readlines():
        if line_num == 0: # 행렬의 행과 열의 정보
            A_row, A_col = map(int,line.split())
        elif line_num == 6: # 행렬의 행과 열의 정보
            B_row, B_col = map(int,line.split())
        elif 0 < line_num < 6: # 행렬의 데이터를 한 행씩 저장
            n0,n1,n2,n3,n4 = map(float, line.split())
            hang = [n0,n1,n2,n3,n4]
            data_1.append(hang)
        else:
            m0,m1,m2,m3,m4 = map(float, line.split())
            hang = [m0,m1,m2,m3,m4]
            data_2.append(hang)
        line_num += 1
        
    print("n_row = {}, n_col = {}".format(A_row,A_col))
    mA = MyClassMtrx.Mtrx("mA", A_row, A_col, data_1)
    print("mA = ",mA)
    
    print("n_row = {}, n_col = {}".format(B_row,B_col))
    mB = MyClassMtrx.Mtrx("mB", B_row, B_col, data_2)
    print("mB = ",mB)
  
    #operations for mC,mD,mE
    mC = mA - mB
    print("mC = mA - mB =", mC)
    mD = mA + mB
    print("mD = mA + mB =", mD)
    mE = mA * mB  
    print("mE = mA * mB =", mE)
    
    #json 파일을 생성 (javaScript Object Notation)
    #-> 효율적으로 데이터를 저장하고 교환하는데 사용하는 텍스트 데이터 포멧
    f_json = open("mA_json.txt",'w')
    json.dump(mA,f_json,indent=4,cls=CustomJsonEncoder.CustomEncoder)
    #json.dump = json데이터로 인코딩, indent(들여쓰기),
    f_json.close()
    
    size_f_json=os.path.getsize("mA_json.txt")
    print("size of mA_json.txt = ",size_f_json)
    
    #pickle 파일 생성 (파이썬클래스와 자료형 객체를 binary 형태로 저장)
    #-> 일반 텍스트를 파일로 저장할 때는 파일 입출력 사용
    #   리스트나 클래스 같은 텍스트가 아닌 자료형은 일반적 입출력으로 불가
    f_pickle = open("mA_pickle.bin","wb")
    pickle.dump(mA,f_pickle)
    f_pickle.close()
    
    size_f_pickle = os.path.getsize("mA_pickle.bin")
    print("size of mA_pickle.bin =",size_f_pickle)
if __name__ == "__main__":
    main()