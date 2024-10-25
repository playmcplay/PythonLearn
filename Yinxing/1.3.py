s=int(input("请输入数字数目:"))
numbers=[]
for _ in range(s):
    n=int(input("请输入整数:"))
    numbers.append(n)
print('lenth=:',len(numbers))
print('max=:',max(numbers))
print('min=:',min(numbers))
print('sum=:',sum(numbers))
print('aver=:',sum(numbers)/len(numbers))
