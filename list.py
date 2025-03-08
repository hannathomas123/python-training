if __name__ == '__main__':
    N = int(input())
    list=[]
    for _ in range(N):
        row=input().split()
        if(row[0]=='insert'):
            list.insert(int(row[1]),int(row[2]))
        elif(row[0]=='print'):
            print(list)
        elif(row[0]=='remove'):
            list.remove(int(row[1]))
        elif(row[0]=='append'):
            list.append(int(row[1]))
        elif(row[0]=='sort'):
            list.sort()
        elif(row[0]=='pop'):
            list.pop()
        else:
            list.reverse()
       
        
