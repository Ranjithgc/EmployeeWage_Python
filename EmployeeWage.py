"""
@Author: Ranjith G C
@Date: 2021-06-27
@Last Modified by: Ranjith G C
@Last Modified Time: 2021-06-28
@Title: Employee Wage Computation Program
"""
import random

# constants
PRESENT = 1
PART_PRESENT = 2

print("Welcome to Employee Wage Computation problem")

#Uc4: Refactored code using switcher

def employee_attendance():
    """
    Description:
        This function will calculate Daily Employee Wage Using Switcher
    """
    
    wage_per_hr = 20

    emp_Check = random.randint(0,2)
    if emp_Check == PRESENT:
        print("Employee is present")
        wrk_Hr = 8
    elif emp_Check == PART_PRESENT:
        print("Employee is part present")
        wrk_Hr = 4
    else:
        print("Employee is absent")
        wrk_Hr = 0
    employee_Wage = wage_per_hr * wrk_Hr 
    print("Employee Wage is - ", employee_Wage)

absent = 0
fullPresent = 1
part_present = 2

switcher = {
    0: absent,
    1: fullPresent,
    2: part_present
}

emp_Check = random.randint(0,2)
attendance = switcher.get(emp_Check)
employee_attendance()