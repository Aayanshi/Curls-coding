class Parent:
    def __init__(self,mother,father,bp):
        self.mother = mother
        self.father = father
        self.bp = bp

    def bloodgroup(self):
        print(f"bloodgroup is {self.bp}")  

obj = Parent("mum","pa","b+") 
obj.bloodgroup()
print(obj, obj.mother)       