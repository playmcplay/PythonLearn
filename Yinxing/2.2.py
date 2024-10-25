def search(list,left,right,target):
    if right >=left:
        mid=(left+right)//2
        if list[mid]==target:
            return mid
        elif list[mid]>target:
            return search(list,left,mid-1,target)
        else:
            return search(list,mid+1,right,target)
    else:
        return  -1
list=[1,13,26,33,45,55,68,72,83,99]
target=int(input("Enter the number to find the target number:"))
if(search(list,0,len(list)-1,target)==-1):
    print("The number does not exist")
else:
    print("The number",target,"is",search(list,0,len(list)-1,target))
