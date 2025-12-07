# If any one pass parameter in single string so with the use of '@classmethod' we can split it and make it as our requirement

class Student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno

    @classmethod
    def converter(cls,str):
        return cls(str.split(",")[0],int(str.split(",")[1]))
    
s1=Student.converter('Rudra,26')
print(s1.name)
print(s1.rollno)