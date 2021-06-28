
"""
@Author: Ranjith G C
@Date: 2021-06-27
@Last Modified by: Ranjith G C
@Last Modified Time: 2021-06-28
@Title: Employee Wage Computation Program
"""
import random
#constants
WORKING_DAYS = 20

print("Wellcome to employee wage computation")

def calculateHour(attendance):
    """
    Description:
        this function determine the work hours
    Parameter:
        attendance is used to determine work hour of employee
    Return:
        the functution return 8 or 4 or 0 value as work hour
    """
    if attendance == isFullTime:
        work_Hour = 8
    elif attendance == isPartTime:
        work_Hour = 4 
    else:
        work_Hour = 0
    return work_Hour

def calculateWage():
    """
    Description:
        this function calculate employee wage
    Return:
        this function return total employee wage of a month
    """
    wage_Per_Hour = 20
    total_Wage = 0
    for day in range(WORKING_DAYS):
        attendance = random.randint(0,2)
        attendanceStatus = switcher.get(attendance)
        working_Hours = calculateHour(attendanceStatus)
        total_Wage += working_Hours * wage_Per_Hour
    return total_Wage

absent = 0
isFullTime = 1
isPartTime = 2

switcher = {
    0: absent,
    1: isFullTime,
    2: isPartTime,
}

print("Total employee wage for month is:",calculateWage())
