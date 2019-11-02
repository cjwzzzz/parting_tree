class Net:
    def __init__(self, netId, subnet_id,pin1_X, pin1_Y,pin1_Layer, pin2_X, pin2_Y,pin2_Layer,flag):
        self.netId = netId
        self.subnet_id = subnet_id
        self.pin1_X = pin1_X
        self.pin1_Y = pin1_Y
        self.pin1_Layer = pin1_Layer        
        self.pin2_X = pin2_X
        self.pin2_Y = pin2_Y
        self.pin2_Layer = pin2_Layer              
        self.flag = flag
# netList=[]
# pathList=[]
# debug_jiaochadian=0
# with open('2d_Pinlist0.txt', "r") as file0 , open('2d_Output_Sort.txt','r') as file1:
#     num=int(file0.readline().split()[0])
#     for j in range(num):          #net shumu           
#         line=file0.readline().split()
#         leng=(len(line)-1)/2
#         for k in range(leng):
#             pinlist.append((int(line[2*k]),int(line[2*k+1])))
#         subnet_num=int(line[1])
#         netId=int(line[0])
#         subnet_id=int(line[1])
#         pin1_X=int(line[2])
#         pin1_Y=int(line[3])
#         pin1_Layer=int(line[4])

#         pin2_X=int(line[5])
#         pin2_Y=int(line[6])
#         pin2_Layer=int(line[7])
#         flag=int(line[8])
#         netObj = Net(netId,  subnet_id ,pin1_X, pin1_Y,pin1_Layer, pin2_X, pin2_Y,pin2_Layer, flag)
#         netList.append(netObj)
#         pinlist0=list(file1.readline().split()[1:]) #保存路径坐标
#         #print(pinlist0)
#         pinlist=[]
#         length=int(len(pinlist0)/2)  #路径中点的数目

#         for k in range(length):
#             pinlist.append((int(pinlist0[2*k]),int(pinlist0[2*k+1])))    #引脚保存为 路径 点对
#         #print(pinlist)

#         try:
#             index1=pinlist.index((pin1_X,pin1_Y))            
#             index2=pinlist.index((pin2_X,pin2_Y))
#         except ValueError as e:
#             print(pinlist0)
#             print(pinlist)
#             print("ID{0}".format(j))
#             print((pin1_X,pin1_Y))   
#             print((pin2_X,pin2_Y))
#         minIndex=min(index1,index2)
#         maxIndex=max(index1,index2)
#         indexlist0=list(file1.readline().split()[1:])   #路径文件中交叉点列表
#         if(len(indexlist0)==0):
#             pathList.append(pinlist[minIndex:maxIndex])  #输出到文件时注意空格

            

