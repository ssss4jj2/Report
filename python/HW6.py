"""
 Project : 파이썬 프로그램 Homework 6.1
 Author  : 21611845 이승준
 Date of last update : 2020 10 14
 Update list : 
      
"""
#Procedure 자료형의 속성인 이름, 정수 주민등록 번호, 정수 나이를 가지는 Person 클래스 구현

# class Person:
   
#     def __init__(self,name,reg_id,age): # 클래스의 instance들을 초기화하는 함수
#         self.setName(name) 
#         self.setReg_id(reg_id)
#         self.setAge(age)
#         #print("Person::__init__() is excuted.")
        
#     def getName(self):
#         return self.name
#     def getReg_id(self):
#         return self.reg_id
#     def getAge(self):
#         return self.age 
    
#     def setName(self,nm): # Person의 이름을 설정.
#         self.name = nm
#     def setReg_id(self,r_id): # Person의 주민번호를 설정.
#         self.reg_id = r_id
#     def setAge(self,ag): # Person의 나이를 설정.
#         if 0 <= ag < 250: # 나이 정보의 옮고 그름을 판단.
#             self.age = ag
#         else:
#             print("*** Error in setting age (name:{}, age:{})".format(self.name,ag))
#             self.age = 0 #default value  
            
#     def __str__(self): # person의 형식 정의
#         return " Person({}, {}, {})".format(self.getName(), self.getReg_id(), self.getAge())
    
# def printPersonList(L_persons): # 클래스 출력 시스템 
#     for p in L_persons:
#         print(" ", p)
        
# ######################################################
# # Application
# if __name__ == "__main__":
#     persons = [
#         Person("Kim  ", 990101, 21),
#         Person("Lee  ", 980715, 22),
#         Person("Park ", 101225, 20),
#         Person("Hong ", 110315, 19),
#         Person("Yoon ", 971005, 23),
#         Person("Wrong", 100000, 350)
#     ]       
#     print("persons : ")
#     printPersonList(persons)




"""
 Project : 파이썬 프로그램 Homework 6.2
 Author  : 21611845 이승준
 Date of last update : 2020 10 14
 Update list : 
      
"""
#Procedure 클래스 student를 구현(학번,전공,평균성적)

# class Person:
       
#     def __init__(self,name,age): # 클래스의 instance들을 초기화하는 함수
#         self.setName(name) 
#         self.setAge(age)
#         #print("Person::__init__() is excuted.")
        
#     def getName(self):
#         return self.name
#     def getAge(self):
#         return self.age 
    
#     def setName(self,nm): # Person의 이름을 설정.
#         self.name = nm
#     def setAge(self,ag): # Person의 나이를 설정.
#         if 0 <= ag < 100: # 나이 정보의 옮고 그름을 판단.
#             self.age = ag
#         else:
#             print("*** Error in setting  age (name:{:4}, age:{:4})".format(self.name,ag))
#             self.age = 0 #default value  
            
#     def __str__(self): # person의 형식 정의
#         return " Person({}, {})".format(self.getName(), self.getAge())

# # Person클래스를 부모로 가지는 Student클래스
# class Student(Person):  
    
#     def __init__(self, name, age, st_id, major, gpa): # 학생들의 정보를 초기화 하는 함수
#         Person.__init__(self, name, age)
#         self.setSTID(st_id)
#         self.setMajor(major)
#         self.setGPA(gpa)
        
#     # 학생들의 전공, 학번, 학점을 가져온다.
#     def getMajor(self):
#         return self.major
#     def getSTID(self):
#         return self.st_id
#     def getGPA(self):
#         return self.gpa
    
#     # 학생들의 전공, 학번, 학점을 설정한다.
#     def setMajor(self, major):
#         # checking available major
#         set_majors = {"EE", "ICE", "ME", "CE"}
#         if major in set_majors: # 만약 위의 조건에 없는 전공 판별
#             self.major = major
#         else:
#             print("*** Error in setting major (name:{:4}, age:{:4})".format(self.name, self.age))
#             self.major = "None" # default value
            
