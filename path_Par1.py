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

def yes1(cur):
    global list1,list0,pinlist
    global pathdic
    global pin_List_Write,pin_List_Over
    global path_List_Write,path_List_Over
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
            #print(cur)
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
                pin_List_Write.append(cur)  
                pin_List_Write.append(first_Flag+last_Flag)   
                pin_List_Over.append(pin_List_Write)    
                pin_List_Write=[]        
                #pin_List_Write.append('\n')
                path_List_Over.append(path_List_Write)
                #path_List_Write.append('\n')
                path_List_Write=[]

                    
                break          #when stop while(1)?
            if(pathdic[cur][0]==0):
                last_Flag='0'
                pin_List_Write.append(cur) 
                pin_List_Write.append(first_Flag+last_Flag) 

                pin_List_Over.append(pin_List_Write)    
                pin_List_Write=[]      
                #pin_List_Write.append('\n')
                path_List_Over.append(path_List_Write)
                #path_List_Write.append('\n')
                path_List_Write=[]
                break
            if(cur  in pinlist and pathdic[cur][0]==1):
                last_Flag='0'
                pin_List_Write.append(cur)
                pin_List_Write.append(first_Flag+last_Flag) 
                pin_List_Over.append(pin_List_Write)    
                pin_List_Write=[]     
                #pin_List_Write.append('\n')
                path_List_Over.append(path_List_Write)
                #path_List_Write.append('\n')
                path_List_Write=[]
                pin_List_Write.append(cur)
                path_List_Write.append(cur)
                cur=(pathdic[cur][1],pathdic[cur][2])
                first_Flag='0'              #attention: 没有2个以上节点，但进入新的一行
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
                #print(cur)
                if(pathdic[cur][0]>1):
                    pin_List_Write.append(cur)
                    pin_List_Write.append(first_Flag+last_Flag) 
                    pin_List_Over.append(pin_List_Write)    
                    pin_List_Write=[]      
                    #pin_List_Write.append('\n')
                    path_List_Over.append(path_List_Write)
                    #path_List_Write.append('\n')
                    path_List_Write=[]
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
                    pin_List_Write.append(cur)
                    pin_List_Write.append(first_Flag+last_Flag) 
                    pin_List_Over.append(pin_List_Write)    
                    pin_List_Write=[]      
                    #pin_List_Write.append('\n')
                    path_List_Over.append(path_List_Write)
                    #path_List_Write.append('\n')
                    path_List_Write=[]
                    break                    
                if(cur  in pinlist):
                    last_Flag='0'
                    pin_List_Write.append(cur)
                    pin_List_Write.append(first_Flag+last_Flag) 
                    pin_List_Over.append(pin_List_Write)    
                    pin_List_Write=[]       
                    #pin_List_Write.append('\n')
                    path_List_Over.append(path_List_Write)
                    #path_List_Write.append('\n')
                    path_List_Write=[]
                    pin_List_Write.append(cur)
                    path_List_Write.append(cur)
                    cur=(pathdic[cur][1],pathdic[cur][2])
                    first_Flag='0'
                else:
                    cur=(pathdic[cur][1],pathdic[cur][2])
        #when stop while(1)?

    list1=[]   
    if(len(list0)!=0):
        yes1(cur)




if __name__=='__main__':
    list0=[]
    list1=[]
    pathdic={}
    pinlist=[]
    index=0
    pathList_firstly=[]
    num_firstly=[]
    path_List_Write=[]
    pin_List_Write=[]   
    path_List_Over=[]
    pin_List_Over=[]
    

    with open('2d_Pinlist0.txt', "r") as file0 , open('2d_Output_Sort.txt','r') as file1:
        line=file0.readline()
        for i in range(20):
            path_List_Write=[]
            pin_List_Write=[]
            pinlist.clear()
            pathdic.clear()
            index=0
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
                first_Flag='0'
                pin_List_Write.append(cur)
                #print(cur)
                path_List_Write.append(cur)
                cur=(pathdic[cur][1],pathdic[cur][2])           

                while(1):
                    path_List_Write.append(cur)
                    if(pathdic[cur][0]==0): #终止点一定是 pin？  需要验证
                        last_Flag='0'
                        pin_List_Write.append(cur)
                        pin_List_Write.append(first_Flag+last_Flag) 
                        pin_List_Over.append(pin_List_Write)    
                        pin_List_Write=[]         
                        #pin_List_Write.append('\n')
                        path_List_Over.append(path_List_Write)
                        #path_List_Write.append('\n')
                        path_List_Write=[]
                        #print(0)
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
                        pin_List_Write.append(cur)
                        pin_List_Write.append(first_Flag+last_Flag) 
                        pin_List_Over.append(pin_List_Write)    
                        pin_List_Write=[]         
                        #pin_List_Write.append('\n')
                        path_List_Over.append(path_List_Write)
                        #path_List_Write.append('\n')
                        path_List_Write=[]
                        yes1(cur)
                        break  
                    if(cur  in pinlist and pathdic[cur][0]==1):
                        last_Flag='0'
                        pin_List_Write.append(cur)
                        pin_List_Write.append(first_Flag+last_Flag) 
                        pin_List_Over.append(pin_List_Write)    
                        pin_List_Write=[]         
                        #pin_List_Write.append('\n')
                        path_List_Over.append(path_List_Write)
                        #path_List_Write.append('\n')
                        path_List_Write=[]
                        pin_List_Write.append(cur)
                        path_List_Write.append(cur)
                        cur=(pathdic[cur][1],pathdic[cur][2])
                        first_Flag='0'
                    else:
                        cur=(pathdic[cur][1],pathdic[cur][2])       

    print(path_List_Over)
    print('lueluelue')
    print(pin_List_Over)
    







