'''
@Author: Nikita
@Date: 2022-03-29 20: 56: 00
@Last Modified by: Nikita
@Last Modified time: 2022-03-31 19: 17: 00
@Title: Calculating Daily Wage
'''

import random

print("Welcome to Employee Wage Computation Programs")
fullTime=1
wagePerHr=20
employeeWage=0
Present=1
attendance=random.randint(0,1)

if attendance==1:   
    print("Employee is Present")
    empHr=8
    employeeWage=empHr*wagePerHr
    print("Daily Employee Wage for Employee is ",+employeeWage)

else:
    print("Employee is Absent")
    empHr=0