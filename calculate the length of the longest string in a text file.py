f=open("count.txt","r+")
s1=f.read()
s1=s1.split()
m=0
s=0
for i in s1:
    if m<len(i):
        m=len(i)
        s=i
print(s)
print(m)
f.close()