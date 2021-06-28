"""
@Author: Ranjith G C
@Date: 2021-06-27
@Last Modified by: Ranjith G C
@Last Modified Time: 2021-06-27
@Title: Employee Wage Computation Program
"""
import random

print("Welcome to Employee Wage Computation problem")

#Uc1:
#Uc2:
def employee_attendance():
    """
    Description:
        This function will check if employee is present or absent
    """
    #constants
    PRESENT = 1
    
    wage_per_hr = 20

    emp_Check = random.randint(0,2)
    if emp_Check == PRESENT:
        print("Employee is present")
        wrk_Hr = 8
    else:
        print("Employee is absent")
        wrk_Hr = 0
    employee_Wage = wage_per_hr * wrk_Hr 
    print("Employee Wage is - ", employee_Wage)

employee_attendance()