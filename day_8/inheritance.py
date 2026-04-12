class Person:
    def __init__(self,f_name,l_name):
        self.f_name = f_name
        self.l_name = l_name

class Student(Person):
    def printName(self):
        print(f"Hello {self.f_name} {self.l_name}. How are you ?")


student = Student("Abdul","Jeelan");
student.printName()