str = "Not Class Member"
class GString:
    def __init__(self):
        self.str = "asb" 
    def set(self, msg):
        self.str = msg
    def print(self):
        print(self.str)
    def __del__(self):
        print("Instance is deleted!")
g = GString()
g.set("First Message")
g.print()
a=GString()
del(g)


print(a.str)