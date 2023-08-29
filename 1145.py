X,Y = map(int,input().split())
count = 1
for i in range(1,Y+1):
    if count == X:
        print(i,end='\n')
        count = 1
    else:
        print(i,end=" ")
        count = count+1