#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 20:18:17 2022

@author: bing
"""

from matplotlib import pyplot as plt


class Sample:
    def __init__(self, attributes:list):
        self.attributes = attributes   # epresents the names of the columns in the dataset
        self.data = {}  # a Python dictionary storing the (attribute, value) pairs of a data item
        self.label = None
    
    def set_attributes(self, raw_item:str):
        
        ## fill the self.data with the raw_item, for self.data
        ## keys are the self.attributes
        ## values are extracted from raw_item
        raw_item = raw_item.split(',')      # raw_item should looks like 4.6,3.1,1.5,.2,"Setosa" => ['4.6', '3.1', '1.5', '.2', '"Setosa"']
        for i in range(len(raw_item)):
            if raw_item[i][0].isnumeric():
                raw_item[i] = float(raw_item[i].strip())   # 这个strip是在做什么
            else:
                raw_item[i] = raw_item[i].strip()[1:-1]    # 这个strip是在做什么
            # [4.6, 3.1, 1.5, '.2', 'Setosa']

        for i in range(len(self.attributes)):
            # attributes: "sepal.length","sepal.width","petal.length","petal.width","variety"
            self.data[self.attributes[i]] = raw_item[i]    # {'sepal.length': 4.6, ...}
                                                            # 这里每一个dic只储存一个数据吗

        
    def get(self, attr:str):
        
        return self.data[attr]
    
    def set_label(self, label):
        self.label = label
    
    def __add__(self, sample):
        new_s = Sample(self.attributes)    # 这一步有什么作用？
        for attr in new_s.attributes:
            if type(self.data[attr]) is str:
                new_s.data[attr] = ''
                continue
            new_s.data[attr] = self.data[attr] + sample.data[attr]
        return new_s
        # 将sample的数值与本来的数值相加

    def __truediv__(self, n):
        new_s = Sample(self.attributes)
        pass
        for k in self.data.keys():
            if type(self.data[k]) is str:
                continue
            new_s.data[k] = self.data[k]/n
        return new_s
            
        

def plot_samples(samples:list, attr_x, attr_y):
    
    colors = ['r', 'g', 'b', 'c', 'm', 'k']
    shapes = ['v', 'o', 'x', 'd', '+', 's',]
    
    for s in samples:
        x = s.get(attr_x)
        y = s.get(attr_y)
        if s.get('variety')=="Virginica":
            c = colors[0]
            s = shapes[0]
        elif s.get('variety')=='Versicolor':
            c = colors[1]
            s = shapes[1]
        else: ##satosa
            c = colors[2]
            s = shapes[2]
    
        plt.plot(x, y, s+c)
    plt.show()
        
    

if __name__ == "__main__":
    
    f = open('iris.csv', 'r')
    raw_data = f.readlines()
    
    attributes = raw_data[0].split(',') #raw_data[0] :"sepal.length","sepal.width","petal.length","petal.width","variety" /n
                                        #attributes = ["sepal.length","sepal.width","petal.length","petal.width","variety", "/n"]
    
    for i in range(len(attributes)):
        attributes[i] = attributes[i].strip()[1:-1]    # 这个strip是为了将字符串两端的双引号去掉？

        
    samples = []
    
    for item in raw_data[1:]:
        sample = Sample(attributes)
        sample.set_attributes(item)
        samples.append(sample)

    # plot_samples(samples, attributes[1], attributes[3])
        
    