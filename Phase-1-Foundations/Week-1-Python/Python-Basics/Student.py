class Student:
    def __init__(self,name,*grade):
        self.name=name
        self.grade=list(grade)

    def avg(self):
        c=0
        for i in self.grade:
            if(i.upper()=='A'):
                c+=10
            elif(i.upper()=='B'):
                c+=8
            elif(i.upper()=='C'):
                c+=6
            elif(i.upper()=='D'):
                c+=4
        a = c/len(self.grade)
        if(a>8):
            return 'A'
        elif(a>6):
            return 'B'
        elif(a>4):
            return 'C'
        else:
            return 'D'

s = Student('Rudra','A','A','A','A','B')
print(s.avg())