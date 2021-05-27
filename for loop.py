N=["A","B","C"]
for x in N:
    print(x)

#for loop for string
for x in "kajal":
    print(x)

#for integer 1st method
for x in [1,2,3,4]:
    print(x)
#2nd method
y=[1,2,3,4]
for n in y:
    print(n)

for x in "kajal":
    print(x,end="")

#break statement use in for
y=[1,2,3,4]
for n in y:
    print(n)
    if n==3:
        break
    

y=[1,2,3,4]
for n in y:
    if n==3:
        break
    print(n)

y=[1,2,3,4]
for n in y:
    if n==3:
        continue
    print(n)

x=["kajal","charu","best friend"]
for y in x:
    if y=="charu":
        continue
    print(y)

for x in range(10):
    print(x)

for x in range(10):
    print(x,end=" ")

for x in range(2,9):
    print(x)

for x in range(1,50,2):
    print(x)

for x in range(10):
    print(x)
else:
    print("hello kajal")

name=["kajal","charu"]
hobby=["cricket","dance"]
for x in name:
   for y in hobby:
    print(x,y)

    
    
    
    
