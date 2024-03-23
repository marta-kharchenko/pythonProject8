class Employee:
    def __init__(self, name, id_number, department):
        self.name = name
        self.id_number = id_number
        self.department = department

    def display(self):
        return print(f'Information about the employee: \nEmployee name: {self.name} \nEmployee ID: {self.id_number} \nDepartment: {self.department}')


Employee_Name = input('Please enter the employee name: ')
ID_Num = input('Please enter the employee ID number: ')
Department = input('Please enter the department name: ')
employee = Employee(Employee_Name, ID_Num, Department)
employee.display()