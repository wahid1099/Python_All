import random

class studentData:
    def __init__(self,student_name,mark):
        self.student_name=student_name
        self.mark=mark
        self.student_id=random.randint(0,500)

    
    def store_date(self):
        f = open("wahid.txt", "a")
        a = f.write(f"Student_Id:{self.student_id} Student_Name:{self.student_name} and Student_Mark:{self.mark}\n")
        f.close()
        
    





print("How many students data you want to add")
n=int(input())
for i in range(n):
    student_name=input("Student Name:")
    mark=int(input("Student Mark:"))
    studetndata=studentData(student_name,mark)
    studetndata.store_date()

