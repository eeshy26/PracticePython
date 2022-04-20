class parent():
    def __init__(self,name,age,weight):
        self.name=name
        self.age=age
        self.weight=weight

class child1():
    def __init__(self,name,age,weight,height):
        self.name=name
        self.age=age
        self.weight=weight
        self.height=height
        
class child2(parent,child1):
    def __init__(self,name,age,weight,height):
        self.name=name
        self.age=age
        self.weight=weight
        self.height=height
        
    p=parent("Jim",39,"45kg")
    ch1=child1("Lily",7,"19kg","1.2m")

    print(p.weight)
    print(ch1.name)
    print(ch1.height)
