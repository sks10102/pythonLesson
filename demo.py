# demo.py

strA="Hello python"
x=5
y=3.14

print(strA)
print(len(strA))
print(y)

for x in [3,5]:
    if x==5:       
        print(x,"""
        영원히\n
        살아요
        """)
    else:
        print(x,'슬퍼요')

strA="python"
print(strA[2:4],strA[-1])

friend=5
Friend=6
print(dir())
print(type(friend))
print("c:\\work\\test.txt")

# 자료형
colors=["red","green","blue"]
colors.append('black')
colors.remove('red')
colors+=["pink"]

colors.sort()

print(colors)
