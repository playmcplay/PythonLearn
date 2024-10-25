year=int(input("请输入年份:"))
f=0
if(year%4==0 and year%100!=0)or(year%400==0):
    f=1
else:
    f=0
if f==1:
    print("是闰年")
else:
    print("不是闰年")
