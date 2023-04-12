from parent import Parent
class Child(Parent):
    def __init__(self, mother, father, bp, name):
        self.name = name
        super().__init__(mother,father,bp)

    def id(self):
        print(f" name  is {self.name} parents are {self.mother} and {self.father} having {self.bp}")    

obj = Child("mum","pa","be+","aaina")      
obj.id()
obj.bloodgroup()
print(obj)  
        