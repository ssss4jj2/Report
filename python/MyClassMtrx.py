class Mtrx:
    def __init__(self, name, n_row, n_col, L_data): # 행렬들의 값들을 초기화
        self.name = name
        self.n_row = n_row
        self.n_col = n_col
        self.L_data = L_data
 
    def __str__(self): # 리스트를 행렬로 표현
        s='\n'
        for i in range(0,self.n_row):
            for j in range(0,self.n_col):
                s += "{:5.1f}".format(self.L_data[i][j],end=" ")
            s += "\n"
        return s
    
    def __sub__(self, other): # operator overloading of '-'
        L_res =[[0]*(self.n_row) for _ in range(self.n_col)] # 2차원 행렬 0으로 초기화
        for i in range(0,self.n_row):
            for j in range(0,self.n_col):
                L_res[i][j] = self.L_data[i][j] - other.L_data[i][j]
        return Mtrx(self.name,self.n_row,self.n_col,L_res) 
                        
    def __add__(self, other): # operator overloading of '+'
        L_res =[[0]*(self.n_row) for _ in range(self.n_col)] # 2차원 행렬 0으로 초기화
        for i in range(0,self.n_row):
            for j in range(0,self.n_col):
                L_res[i][j] = self.L_data[i][j] + other.L_data[i][j]
        return Mtrx(self.name,self.n_row,self.n_col,L_res)   
         
    def __mul__(self, other): # operator overloading of '*'
        L_res =[[0]*(self.n_row) for _ in range(self.n_col)] # 2차원 행렬 0으로 초기화
        for i in range(0,self.n_row): 
            for j in range(0,self.n_col):
                for k in range(0,self.n_col):
                    L_res[i][j] = L_res[i][j] + self.L_data[i][k]*other.L_data[k][j]
        return Mtrx(self.name,self.n_row,self.n_col,L_res) 