#     def setSTID(self, st_id):
#         if st_id < 0 or st_id > 99999:
#             print("*** Error in setting st_id (name:{:4}, age:{:4})".format(self.name, self.age))
#             self.st_id = 0
#         else:
#             self.st_id = st_id
            
#     def setGPA(self, gpa):
#         if gpa > 4.5 or gpa < 0.0:
#             print("*** Error in setting  GPA  (name:{:4}, age:{:4})".format(self.name, self.age))
#             self.gpa = 0
#         else:
#             self.gpa = gpa
        
#     def __str__(self): # 기본 틀
#         return "Student({:6}, {:3}, {:5}, {:4}, {:4})".\
#             format(self.getName(), self.getAge(), self.getSTID(),\
#                 self.getMajor(), self.getGPA())

# # 학생들의 정보(학번, 이름, 학점)를 비교 하는 함수
# def compareStudent(st1, st2, compare): 
#     if compare == "st_id": # 학번 비교
#         if st1.st_id < st2.st_id:
#             return True
#         else:
#             return False
        
#     elif compare == "name": # 이름 비교
#         if st1.name < st2.name:
#             return True
#         else:
#             return False
        
#     elif compare == "gpa": # 학점은 내림차순으로 비교
#         if st1.gpa > st2.gpa:
#             return True
#         else:
#             return False
    
# # 학생들의 정보 중 compare 할 것을 기준으로 compare 함수를 이용해 소팅
# def sortStudent(L_st, compare): 
#     for i in range(0, len(L_st)):
#         min_idx = i
#         for j in range(i+1, len(L_st)):
#             if compareStudent(L_st[j],L_st[min_idx],compare):
#                 min_idx = j
#         if min_idx != i:
#             L_st[i],L_st[min_idx] = L_st[min_idx],L_st[i]

# def printStudents(L_st):
#     for s in range(len(L_st)):
#         print(L_st[s])

# ############################################
# ##########
# # Application

# if __name__ == "__main__":
#     students = [
#         Student("Kim ", 21, 12345, "EE", 4.0),
#         Student("Lee ", 22, 11234, "ME", 4.2),
#         Student("Park", 20, 10234, "ICE", 4.3),
#         Student("Hong", 19, 13123, "CE", 4.9),
#         Student("Yoon", 23, 11321, "ICE", 4.2),
#         Student("Wrong", 23, 12349, "GE", 3.2),
#         Student("Lee ", 25, 16161, "GE", 4.5),
#         Student("Kwon", 25, 100000, "EE", 2.9),
#         Student("Young", 26, 10001, "ICE", 3.7),
#         Student("Ha ", 170, 11111, "EE", 3.9)
#     ]
    
#     print("students before sorting : ")
#     printStudents(students)
#     # 학생들의 이름을 가지고 소팅
#     sortStudent(students, "name")
#     print("\nstudents after sorting by name : ")
#     printStudents(students)
#     # 학생들의 학번을 가지고 소팅
#     sortStudent(students, "st_id")
#     print("\nstudents after sorting by student_id : ")
#     printStudents(students)
#     # 학생들의 학점을 가지고 소팅 (내림차순)
#     sortStudent(students, "gpa")
#     print("\nstudents after sorting by GPA in decreasing order : ")
#     printStudents(students)



"""
 Project : 파이썬 프로그램 Homework 6.3
 Author  : 21611845 이승준
 Date of last update : 2020 10 14
 Update list : 
      
"""
#Procedure 연, 월, 일의 데이터 멤버를 가지는 class Date를 구현

# class Date:
#     def __init__(self, yr, mt, dy): # 년 월 일 초기화
#         self.setYear(yr)
#         self.setMonth(mt)
#         self.setDay(dy)
        
