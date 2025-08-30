name = (input("Please enter your name: ")).lower()
age = int(input("Please enter your age: "))
hair_color = (input("Please enter the color of your hair: ")).lower()
eye_color = (input("Please enter your eye color: ")).lower()

# Create Adult class
class Adult():    
    def __init__(self, age, name, hair_color, eye_color):
        self.name = name
        self.age = age
        self.hair_color = hair_color
        self.eye_color = eye_color
    def can_drive(self):   
        if self.age >= 18:
            print(f"{self.name} is {self.age} and is old enough to drive")   
# Create Subclass called Child
class Child(Adult):
    def can_drive(self):
        if self.age <= 18:
            print(f"{self.name} is {self.age} and is too young to drive") 
child_1 = Child()  
child_1.can_drive()      