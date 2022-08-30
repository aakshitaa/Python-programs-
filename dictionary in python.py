d1 = {}
list1 = []
n = int(input("enter number of students\n"))
i = 0
var = 0
name = ""
m=int(input("enter number of subjects\n"))
for i in range(n):
    name = input("input name of student\n")
    for j in range(m):
        marks = int(input("input marks of student\n"))
        list1.append(marks)
    d1[name] = list1
    list1 = []
list2 = d1[name]
print (d1)
list3=[]
for i in d1:
    avg=(sum(d1[i])/m)
    print (i,avg)
