str= input("enter: ")
c=input("letter: ")
words = str.split()
count = 0
for word in words:
    if word.lower().startswith(c):
        count += 1
print("Number of words starting with" ,c , count)
