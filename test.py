class Person:
    def __init__(self,name = "jj", age = 18):
        self.age = age
        self.name = name
    def speak(self):
        print("my name is {} ".format(self.name))

class Student(Person):
    def __init__(self,name): 
        self.name = name      
        #super().__init__()
        print("....")
    

if __name__ == "__main__":
    p = Person("jason", 24)
    s = Student('kk')
    s.speak()
