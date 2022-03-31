'''
@Author: Nikita
@Date: 2022-03-29 20: 51: 00
@Last Modified by: Nikita
@Last Modified time: 2022-04-01 : 1: 33
@Title: Calculating  Wage till condition of working hour or days reached
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
    switcher = {1: 8, 2: 4}
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
    switcher = {0: 0, 1: 1}
    return switcher[checkAttendance]


wagePerHour = 20
fullTime = 1
partTime = 0
empWorkingHr = 0
totalWorkingDays = 0
maxWorkingDays = 20
totalEmpHours = 0
maxWorkingHr = 100

for i in range(20):

    checkAttendance = random.randint(0, 1)
    attendancechake = attendance(checkAttendance)
    if attendancechake == 1:
        check = random.randint(1, 2)
        empWorkingHr = workingHr(check)
        totalEmpHours += empWorkingHr

    if totalEmpHours >= 100:
        break

totalWage = (wagePerHour*totalEmpHours)
print("Total Working Days in month ", i+1)
print("Total Working Hour is ",totalEmpHours)
print("Monthly Employee Wage= ", totalWage)

