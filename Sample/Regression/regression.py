# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 22:48:26 2017

@author: zhengzhang
"""
import random
import matplotlib.pyplot as plt
from sample import Sample
import util
import regression_helper

VERBOSE = False

    
def compute_error(pred, truth):
    """ mean square error:
        sum of (pred[i] - truth[i])^2, divided by 2*length
    """
    # 计算E(w)
    error = 0
    n = len(pred)
    for i in range(n):
        error += (pred[i] - truth[i]) ** 2
    error /= 2 * n
    
    return error

def compute_grad(pred, truth, x):
    """ gradient is mean of (pred[i] - truth[i]) * x[i]
    """
    grad = 0
    n = len(pred)
    for i in range(n):
        grad += (pred[i] - truth[i]) * x[i]
    grad /= n

    
    return grad
    
if __name__ == "__main__":

    # num_samples = 100
    path = './faithful.csv'
    # loading data 
    f = open(path, 'r')
    raw_data = f.readlines()
    # print(raw_data)
    attributes = raw_data[0].strip().split(',')
    attributes= [item[1:-1] for item in attributes]
    print(attributes)
    data = [] 
    for item in raw_data[1:]:
        sample = Sample(attributes)
        item_list = item.strip().split(',')
        sample.set_attributes(item_list) #take the last two features
        sample.set_label(item_list[0].strip()[1:-1])
        data.append(sample)
    
    print(f"There are {len(data)} data items.")
    # print(data[0].get("eruptions"))
    # Make a random split of the data
    random.shuffle(data)
    
    train_data = data[:round(0.8*len(data))]
    test_data = data[round(0.8*len(data)):]

    # Plotting the randomly generated data
    d_x = [d.get(attributes[1]) for d in train_data]
    d_y = [d.get(attributes[2]) for d in train_data]
#    plt.ion()
    plt.figure(1)
    plt.scatter(d_x, d_y)
    plt.show()
    
    num_iter = 100
    steps = 0
    learning_rate = 0.01
    n = len(train_data)
    error_history = []
    error_last_iter = 0
    margin = 0.01

    # w is the parameter to be learned
    w = 0.5

    # training loop
    while True:
        
        # predict and compute error
        pred_y = [w*x for x in d_x]   
        # print(pred_y)
        error = compute_error(pred_y, d_y)
        error_history.append(error)
        #computer the change of error
        delta_error = error - error_last_iter
        error_last_iter = error
        
        plt.cla()
        plt.scatter(d_x, d_y)
        plt.plot(d_x, pred_y, 'r')
        title_str = "train error: %0.2f" % error
        plt.title(title_str)
        plt.show()
        
        steps += 1
        if abs(delta_error) <= margin or steps >= num_iter:
            break
        
        # gradient descent
        grad = compute_grad(pred_y, d_y, d_x)
        w -= learning_rate * grad
        
        if VERBOSE and input("cont? (y/n) ") == 'n':
            break

    # testing on test data
    d_x = [d.get(attributes[1]) for d in test_data]
    d_y = [d.get(attributes[2]) for d in test_data]
    pred_y = [w*x for x in d_x]   
    error = compute_error(pred_y, d_y)
    plt.figure(1)
    plt.scatter(d_x, d_y)
    plt.plot(d_x, pred_y, 'r')
    title_str = "test error: %0.2f" % error
    plt.title(title_str)
    plt.show()
        
    plt.plot(error_history)
    plt.title('training error')
    plt.show()