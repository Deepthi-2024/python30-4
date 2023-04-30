str=input("Enter a string : ")
str1 = []
for i in str:
    if i not in str1:
        str1.apprnd(i)
for i in range(0,len(str1)):
    print(i,end=",")