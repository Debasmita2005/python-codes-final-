'''
If an Employee object contains following details:
empcode, empname, Date of Joining, Salary
Write a program to serialize and deserialize this data.'''

import pickle

class Employee:
    def __init__(self, empcode, empname, doj, salary):
        self.empcode = empcode
        self.empname = empname
        self.doj = doj
        self.salary = salary

    def display(self):
        print(f"Code: {self.empcode}, Name: {self.empname}, DoJ: {self.doj}, Salary: {self.salary}")

def serialize_employee(emp, filename):
    with open(filename, 'wb') as f:
        pickle.dump(emp, f)
    print("Employee object serialized.")

def deserialize_employee(filename):
    with open(filename, 'rb') as f:
        emp = pickle.load(f)
    print("Employee object deserialized:")
    emp.display()

