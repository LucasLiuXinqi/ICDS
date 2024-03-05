#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 10:49:18 2020

@author: xg7
"""
import pickle as pk
from employee_class_student import *

def main(quit_system):
    try:
        Database = open('emp_database.dat', 'rb')
        emp_dict = pk.load(Database)
        Database.close()
        #print("Database loaded successfully.\n")
    except (FileNotFoundError, EOFError):
        emp_dict = {}
        #print("No Database Found. Creating one.\n")

    MENU = ("1.Look up\n"
            "2.Add new employee\n"
            "3.Change employee information\n"
            "4.Delete employee\n"
            "5.Quit\n"
            "Please select an operation: ")

    option = input(MENU)

    if option not in "12345":
        print("Invalid option:", option)

    if option == '1':
        lookUp = input("Please input the ID: ")
        try:
            theEmployee = emp_dict[lookUp]
            print("{ID}/{name}/{dept}/{jobtitle}".format(ID=theEmployee.get_ID(),
                                                         name=theEmployee.get_name(), dept=theEmployee.get_department(),
                                                         jobtitle=theEmployee.get_jobTitle()))
        except KeyError:
            print("No such an ID.")
    elif option == '2':
        empInfo = input("Please input name/ID/department/job title: ")
        empInfo = empInfo.split('/')
        try:
            k_id = empInfo[1]
            emp_dict[k_id] = Employee()
            emp_dict[k_id].set_name(empInfo[0])
            emp_dict[k_id].set_ID(empInfo[1])
            emp_dict[k_id].set_department(empInfo[2])
            emp_dict[k_id].set_jobTitle(empInfo[3])
        except IndexError:
            print("Incorrect input format.")

    elif option == '3':
        # change account information by ID, please look at the screenshots for prompts
        pass
        lookUp = input("Please input the ID: ")
        try:
            theEmployee = emp_dict[lookUp]
            print("{ID}/{name}/{dept}/{jobtitle}".format(ID=theEmployee.get_ID(),
                                                         name=theEmployee.get_name(), dept=theEmployee.get_department(),
                                                         jobtitle=theEmployee.get_jobTitle()))
            emp_dict[lookUp].set_name(input('Please input a new name:'))
            emp_dict[lookUp].set_department(input('Please input a new department:'))
            emp_dict[lookUp].set_jobTitle(input('Please input a new job title:'))

        except KeyError:
            print("No such an ID.")





    elif option == '4':
        # delete account information by ID, please look at the screenshots for prompts
        pass
        try:
            delete = input("Please input the ID for delete:")
            del emp_dict[delete]
        except:
            print("No such an ID.")


    elif option == '5':
        Database.close()
        quit_system = True
        return quit_system
    else:
        print("How did you get here?")

    Database = open('emp_database.dat', 'wb')
    # use pickle method to save the updated dictionary to the file
    pass
    
    Database.close()
    return quit_system


if __name__ == '__main__':

    quit_system = False
    while not quit_system:
        quit_system = main(quit_system)
