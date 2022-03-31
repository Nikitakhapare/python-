'''
@Author: Nikita
@Date: 2022-03-29 20: 56: 00
@Last Modified by: Nikita
@Last Modified time: 2022-04-01 : 12: 58
@Title: Calculating Employee Wage for a Month
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
    switcher={ 1: 8, 2: 4}
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
totalWorkingDays=0
maxWorkingDays=20
totalEmpHours=0

while(totalWorkingDays<maxWorkingDays):
    checkAttendance=random.randint(0,1)
    attendancechake=attendance(checkAttendance)
    if attendancechake==1:   
        check = random.randint(1,2)
        empWorkingHr=workingHr(check)
        totalWorkingDays+=1
        totalEmpHours=totalEmpHours+empWorkingHr    
  
totalWage=(wagePerHour*totalEmpHours)
print("Employee Working Days is ", totalWorkingDays)
print("Monthly Employee Wage= ",totalWage)


