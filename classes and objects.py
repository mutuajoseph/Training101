# A class is blueprint(prototype) i.e a collection of related properties and methods
# When creating classes we do use the keyword CLASS
# Always start with a capital letter

class Student:
    # class variables are variables that are shared across all instances
    reg_number = ""
    grade = ""
    total = 0
    average = 0

    # This refers to a constructor
    def __init__(self,math,eng,kiswa,sci,ssr):
        self.total = self.totalMarks(math,eng,kiswa,sci,ssr)
        self.calculateAv(self.total)

    # METHODS
    # self pops up after defining the method totalMarks
    # This therefore tells us that this is no longer a function but a method
    def totalMarks(self,math,eng,kiswa,sci,ssr):

        # In order to access the total we use a self. the item you want to access
        total = math+eng+kiswa+sci+ssr
        return total

    def calculateAv(self,tot):
        self.average = tot/5

    # def findGrade(self,average):

# Variable Brian is an object of a class
# An object is an instance of a class
Brian = Student(85,78,77,84,69)
Esther = Student(95,87,63,87,89)

print(Brian.total)
print(Esther.average)