#             for i in range(subnet_num-1):
#                 line = file0.readline().split()
#                 subnet_id=int(line[1])
#                 pin1_X=int(line[2])
#                 pin1_Y=int(line[3])
#                 pin1_Layer=int(line[4])       
#                 pin2_X=int(line[5])
#                 pin2_Y=int(line[6])
#                 pin2_Layer=int(line[7]) 
#                 flag=int(line[8])      
#                 index1=pinlist.index((pin1_X,pin1_Y))            
#                 index2=pinlist.index((pin2_X,pin2_Y))   
#                 minIndex=min(index1,index2)
#                 maxIndex=max(index1,index2)     
#                 pathList.append(pinlist[minIndex:maxIndex])  #输出到文件时注意空格
#                 netObj = Net(netId,  subnet_id ,pin1_X, pin1_Y,pin1_Layer, pin2_X, pin2_Y,pin2_Layer, flag)
#                 netList.append(netObj)
#         else:
#             for x in indexlist0:
#                 if(int(x) >= minIndex and int(x)<= maxIndex):
#                     debug_jiaochadian+=1
#             if(debug_jiaochadian>=3):
#                 print(j)
#             debug_jiaochadian=0
#             for i in range(subnet_num-1):
#                 line = file0.readline().split()
#                 subnet_id=int(line[1])
#                 pin1_X=int(line[2])
#                 pin1_Y=int(line[3])
#                 pin1_Layer=int(line[4])       
#                 pin2_X=int(line[5])
#                 pin2_Y=int(line[6])
#                 pin2_Layer=int(line[7]) 
#                 flag=int(line[8])      
#                 try:
#                     index1=pinlist.index((pin1_X,pin1_Y))            
#                     index2=pinlist.index((pin2_X,pin2_Y))
#                 except ValueError as e:
#                     print(pinlist0)
#                     print(pinlist)
#                     print("ID{0}".format(j))
#                     print((pin1_X,pin1_Y))   
#                     print((pin2_X,pin2_Y))
#                 minIndex=min(index1,index2)
#                 maxIndex=max(index1,index2)     
#                 for x in indexlist0:
#                     if(int(x) >= minIndex and int(x)<= maxIndex):
#                         debug_jiaochadian+=1     
#                 if(debug_jiaochadian>=3):
#                     print(j)
#                     debug_jiaochadian=0  
#                     continue
#                 debug_jiaochadian=0                                   
#                 pathList.append(pinlist[minIndex:maxIndex])  #输出到文件时注意空格
#                 netObj = Net(netId,  subnet_id ,pin1_X, pin1_Y,pin1_Layer, pin2_X, pin2_Y,pin2_Layer, flag)
#                 netList.append(netObj)
# with open('2d_Output_Sort.txt','r') as file1:
#     for x in netList:
def yes1(cur):
    global list1,list0,pinlist
    global pathdic
    for x in list0:
        #print(cur)  问题：丢失了转弯节点
        pin_List_Write.append((x[1],x[2]))
        path_List_Write.append((x[1],x[2]))
        if(x[0]==0):
            first_Flag='0'
        else:
            first_Flag='1'

        cur=(x[3],x[4])
        while(1):            
            print(cur)
            path_List_Write.append(cur)
            if(pathdic[cur][0]>1 ):
                if(cur in pinlist):
                    last_Flag='0'
                    for i in range(pathdic[cur][0]):                       
                        list1.append((0,cur[0],cur[1],pathdic[cur][2*i+1],pathdic[cur][2*i+2]))            #进入函数
                else:
                    last_Flag='1'
                    for i in range(pathdic[cur][0]):                        
                        list1.append((1,cur[0],cur[1],pathdic[cur][2*i+1],pathdic[cur][2*i+2]))            #进入函数                    
                pin_List_Write.append('\n')
                path_List_Write.append('\n')

                    
                break          #when stop while(1)?
            if(pathdic[cur][0]==0):
                last_Flag='0'
                pin_List_Write.append('\n')
                path_List_Write.append('\n')
                break
            if(cur  in pinlist and pathdic[cur][0]==1):
                last_Flag='0'
                pin_List_Write.append('\n')
                path_List_Write.append('\n')
                pin_List_Write.append(cur)
                path_List_Write.append(cur)
                cur=(pathdic[cur][1],pathdic[cur][2])
            else:
                cur=(pathdic[cur][1],pathdic[cur][2])
    list0=[]
    if(len(list1)!=0):
        for x in list1:
            pin_List_Write.append((x[1],x[2]))
            path_List_Write.append((x[1],x[2]))
            if(x[0]==0):
                first_Flag='0'
            else:
                first_Flag='1'
            cur=(x[3],x[4])
            while(1):
                path_List_Write.append(cur)
                print(cur)
                if(pathdic[cur][0]>1):
                    pin_List_Write.append('\n')
                    path_List_Write.append('\n')
                    if(cur in pinlist):
                        last_Flag='0'
                        for i in range(pathdic[cur][0]):
                            
                            list1.append((0,cur[0],cur[1],pathdic[cur][2*i+1],pathdic[cur][2*i+2]))            #进入函数
                    else:
                        last_Flag='1'
                        for i in range(pathdic[cur][0]):
                            
                            list1.append((1,cur[0],cur[1],pathdic[cur][2*i+1],pathdic[cur][2*i+2]))            #进入函数  
                        #list0.append(pathdic[cur][2*i+1])
                    break  
                if(pathdic[cur][0]==0):
                    last_Flag='0'
                    pin_List_Write.append('\n')
                    path_List_Write.append('\n')
                    break                    
                if(cur  in pinlist):
                    last_Flag='0'
                    pin_List_Write.append('\n')
                    path_List_Write.append('\n')
                    pin_List_Write.append(cur)
                    path_List_Write.append(cur)
                    cur=(pathdic[cur][1],pathdic[cur][2])
                else:
                    cur=(pathdic[cur][1],pathdic[cur][2])
        #when stop while(1)?

    list1=[]   
    if(len(list0)!=0):
        yes1(cur)





