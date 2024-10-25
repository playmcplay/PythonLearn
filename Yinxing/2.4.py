data1 = b'Xiaoming'
data2 = b'student'
with open("my.dat", "wb") as file:
    file.write(data1)
    file.write(data2)
# 读取文件的后7个字节
with open("my.dat", "rb") as file:
    file.seek(-7, 2)  # 移动到文件末尾前的7个字节
    last_seven_bytes = file.read(7)
    utf8_string=last_seven_bytes.decode('utf8')
print(utf8_string)
544514566465456
