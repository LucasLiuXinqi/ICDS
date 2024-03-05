#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 21:10:30 2022

@author: bing
"""


class Cluster:  # used to represent a cluster in the clustering.
    
    def __init__(self, label:int, attributes):
        
        self.label = label
        self.attributes = attributes    # the attributes that are used to generate this cluster
        self.samples = []   # the data items belonging to this cluster, which is a list of instances of Sample class


    def add_sample(self, sample):
        self.samples.append(sample)



    def get_center(self):   # a method for computing the center of this cluster
        '''
        return the centroid of the cluster
        the centroid is an instance of Sample
        '''
        pass
        if self.samples:
            center = self.samples[0]
            for s in self.samples[1:]:
                center += s

            center = center / len(self.samples)
            return center   # center是否也是一个包含了多种数值的dictionary
        return None