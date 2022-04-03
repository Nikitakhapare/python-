'''
@Author: Nikita
@Date: 2022-04-03 18: 30: 00
@Last Modified by: Nikita
@Last Modified time: 2022-04-03 18:30:00
@Title: Take User Input and Replace String
'''
old_string = "Hello <<UserName>>, How are you?"
input = input("Enter Name: ")

if len(input)>3:
    new_string = old_string.replace("<<UserName>>", input)
    print(new_string)
    
else: 
    print("Enter a Valid User Name: ")
    
