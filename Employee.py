'''
@Author: Nikita
@Date: 2022-03-29 20: 56: 00
@Last Modified by: Nikita
@Last Modified time: 2022-03-31 18: 52: 00
@Title: Checking Employee is Present or Absent
'''
import random

print("Welcome to Employee Wage Computation Programs")

Present=1
attendance=random.randint(0,1)

if attendance==1:   
    print("Employee is Present")
else:
    print("Employee is Absent")

