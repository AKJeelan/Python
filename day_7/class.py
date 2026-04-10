class Person:

    # Constructor
    def __init__(self,name):
        self.name = name;

    def talk(self):
        print(f"Hello i'm {self.name}")

# Creating a object.
person = Person("Abdul Jeelan")
person.talk()

person1 = Person("Khadar")
person1.talk()