class Student:
    def __init__(self):
        print("This is default constructor of Student class")
    def __init__(self,name,sec,height):
        self.name = name
        self.sec= sec
        self.height=height
        print("This is parametersied constructor of Student class")
    def __init__(self,name,sec,height):
        self.name = "Arun"
        self.sec= "C"
        self.height=25
        print("This is non-parametersied constructor of Student class")
class BraveStudent(Student):
    quality="Brave"
    print("This is BraveStudent class inheriting Student class quality: ", quality)

class ExellentStudent(BraveStudent):
    quality="Excellence"
    print("This is ExellentStudent class inheriting BraveStudent class quality: ",quality)

class PerfectStudent(ExellentStudent):
    quality="perfect"
    print("This is PerfectStudent class inheriting ExellentStudent class quality: ",quality)
    

a1=Student()
a2=Student("Aditya","A",25)
a3=Student()
b=BraveStudent()
c=ExellentStudent()
d=PerfectStudent()