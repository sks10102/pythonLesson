# DemoDict.py

price={'car':'3000만원','laptop':'8만원','bike':'150만원'}
print(type(price),price)

print(price["car"])
price['ring'] = '200만원'
#반복구문(~.items(), ~.values(), ~.keys())
for item in price.items():
    print(item)

#반복구문(~.items(), ~.values(), ~.keys())
for k,v in price.items():
    print(k,v)

del price['ring']

print(price)
print(price)

print(price.keys())
print(price.values())

p=price
price['mouse']='5천원'
print(type(p))
print(p)
print(price)

for item in price.keys():
    print(item)