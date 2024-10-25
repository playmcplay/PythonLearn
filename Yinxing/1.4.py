total_sum=0
ji_sum=0
ou_sum=0
for n in range(1,101):
    total_sum+=n
    if n%2==0:
        ou_sum+=n
    else:
        ji_sum+=n
print("所有数之和:",total_sum)
print("奇数和:",ji_sum)
print("偶数和:",ou_sum)
'''
total_sun=0
ji_sun=0
ou_sun=0
i=0
while i<=100:
    if i%2==0:
        ou_sun+=i
    else :
        ji_sun+=i
'''