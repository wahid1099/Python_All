# Create a Student class
class Student :

    # initialise class variable
    counter = 0

    # Constructor method
    def __init__(self,name,age) :

        # instance variable or object attributes
        self.name = name
        self.age = age

        # incrementing the class variable by 1
        # whenever new object is created
        Student.counter += 1

    # Create a method for printing details
    def printDetails(self) :
        print(self.name,self.age,"years old")

    

# Create an object of Student class with attributes
student1 = Student('Ankit Rai',22)
student2 = Student('Aishwarya',21)
student3 = Student('Shaurya',21)

# Print the total no. of objects cretaed 
print("Total number of objects created: ",Student.counter)
