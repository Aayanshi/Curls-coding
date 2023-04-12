class student:
    def __init__(self,name,rollno,age):
        self.name = name 
        self.rollno = rollno
        self.age = age
    
    def attendence(self):
        k = input("tell your attendence= ")
        print(f"{self.name} is {k}")


s1 = student("aaina",1,20)
s1.attendence()
print(s1)