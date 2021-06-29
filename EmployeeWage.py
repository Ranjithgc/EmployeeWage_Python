"""
@Author: Ranjith G C
@Date: 2021-06-27
@Last Modified by: Ranjith G C
@Last Modified Time: 2021-06-28
@Title: Employee Wage Computation Program
"""
import random

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

def getWorkHours(total_Working_Hours):
    """
    Description:
        this function calculate working hours
    """
    print("Total working hours:", total_Working_Hours)

def calculateWage():
    """
    Description:
        this function calculate employee wage
    Return:
        this function return total employee wage of a month
    """
    wage_Dict = {}
    wage_Per_Hour = 20
    working_Days = 0
    total_Working_Hours = 0
    maximum_Working_Days = 20
    maximum_Working_Hours = 100
    total_Wage = 0
    while working_Days < maximum_Working_Days and total_Working_Hours < maximum_Working_Hours:
        attendance = random.randint(0,2)
        attendanceStatus = switcher.get(attendance)
        working_Hours = calculateHour(attendanceStatus)
        daily_Wage = working_Hours * wage_Per_Hour
        total_Wage += working_Hours * wage_Per_Hour
        total_Working_Hours += working_Hours
        wage_Dict[working_Days] = {
            "daily_wage" : daily_Wage,
            "total_wage" : total_Wage
        }
        working_Days += 1
    getWorkHours(total_Working_Hours)
    print("Daily Wage - ", wage_Dict)
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