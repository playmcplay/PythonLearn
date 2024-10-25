def _area(a, b, c):
    s = (a + b + c) / 2
    area=(s*(s-a)*(s-b)*(s-c))**0.5
    return area


a = float(input("输入第一条边长a:"))
b = float(input("输入第二条边长b:"))
c = float(input("输入第三条边长c:"))

while (a > 0 and b > 0 and c > 0 and b + c > 0 and a + b > 0 and a + c > 0) :
    print(f"三角形的面积是: {_area(a,b,c)}")
    break
    
