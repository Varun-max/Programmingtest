def conf_room(input_lst):                                  

    lst_lines_rooms = open('rooms.txt', 'r').readlines()
    final_lst = []             
    final_full_lst = []        
    ult_lst = []               

    for l in range(len(lst_lines_rooms)):
        il_2 = int(''.join(input_lst[2].split(':')))        
        il_3 = int(''.join(input_lst[3].split(':')))        

        for z in range(2, len(lst_lines_rooms[l].split(','))-1, 2):
            nl_z = int(''.join(lst_lines_rooms[l].split(',')[z].split(':')))         
            nl_z1 = int(''.join(lst_lines_rooms[l].split(',')[z+1].split(':')))

            if (il_2 >= nl_z and il_3 <= nl_z1 and int(input_lst[0]) <= int(lst_lines_rooms[l].split(',')[1])):   
                final_full_lst.append(lst_lines_rooms[l].split(',')[0])                                           
                final_lst.append(int(lst_lines_rooms[l].split(',')[0].split('.')[0]))                             
            
    minn_val = abs(int(input_lst[1])-final_lst[0])                                
    
    for jx in range(1,len(final_lst)):
        if minn_val > abs(int(input_lst[1])-final_lst[jx]):
            minn_val = abs(int(input_lst[1])-final_lst[jx])                      

    lst_idx_minn = []                                                            
    
    for ilc in range(len(final_lst)): 
        if abs(int(input_lst[1])-final_lst[ilc]) == minn_val:
            lst_idx_minn.append(ilc)
    
    for kj in lst_idx_minn:                                                     
        ult_lst.append(final_full_lst[kj])    
    return ','.join(ult_lst)                                                    


print(conf_room([5,8,"10:30","11:30"]))                                         # calling the function conf_room and passing input list as the argument to the function.

