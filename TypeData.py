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