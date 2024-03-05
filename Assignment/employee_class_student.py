#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 10:11:08 2017

@author: xg7
"""

class Employee:
    
    def __init__(self): 
        self.name = None
        self.ID = None
        self.department = None
        self.jobTitle = None
        
##Alternatively, we can using the following to initilialize
## but in this exercise, we use the above for practice purpose.
#    def __init__(self, name, ID, department, jobTitle):
#        self.name = name
#        self.ID = ID
#        self.department = department
#        self.jobTitle = jobTitle
#    
    #setter
    ## set_name is an example for setters.
    def set_name(self, name):
        self.name = name
    
    
    #### please complete the following methods
    def set_ID(self, ID):
        pass
        self.ID = ID

    def set_department(self, department):
        pass
        self.department = department

    def set_jobTitle(self, jobTitle):
        pass
        self.jobTitle = jobTitle
    
    #getter
    ## get_name is an example for getters.
    def get_name(self):
        return self.name
    
    #### please complete the follwing methods
    def get_ID(self):
        pass
        return self.ID
    
    def get_department(self):
        pass
        return self.department
    
    def get_jobTitle(self):
        pass
        return self.jobTitle


if __name__ == '__main__':
    emp1 = Employee()
    emp1.set_name("Susan Meyers")
    emp1.set_ID("47899")
    emp1.set_department("Accounting")
    emp1.set_jobTitle("Vice President")
    ### Please input the information of the rest employees in the table
    emp2 = Employee()
    emp3 = Employee()
    
    print(emp1.get_name(), emp1.get_ID(), emp1.get_department(), emp1.get_jobTitle() )
    ### Please complete the following code to show employee information, using the getter you defined
    print(emp2)
    print(emp3)
    