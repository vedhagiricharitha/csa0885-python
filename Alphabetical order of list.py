ab=[]
size=int(input("enter range"))
for i in range (1,size):
    ba=str(input("enter value: "))
    ab.append(ba)
ab.sort()
print(ab)
ab1=ab[::-1]
print(ab1)
