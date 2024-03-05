# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 15:23:36 2016

@author: zhengzhang
"""
import random
import dice_helper

class Dice:
    def __init__(self, sides=2):
        self.n_sides = sides
        self.bounds = [x/sides for x in range(0, sides)]
        
        self.bounds.append(1.0)
        print("the bounds", self.bounds)
        self.point = None
        self.lands = 0
   
    def set_bounds(self, r):
        assert len(r) == len(self.bounds)
        self.bounds = r
        
    def get_bounds(self):
        return self.bounds
                
    def roll(self):
        self.point = random.uniform(0, 1)
# replace the following line with you code
# it should set self.point as a random var in [0, 1]
# return which side the dice lands on
        return dice_helper.roll(self)

if __name__ == "__main__":       
    d = Dice(2)
    ''' make a biased dice '''
    d.set_bounds([0.0, 0.3, 1])  
    ones = 0
    num_rolls = 1000
    for i in range(num_rolls):
        ones += d.roll()
    print("the dice is:", ones/float(num_rolls))
    