"""
@Author: Ranjith G C
@Date: 2021-06-27
@Last Modified by: Ranjith G C
@Last Modified Time: 2021-06-27
@Title: Employee Wage Computation Program
"""
import random

print("Welcome to Employee Wage Computation problem")

#Uc1: Check Employee is present or absent

def employee_attendance():
    """
    Description:
        This function will check if employee is present or absent
    """
    present = 1

    emp_Check = random.randint(0,2)
    if emp_Check == present:
        print("Employee is present")
    else:
        print("Employee is absent")

employee_attendance()