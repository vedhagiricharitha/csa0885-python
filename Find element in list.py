def check(li,element):
    for i in li:
         if i==element:
             return True  
    return False

li=[]
len=int(input("Range: "))
for i in range (0,len):
    ele=int(input("Enter Elements: "))
    li.append(ele)


element=int(input("Enter Element to find: "))
print("Check if",element,"is in",(li))
print(check(li,element))
