class Mtrx:
    def __init__(self, name, n_row, n_col, L_data): # 행렬들의 값들을 초기화
        self.name = name
        self.n_row = n_row
        self.n_col = n_col
        self.rows = []
        index = 0
        for i in range(0,self.n_row):
            L_row = []
            for j in range(0,self.n_col):
                L_row.append(L_data[index])
                index = index+1
            self.rows.append(L_row)
      
    def __str__(self): # 리스트를 행렬로 표현
        s='\n'
        for i in range(0,self.n_row):
            for j in range(0,self.n_col):
                s += "{:3d}".format(self.rows[i][j],end="")
            s += "\n"
        return s
                    
    def __add__(self, other): # operator overloading of '+'
        L_res =[]
        for i in range(0,self.n_row):
            for j in range(0,self.n_col):
                r_ij = self.rows[i][j] + other.rows[i][j]
                L_res.append(r_ij)
        return Mtrx(self.name,self.n_row,self.n_col,L_res)   
         
    def __sub__(self, other): # operator overloading of '-'
        L_res =[]
        for i in range(0,self.n_row):
            for j in range(0,self.n_col):
                r_ij = self.rows[i][j] - other.rows[i][j]
                L_res.append(r_ij)
        return Mtrx(self.name,self.n_row,self.n_col,L_res) 
    
    def __mul__(self, other): # operator overloading of '*'
        L_res =[]
        for i in range(0,self.n_row):
            for j in range(0,self.n_col):
                r_ij=0
                for k in range(0,self.n_col):
                    r_ij = r_ij + self.rows[i][k]*other.rows[k][j]
                L_res.append(r_ij)
        return Mtrx(self.name,self.n_row,self.n_col,L_res) 