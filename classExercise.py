# classExercise.py

class Person:
    num_person=0
    def __init__(self):
        
        self.name = "default name"
        Person.num_person += 1
    
    def print(self):
        print("My name is {0}",self.name)

p1=Person()
p1.print()

p2=Person()
p2.name="shin"
p2.print()

print("인스턴스개수:",Person.num_person)
print("숫자:{0}".format(Person.num_person))

p1.age=4

print(p1.age)

print(object.__str__(p1.age))

Person.title = "New title"

print(Person.title)