class dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def info(self):
            print(self.name,self.age)
    def make_sound(self):
            print("Bark")
class cat:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def info(self):
            print(self.name,self.age)
    def make_sound(self):
            print("Meow")
obj1 = dog("Spike",3)
obj2 = cat("Tom",2)

for i in (obj1,obj2):
    i.info()
    i.make_sound()
        