# funclect.py

def setValue(a,b,c):
    x=a+b
    y=a-c
    return x,y


[x,y]=setValue(3,6,7)
print(x,y)


def userURIBuilder(server,port,**user):
    str="http://"+server+":"+port+"/?"
    for key in user.keys():
        str+=key+"="+user[key]+"&"
    return str

print(userURIBuilder("192.168.0.2","80",id="sks101",passwd="asd",name="mike"))



def times(a=10,b=20):
    return a*b
print(times())
print(times(5,6))    