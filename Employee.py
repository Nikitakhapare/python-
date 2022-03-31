'''
@Author: Nikita
@Date: 2022-03-29 20: 56: 00
@Last Modified by: Nikita
@Last Modified time: 2022-03-31 : 20: 14
@Title: Calculating Employee Wage Using Case Statement
'''

import random
def workingHr(check):
    """
        Description:
            Function to Switch case
        Parameter:
            check is to get the random number of working_hours in emply_wage_presence function
        Return:   
            returning the check variable
    """
    switcher={ 1: 8, 2: 4, 0: 0}
    return switcher[check]

def attendance(checkAttendance):
    """
        Description:
            Function to Switch case
        Parameter:
            check is to get the random number of Employee Attendance
        Return:   
            returning the check variable
    """
    switcher={0:0,1:1}
    return switcher[checkAttendance]
    
wagePerHour=20
fullTime=1
partTime=0
empWorkingHr=0
checkAttendance=random.randint(0,1)
attendance=attendance(checkAttendance)

if attendance==1:   
    print("Employee is Present")
    check = random.randint(0,2)
    empWorkingHr=workingHr(check)
    empchack=random.randint(0,1)
    if empchack==1:
           empHr=8
    elif empchack==2:
            empHr=4   
    employeeWage=empHr*wagePerHour
    print("Daily Employee Wage for Employee is ",+employeeWage)

else:
    print("Employee is Absent")
    empHr=0

totalWage=(wagePerHour*empWorkingHr)
print("Employee Wage= ",totalWage)


