# TypeData.py
a = [1,2,3]
b = a
a[0] = 38
print(id(a),a)
print(id(b),b)
b=a[:]
a[0] = 49
print(id(a),a)
print(id(b),b)
print(b)

print(True and True and True)
print(True or False or False)

print(5//2)
print(5//3)


#score = int(input('Input Score: '))
score=40
if 90 <=score <=100:
    grade='A'
elif 70<= score:
    grade='B' 
elif 50<= score:
    grade='C'
else:
    grade='F'


print("grade : %s" %(grade))

i=0
while i<=3:
    print(i)
    i+=1
else:
    print("Completed")

lst = ["apple",100,3.14]
for item in lst:
    print(item, type(item))

d={"apple":100, "orange":100, "banana":300}
for k,v in d.items():
    print(k,v)

i=3
for j in [1,2,3,4,5,6,7,8,9]:
    print('{0},{a10},{a100},{jj}'.format(j,a10=j*10,a100=j*100,jj=j))

for i in range(5):
    print(i*2)

d = {"apple":100, "kiwi":200}

for k in d.keys():
    print(k)
    
for k in d.items():
    print(k)

    
for k in d.values():
    print(k)

for i in [1,2,3,4,5,6,7,8,9,10]:
    if i>5:
        break
    print("*"*i)

    
for i in range(20,True,-2):
    if 2<i<8:
        continue    
    print("*"*i)
print(list(range(1,100,2)))
print(tuple(range(1,100,2)))

print(tuple(range(1,100,2)))