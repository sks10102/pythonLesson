# DemoList.py


colors=["red","green","blue"]

print(len(colors))
print(colors)
print(colors[0])

colors.append("white")

print(colors)

colors.insert(1,"yellow")

for item in colors:
    print(item)

print(colors.pop())
print(colors.pop())
print(colors.pop())
print(colors.pop())
print(colors)


#set 연습

a = {1,2,3,4}
b = {3,4,5,6,6}

print(a.union(b))
print(a.difference(b))
print(a.intersection(b))

#tuple은 주로 묶어서 처리

c = ("쇼니","초니",3)
d = (3,4)

print(c[0])

def calc(a,b):
    return a*b,a+b

print(set(list(calc(*d))))


