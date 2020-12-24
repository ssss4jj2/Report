

def DFS(L_graph,count):
    #path.append(begin_nm)
    count_result = []
    for i in range(6):
        for j in range(6):
                L_data = L_graph[i][j] # 출발하는 노드
                
                for i_L in range(i,6):
                    for j_L in range(j,6):
                        # 행이 0일때
                        if i_L == 0: 
                            # 행이 0이고, 열이 0일때
                            if j_L == 0:
                                if (L_data == L_graph[i_L+1][j_L]) or (L_data == L_graph[i_L][j_L+1]):    ## 하 or  우
                                    count = count + 1
                                    continue

                            # 행이 0이고, 열이 6일때
                            elif j_L == 6:
                                if L_data == L_graph[i_L+1][j_L] or L_data == L_graph[i_L][j_L-1]:    ## 하 or 좌
                                    count = count + 1

                            # 행이 0이고, 열이 0과 6이 아닐때
                            else:
                                if L_data == L_graph[i_L+1][j_L] or L_data == L_graph[i_L][j_L-1] or L_data == L_graph[i_L][j_L+1]:    ## 하
                                    count = count + 1

                        # 행이 0과 6이 아닐때
                        elif 0 < i_L < 6:
                            # 행이 0과 6이 아니고, 열이 0일때
                            if j_L == 0:
                                if L_data == L_graph[i_L-1][j_L] or L_data == L_graph[i_L+1][j_L] or L_data == L_graph[i_L][j_L+1]:      ## 상
                                    count = count + 1

                                
                            #행이 0과 6이 아니고, 열이 6일때
                            elif j_L == 6:
                                if L_data == L_graph[i_L-1][j_L] or L_data == L_graph[i_L+1][j_L] or L_data == L_graph[i_L][j_L-1]:      ## 상
                                    count = count + 1
                            
                        # 행이 6일때
                        else:
                            # 행이 6이고, 열이 0일때
                            if j_L == 0:
                                if L_data == L_graph[i_L-1][j_L] or L_data == L_graph[i_L][j_L+1] :      ## 상
                                    count = count + 1

                                
                            # 행이 6이고, 열이 6일때
                            elif j_L == 6:
                                if L_data == L_graph[i_L-1][j_L] or L_data == L_graph[i_L][j_L-1]:      ## 좌
                                    count = count + 1

                            
                            #행이 6이고, 열이 0과 6이 아닐때
                            else:
                                if L_data == L_graph[i_L-1][j_L] or L_data == L_graph[i_L][j_L+1] or L_data == L_graph[i_L][j_L-1]:      ## 상
                                    count = count + 1
            if count >=3:
                count_result.append(count)
                return count_result
    # if count >= 3 :
    #     count_result.append(count)
    #     return count_result

    
    # for i in range(6):
    #     for j in range(6):
    #             L_data = L_graph[i][j]
    #             for i_L in range(i,6):
    #                 for j_L in range(j,6):
                        
    #                     # 행이 0일때
    #                     if i_L == 0: 
    #                         # 행이 0이고, 열이 0일때
    #                         if j_L == 0:
    #                             if (L_data == L_graph[i_L+1][j_L]) or (L_data == L_graph[i_L][j_L+1]):    ## 하 or  우
    #                                 count = count + 1
    #                                 continue
    #                                 #DFS(L_graph,count)
                                        
    #                             # elif L_data == L_graph[i][j+1]:    ## 우
    #                             #     count = count + 1
    #                             #     DFS(L_graph,i,j+1,count)
    #                             #return count
                                
    #                         # 행이 0이고, 열이 6일때
    #                         elif j_L == 6:
    #                             if L_data == L_graph[i_L+1][j_L] or L_data == L_graph[i_L][j_L-1]:    ## 하 or 좌
    #                                 count = count + 1
    #                                 #DFS(L_graph,count)
                                        
    #                             # elif L_data == L_graph[i][j-1]:    ## 좌
    #                             #     count = count + 1
    #                             #     #DFS(L_graph,count)
                                    
    #                         # 행이 0이고, 열이 0과 6이 아닐때
    #                         else:
    #                             if L_data == L_graph[i_L+1][j_L] or L_data == L_graph[i_L][j_L-1] or L_data == L_graph[i_L][j_L+1]:    ## 하
    #                                 count = count + 1
    #                                 #DFS(L_graph,count)
                                        
    #                             # elif L_data == L_graph[i][j-1]:    ## 좌
    #                             #     count = count + 1
    #                             #     #DFS(L_graph,count)
                                        
    #                             # elif L_data == L_graph[i][j+1]:    ## 우
    #                             #     count = count + 1
    #                             #     #DFS(L_graph,count)
    #                             #return count
                            
    #                     # 행이 0과 6이 아닐때
    #                     elif 0 < i_L < 6:
    #                         # 행이 0과 6이 아니고, 열이 0일때
    #                         if j_L == 0:
    #                             if L_data == L_graph[i_L-1][j_L] or L_data == L_graph[i_L+1][j_L] or L_data == L_graph[i_L][j_L+1]:      ## 상
    #                                 count = count + 1
    #                                 #DFS(L_graph,count)
                                
    #                             # elif L_data == L_graph[i+1][j]:    ## 하
    #                             #     count = count + 1
    #                             #     #DFS(L_graph,count)
                                        
    #                             # elif L_data == L_graph[i][j+1]:    ## 우
    #                             #     count = count + 1
    #                             #     #DFS(L_graph,count)
    #                             #return count
                                
    #                         #행이 0과 6이 아니고, 열이 6일때
    #                         elif j_L == 6:
    #                             if L_data == L_graph[i_L-1][j_L] or L_data == L_graph[i_L+1][j_L] or L_data == L_graph[i_L][j_L-1]:      ## 상
    #                                 count = count + 1
    #                                 #DFS(L_graph,count)
                                
    #                             # elif L_data == L_graph[i+1][j]:    ## 하
    #                             #     count = count + 1
    #                             #     #DFS(L_graph,count)
                                        
    #                             # elif L_data == L_graph[i][j-1]:    ## 좌
    #                             #     count = count + 1
    #                             #     #DFS(L_graph,count)
    #                             #return count
                            
    #                     # 행이 6일때
    #                     else:
    #                         # 행이 6이고, 열이 0일때
    #                         if j_L == 0:
    #                             if L_data == L_graph[i_L-1][j_L] or L_data == L_graph[i_L][j_L+1] :      ## 상
    #                                 count = count + 1
    #                                 #DFS(L_graph,count)
    #                             # elif L_data == L_graph[i][j+1]:    ## 우
    #                             #     count = count + 1
    #                             #     #DFS(L_graph,count)
    #                             #return count
                                
    #                         # 행이 6이고, 열이 6일때
    #                         elif j_L == 6:
    #                             if L_data == L_graph[i_L-1][j_L] or L_data == L_graph[i_L][j_L-1]:      ## 상
    #                                 count = count + 1
    #                                 #DFS(L_graph,count)
    #                             # elif L_data == L_graph[i][j-1]:    ## 좌
    #                             #     count = count + 1
    #                             #     #DFS(L_graph,count)
    #                             #return count
                            
    #                         #행이 6이고, 열이 0과 6이 아닐때
    #                         else:
    #                             if L_data == L_graph[i_L-1][j_L] or L_data == L_graph[i_L][j_L+1] or L_data == L_graph[i_L][j_L-1]:      ## 상
    #                                 count = count + 1
    #                                 #DFS(L_graph,count)
    #                             # elif L_data == L_graph[i][j+1]:    ## 우
    #                             #     count = count + 1
    #                             #     #DFS(L_graph,count)
    #                             # elif L_data == L_graph[i][j-1]:    ## 좌
    #                             #     count = count + 1
    #                             #     #DFS(L_graph,count)
    #                             #return count
    # if count >= 3 :
    #     count_result.append(count)
    #     return count_result
    # #return count


C_row = 7
C_col = 7

Candy_List = [[int(x) for x in input().split( )]for y in range(C_col)]

result = 0

print ("result = ",DFS(Candy_List,result))    