#     def __eq__(self, other):
#         if self.year == other.year and self.month == other.month\
#             and self.day == other.day:
#                 return True
    
#     def __lt__(self, other): 
#         if self.__eq__(other):
#             return False
#         elif (self.year, self.month, self.day) < (other.year,other.month,other.day):
#             return True
#         else:
#             return False
        
#     def __str__(self): # 틀
#         return ("({:5d}:{:5d}:{:4d})".format(self.getYear(), self.getMonth(), self.getDay()))
        
#     def getYear(self): # 년
#         return self.year
#     def getMonth(self): # 월
#         return self.month
#     def getDay(self): # 일
#         return self.day
    
#     def isLeapYear(self, yr): # 윤년인지 판단
#         if ((yr % 4 == 0) and (yr % 100 != 0)) or (yr % 400 == 0):
#             return True
#         else:
#             return False
    
#     def setYear(self,yr): # 년도 값 설정 받음
#         self.year = yr
        
#     def setMonth(self,mt): # 해당하는 달 검사 및 값 설정
#         if 1 <= mt <=12:
#             self.month = mt
#         else:
#             print("*** Error in Month setting ({}, {})".format(self.year, mt))
#             self.month = 1 # default value
            
#     def setDay(self,dy): # 해당하는 일 검사 및 값 설정
#         daysOfMonth = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#         if self.isLeapYear(self.year): # 윤년인지 확인 후 맞으면 윤년 ㄱ
#             daysOfMonth[2] = 29
#         if 1 <= dy <= daysOfMonth[self.month]:
#             self.day = dy
#         else:
#             print("*** Error in date setting ({}, {}, {})".format(self.year, self.month, dy))
#             self.day = 1
        
# ######################################################
# # Application
# #‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐

# if __name__ == "__main__":
#     dates = [
#         Date(2001, 5, 1),
#         Date(1997, 2, 20),
#         Date(2000, 9, 15),
#         Date(2001, 5, 2),
#         Date(2020, 10, 19),
#         Date(2019, 13, 12), # 월 오류
#         Date(1970, 3, 13),
#         Date(1966, 1, 27),
#         Date(1996, 4, 99), # 일 오류
#         Date(1996, 4, 4),
#     ]
    
#     print("dates before sorting : ")
#     for d in dates:
#         print(d)
#     #
#     #dates = sorted(dates)
#     dates.sort()
#     print("\nstudents after sorting : ")
#     for d in dates:
#         print(d)


"""
 Project : 파이썬 프로그램 Homework 6.4
 Author  : 21611845 이승준
 Date of last update : 2020 10 14
 Update list : 
      
"""
#Procedure 시 분 초의 데이터를 가지는 class Time 

# class Time:
#     def __init__(self, hr, mn, sec): # '시', '분', '초'를 초기화
#         self.setHour(hr)
#         self.setMinute(mn)
#         self.setSecond(sec)
        
#     def __lt__(self, other): # sort할 때 
#         if (self.hour, self.minute, self.second)\
#             < (other.hour, other.minute, other.second):
#                 return True
#         else:
#             return False
        
#     def __str__(self): # 틀
#         return "({:2d}:{:2d}:{:2d})"\
#             .format(self.getHour(), self.getMinute(),self.getSecond())
        
#     def getHour(self): # '시'값을 받음
#         return self.hour
#     def getMinute(self): # '분'값을 받음
#         return self.minute
#     def getSecond(self): # '초'값을 받음
#         return self.second
    
#     def setHour(self,hr): # '시'을 검사 및 설정
#         if 0 <= hr <=23:
#             self.hour = hr
#         else:
#             print("*** Error in setting time (hour: {:4})".format(hr))
#             self.hour = 0
            
#     def setMinute(self,mn): # '분'을 검사 및 설정
#         if 0 <= mn <=59:
#             self.minute = mn
#         else:
#             print("*** Error in setting time (minute: {:4})".format(mn))
#             self.minute = 0
            