list0=[]
list1=[]
pathdic={}
pinlist=[]
index=0
pathList_firstly=[]
num_firstly=[]
path_List_Write=[]
pin_List_Write=[]


with open('2d_Pinlist0.txt', "r") as file0 , open('2d_Output_Sort.txt','r') as file1:
    for i in range(3):
        line=file1.readline()
    line=line.split()
    #print(line)
    length=int(line[-1])
    #print(length)
    child=[]

    for i in range(length):
        num_firstly=[]
        child=[]
        #print(i)
        num=int(line[index+3])   
        if(num!=0):     
            for j in range(num):
                child.append(int(line[2*j+4+index]))
                child.append(int(line[2*j+5+index]))
            pathdic[(int(line[index+1]),int(line[index+2]))]=[num]+child
            if(i==0):
                num_firstly.append(num)
                pathList_firstly=[int(line[index+1]),int(line[index+2])]+num_firstly+child
            index+=2*(num-1)+5
        else:
            pathdic[(int(line[index+1]),int(line[index+2]))]=[num]+[0,0]
            index+=5
        #print(child)
        #print(index)

        
    for i in range(4):
        line=file0.readline().split()
    num=int(line[1])
    for i in range(num):
        pinlist.append((int(line[2*i+2]),int(line[2*i+3])))
       

#print(pathdic)

list0=[]
list1=[]
# pathList=[(77,245,1,77,244),(77,244,1,77,243),(77,243,1,77,242),(77,242,1,77,241),(77,241,0,0,0)]
# pathdic={}
# pathdic[(77,245)]=(1,77,244)
# # print(pathdic)
# pathdic[(77,244)]=(1,77,243)
# pathdic[(77,243)]=(1,77,242)
# pathdic[(77,242)]=(1,77,241)
# pathdic[(77,241)]=(0,0,0)


#注意    遇到原始引脚一定换行
cur=(pathList_firstly[0],pathList_firstly[1])
cur_index=0

if(pathList_firstly[2]>1):
    #temp=[]
    #temp.append((cur))
    for i in range(int(pathList_firstly[2])):
        
        list0.append((0,cur[0],cur[1],pathList_firstly[2*i+3],pathList_firstly[2*i+4]))
    #list0.append(temp)
        #list0.append(pathList_firstly[2*i+4])
    yes1(cur)
else:
    pin_List_Write.append(cur)
    print(cur)
    path_List_Write.append(cur)
    cur=(pathdic[cur][1],pathdic[cur][2])

    while(1):
        path_List_Write.append(cur)
        if(pathdic[cur][0]==0): #终止点一定是 pin？  需要验证
            print(0)
            break
        if(pathdic[cur][0]>1):  #有可能也是 原始Pin，需分类，标记出pin
            if(cur in pinlist):
                last_Flag='0'
                for i in range(pathdic[cur][0]):                       
                    list0.append((0,cur[0],cur[1],pathdic[cur][2*i+1],pathdic[cur][2*i+2]))            #进入函数
            else:
                last_Flag='1'
                for i in range(pathdic[cur][0]):                        
                    list0.append((1,cur[0],cur[1],pathdic[cur][2*i+1],pathdic[cur][2*i+2]))            #进入函数      
                #list0.append(pathdic[cur][2*i+2])
            pin_List_Write.append('\n')
            yes1(cur)
            break  
        if(cur  in pinlist and pathdic[cur][0]==1):
            pin_List_Write.append('\n')
            pin_List_Write.append(cur)
            cur=(pathdic[cur][1],pathdic[cur][2])
        else:
            cur=(pathdic[cur][1],pathdic[cur][2])    

print(path_List_Write)







