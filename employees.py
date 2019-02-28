# create the class of the program
class Employees:
    Empnumber = 0

    # Create the constructor for initializing the class (Refers to as the instance of a class(Employees))
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        Employees.Empnumber += 1

    # The first method for counting the numbers of employees
    def EmployeesCount(self):
        print (Employees.Empnumber)

    # The second method for displaying the name of the employee and his/her salary
    def EmpDisplay(self):
        return "Name",self.name,"Salary",self.salary



