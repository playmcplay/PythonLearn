a=[]
for i in range(101,200) :
    for j in range (2,i):
        if i%j==0:
            break
    else:
        a.append(i)
count=0
for n in a:
    print (n,end=' ')
    count+=1
    if count%10==0:
        print()
