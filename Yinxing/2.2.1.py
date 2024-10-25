def search(list,left,right,target):
    left,right=0,len(list)-1
    while left<=right:
        mid=(left+right)//2
        if list[mid]==target:
            return mid
        elif list[mid]>target:
            right=mid-1
        else:
            left=mid+1
    return -1
list=[1,13,26,33,45,55,68,72,83,99]
target=int(input("Enter the number to search: "))
if search(list,0,len(list)-1,target)==-1 :
    print("The number does not exist")
else:
    print("The number",target,"is",search(list,0,len(list)-1,target))
