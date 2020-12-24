"""
2 1 5 1 1 3 4
2 1 5 1 3 5 3
2 3 4 5 2 2 4
4 4 3 2 3 1 3
4 3 5 3 1 4 3
5 4 4 3 3 5 5
2 1 3 5 1 1 2
"""

def DFS(L_grap,st_row,st_col,path): # start row, start col 시작할 행과 열
    
    count = 1 # 같은 색의 블록이 나오면 카운터 1
    L_data = L_grap[st_row][st_col] # start node
    path.append([st_row,st_col])
    #aready_visit = L_grap[st_row][st_col]
    
    vis_row = 0 
    vis_col = 0 # 탐색할 행과 열 -> 이게 start 행열의 상,하,좌,우 가 되야 한다.
    
    ## 상 => vis_row = st_row - 1 ,vis_col = st_col
    ## 하 => vis_row = st_row + 1 ,vis_col = st_col
    ## 좌 => vis_row = st_row     ,vis_col = st_col - 1
    ## 우 => vis_row = st_row     ,vis_col = st_col + 1
    
    plus_minu = [-1,1,0,0]
    plus_minu2 = [0,0,-1,1]
    
    for i in range(0,4):
        vis_row = st_row + plus_minu[i]   # 재탐색이 일어남... 이걸 어떻게 고쳐야 할까..
        vis_col = st_col + plus_minu2[i]
        #visit_data = L_grap[vis_row][vis_col] # 방문할 열?
            
        if vis_row < 0 or vis_col < 0 or vis_row > 6 or vis_col > 6: # 해당 범위 넘어 갈때
            continue
        else:
            if L_data == L_grap[vis_row][vis_col] and [vis_row, vis_col] not in path: #and (visit_data  aready_visit):
                
                count += DFS(L_grap,vis_row,vis_col,path)
                    
    return count


C_row = 7
C_col = 7

Candy_List = [[int(x) for x in input().split( )]for y in range(C_col)]

result = 0
re_count = 0
path = []
for i in range(0,7): # 시작하는 행과 열
    for j in range(0,7):
        result = DFS(Candy_List,i,j,path)
        if result >= 3:
            re_count += 1

print(" ",re_count)


# """
# 2 1 5
# 2 1 5 
# 2 3 4
# """

# def DFS(L_grap,st_row,st_col,path): # start row, start col 시작할 행과 열
    
#     count = 1 # 같은 색의 블록이 나오면 카운터 1
#     L_data = L_grap[st_row][st_col] # start node
#     path.append([st_row,st_col])
#     #aready_visit = L_grap[st_row][st_col]
    
#     vis_row = 0 
#     vis_col = 0 # 탐색할 행과 열 -> 이게 start 행열의 상,하,좌,우 가 되야 한다.
    
#     ## 상 => vis_row = st_row - 1 ,vis_col = st_col
#     ## 하 => vis_row = st_row + 1 ,vis_col = st_col
#     ## 좌 => vis_row = st_row     ,vis_col = st_col - 1
#     ## 우 => vis_row = st_row     ,vis_col = st_col + 1
    
#     plus_minu = [-1,1,0,0]
#     plus_minu2 = [0,0,-1,1]
    
#     for i in range(0,3):
#         vis_row = st_row + plus_minu[i]   # 재탐색이 일어남... 이걸 어떻게 고쳐야 할까..
#         vis_col = st_col + plus_minu2[i]
#         #visit_data = L_grap[vis_row][vis_col] # 방문할 열?
            
#         if vis_row < 0 or vis_col < 0 or vis_row > 2 or vis_col > 2: # 해당 범위 넘어 갈때
#             continue
#         else:
#             if L_data == L_grap[vis_row][vis_col] and [vis_row, vis_col] not in path: #and (visit_data  aready_visit):
                
#                 count += DFS(L_grap,vis_row,vis_col,path)
                    
#     return count
        
    
#     # for i in range(0,6): # 탐색
#     #     vis_row = st_row + i
        
#     #     for j in range(0,6):
#     #         vis_col = st_col + j
#     #         visit_data = L_grap[vis_row][vis_col] # 방문할 열?
            
#     #         if vis_row < 0 or vis_col < 0 or vis_row > 6 or vis_col > 6: # 해당 범위 넘어 갈때
#     #             return False
#     #             #continue
                
#     #         else:
#     #             if L_data == visit_data:
#     #                 count += DFS(L_grap,vis_row,vis_col)
                    
#     # return count
    


# C_row = 3
# C_col = 3

# Candy_List = [[int(x) for x in input().split( )]for y in range(C_col)]

# result = 0
# re_count = 0
# path = []
# for i in range(2): # 시작하는 행과 열
#     for j in range(3):
#         result = DFS(Candy_List,i,j,path)
#         if result >= 3:
#             re_count += 1
# #return re_count

# print(re_count)
