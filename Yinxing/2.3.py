t=("spring","summer","autumn")
with open("file2.txt","w") as file:
    for i in t:
        file.write(i+"\n")
with open("file2.txt","a") as file:
    file.write("winter\n")
with open("file2.txt","r") as file:
    lines=file.readlines()
    last_two_lines=lines[-2:]
print(last_two_lines)