def harmonic(n):
    s=0.0
    for i in range(1,n+1):
        s+=1/i
    return round(s,1)
n=int(input("输入一个数: "))
h_list=[]    
for i in range(1,n+1):
    h_num=harmonic(i)
    h_list.append(h_num)
print(h_list)
print(sum(h_list))
