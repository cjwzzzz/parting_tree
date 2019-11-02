import matplotlib.pyplot as plt

if __name__=='__main__':
    initial_tree_x=[]
    initial_tree_y=[]
    with open('2d_Output_Sort.txt','r') as file1:
        for i in range(2):
            line=file1.readline()
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
                #pathdic[(int(line[index+1]),int(line[index+2]))]=[num]+child
                initial_tree_x.append(int(line[index+1]))
                initial_tree_y.append(int(line[index+2]))
                # if(i==0):
                #     num_firstly.append(num)
                #     #pathList_firstly=[int(line[index+1]),int(line[index+2])]+num_firstly+child
                index+=2*(num-1)+5
            else:
                initial_tree_x.append(int(line[index+1]))
                initial_tree_y.append(int(line[index+2]))                
                #pathdic[(int(line[index+1]),int(line[index+2]))]=[num]+[0,0]
                index+=5


    ax=plt.gca()
    ax.spines['top'].set_color('none')
    ax.spines['right'].set_color('none')   
    plt.scatter(initial_tree_x,initial_tree_y,c='g',s=10)
    plt.title('initial_tree')
    plt.show()