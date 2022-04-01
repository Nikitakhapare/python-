'''
@Author: Nikita
@Date: 2022-03-29 20: 51: 00
@Last Modified by: Nikita
@Last Modified time: 2022-04-01 : 8: 32
@Title: uc9 Store Day and Daily Wage Along with Total Wage
'''

import random
from re import A


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


def calculateWage():
    """
        Description:
            Function to Calculate Hour
        Parameter:
            No Parameter
        Return:
            returning the total working Hour
    """
    list = []
    daylist = []
    a = 0
    totalEmpHours = 0
    totalDays = 0
    while a < 20:
        checkAttendance = random.randint(0, 1)
        attendancechake = attendance(checkAttendance)
        if attendancechake == 1:
            check = random.randint(1, 2)
            empWorkingHr = workingHr(check)
            dailyWage = wagePerHour*empWorkingHr
            list.append(dailyWage)
            totalEmpHours += empWorkingHr
            daylist.append(a)

        else:
            a -= 1

        if totalEmpHours >= 100:
            break
        a += 1

    totalWage = (wagePerHour*totalEmpHours)
    print("Total Working Days in month ", a+1)
    print("Total Working Hour is ", totalEmpHours)
    print("Daily Wage of Employee is ", list)
    print("Day list ", daylist)

calculateWage()
