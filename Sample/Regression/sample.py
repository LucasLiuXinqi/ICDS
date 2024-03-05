#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 12:54:37 2022

@author: bing
"""

from matplotlib import pyplot as plt


class Sample:
    def __init__(self, attributes:list):
        self.attributes = attributes
        self.data = {}
        
    
    def set_attributes(self, raw_item:list):
            
        self.data = {}
        for i in range(len(self.attributes)):
            try:
                self.data[self.attributes[i]] = float(raw_item[i].strip())
            except ValueError:
                self.data[self.attributes[i]] = raw_item[i].strip()[1:-1]
        # print("data", self.data)
            
    def get(self, attr:str):
        return self.data[attr]
    
    
    def set_label(self, label):
        self.label = label
    
    
    def get_label(self):
        try:
            return self.label
        except AttributeError:
            return None
        
    def distance(self, p):
        d = 0
        for attr in self.attributes:
            d += (self.get(attr) - p.get(attr))**2
        return d**0.5
            
    
    def __add__(self, sample):
        new_s = Sample(self.attributes)
        # print(self.data)
        
        for attr in new_s.attributes:
            if type(self.data[attr]) is str:
                new_s.data[attr] = ''
                continue
            new_s.data[attr] = self.data[attr] + sample.data[attr]
        return new_s
            
    
    def __truediv__(self, n):
        
        new_s = Sample(self.attributes)
        for k in self.data.keys():
            if type(self.data[k]) is str:
                continue
            new_s.data[k] = self.data[k]/n
        return new_s
            
        

def plot_samples(samples:list, attr_x, attr_y):
    #some settings 
    LABELS = ('Setosa', 'Versicolor', 'Virginica')
    COLORS = ('b', 'g', 'c', 'm', 'y', 'k')
    MARKS = ('o', 'v', '^', '<', '>', '8',
               's', 'p', '*', 'h', 'H', 'D', 'd')
    
    if samples[0].get_label():
        for s in samples:
            x = s.get(attr_x)
            y = s.get(attr_y)
            m = MARKS[LABELS.index(s.get_label())]
            c = COLORS[LABELS.index(s.get_label())]
            plt.plot(x, y, m+c)
    else:
        for s in samples:
            x = s.get(attr_x)
            y = s.get(attr_y)
            m = 'o'
            c = 'b'
            plt.plot(x, y, m+c)
    plt.show()
        
    

if __name__ == "__main__":
    
    f = open('faithful.csv', 'r')
    raw_data = f.readlines()
    # print(raw_data)
    attributes = raw_data[0].strip().split(',')
    # print(attributes)
    for i in range(len(attributes)):
        attributes[i] = attributes[i].strip()[1:-1]
        
    samples = []
    
    for item in raw_data[1:]:
        sample = Sample(attributes)
        item_list = item.split(',')
        sample.set_attributes(item_list)
        samples.append(sample)
    plot_samples(samples, attributes[1], attributes[2])
        
    


    