a,b=map(int,input().split())
q=[]
for i in range(a,b+1):
    if(i!=2):    
            for y in range(2,i):
                if i%y==0:
                    q.append(i)
                    break

count=0
for z in q:
    count0=0
    for r in range(1,z+1):
                if z%r==0:
                    count0+=1
             
                
    if (count0%2==0):
        count=count+1
                
print(count)