#     def setSecond(self,sec): # '초'을 검사 및 설정
#         if 0 <= sec <=59:
#             self.second = sec
#         else:
#             print("*** Error in setting time (second: {:4})".format(sec))
#             self.second = 0
        
# ######################################################
# # Application
# times = [
#     Time(23, 59, 59),
#     Time(9, 0, 5),
#     Time(13, 30, 0),
#     Time(3, 59, 59),
#     Time(25, 4, 14), # hour Error
#     Time(11, 11, 11),
#     Time(12, 70, 1), # min Error
#     Time(0, 4, 7),
#     Time(17, 18, 49),
#     Time(21, 58, 62) # sec Error
#     ]

# print("times before sorting : ")
# for t in times:
#     print(t)

# # Time을 소팅한 후
# times.sort()
# print("\ntimes after sorting : ")
# for t in times:
#     print(t)


"""
 Project : 파이썬 프로그램 Homework 6.5
 Author  : 21611845 이승준
 Date of last update : 2020 10 14
 Update list : 
      
"""
#Procedure 행렬의 덧셈, 뺄셈, 곱셈 연산의 연산자 오버로딩 기능

class Mtrx:
    def __init__(self, name, n_row, n_col, L_data): # 행렬들의 값들을 초기화
        self.name = name
        self.n_row = n_row
        self.n_col = n_col
        self.L_data = L_data
      
    def __str__(self): # 리스트를 행렬로 표현
        print("")
        for i in range((self.n_row)*(self.n_col)):
            print("{:4}".format(self.L_data[i]), end ='')
            if ((i+1)%self.n_row)==0:
                print("")
        return ''
                    
    def __add__(self, other): # operator overloading of '+'
        L = [0]*25
        for i in range (self.n_col*self.n_row):
            L[i] = self.L_data[i] + other.L_data[i]
        return Mtrx(self.name,self.n_row,self.n_col,L)
        
    def __sub__(self, other): # operator overloading of '-'
        L = [0]*25
        for i in range (self.n_col*self.n_row):
            L[i] = self.L_data[i] - other.L_data[i]
        return Mtrx(self.name,self.n_row,self.n_col,L)
    
    def __mul__(self, other): # operator overloading of '*'
        L = [0]*25
        k = 0;
        for i in range(self.n_col*self.n_row): # 0-24까지 L_Data 수
            # 행렬 곱을 할 때 행을 나눠주기 위해
            if 0 <= i <= 4:
                k = 0
            elif 5<=i<=9:
                k=5
            elif 10<=i<=14:
                k=10
            elif 15<=i<=19:
                k=15
            else:
                k=20
            for j in range(self.n_col): # 0-4까지 열을 표시하기 위해 
                L[i] += self.L_data[j+k] * other.L_data[(5*j)+(i%5)] 
                # 행렬의 곱으로 표현하기.
        
        return Mtrx(self.name,self.n_row,self.n_col,L)
            

#‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐
if __name__ == "__main__":
    data_1 = [ 1, 2, 3, 4, 5,\
               6, 7, 8, 9, 10,\
               11, 12, 13, 14, 15,\
               16, 17, 18, 19, 20,\
               21, 22, 23, 24, 25]
    
    data_2 = [1, 0, 0, 0, 0,\
              0, 1, 0, 0, 0,\
              0, 0, 1, 0, 0,\
              0, 0, 0, 1, 0,\
              0, 0, 0, 0, 1]
    
    m1 = Mtrx("M1", 5, 5, data_1)
    print("m1 = ", m1)
    
    m2 = Mtrx("M2", 5, 5, data_2)
    print("m2 = ", m2)
    
    m3 = m1 + m2
    print("m3 = m1 + m2 =", m3)
    
    m4 = m1 - m2
    print("m4 = m1 - m2 =", m4)
    
    m5 = m1 * m2
    print("m5 = m1 * m2 =", m5)
