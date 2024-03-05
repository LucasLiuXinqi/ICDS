from sample import Sample, plot_samples
from matplotlib import pyplot as plt


LABELS = ('Setosa', 'Versicolor', 'Virginica')
COLORS = ('b', 'g', 'c', 'm', 'y', 'k')
MARKS = ('o', 'v', '^', '<', '>', '8',
           's', 'p', '*', 'h', 'H', 'D', 'd')



def knn(p, data, k):
    """ Compute the distance between p to every sample in data,
        set p's label to the label of the maximum of samples
        within the k nearest neighbors

        # p is a SAMPLE object
        # data is a list of SAMPLE object
        # k is int
    """

    """ Steps:
        1. Iterate through samples in data and store the
           distance from p in the dictionary "distance"; key is the
           distance, value is the sample.
        2. Creat a sorted list of samples according to ascending
           order of the distances.
        3. In the dictioary "label_votes", stores number of votes
           in each label among the top-k nearest samples
        4. Assign p the most popular label
    """
    distances = {} #dict of distance
    ##--below, input your code for computeing the distance--##
    for sample in data:
        distance = p.distance(sample)   # 通过Sample class的distance操作计算distance
        if distance in distances:   # 将sample以distance作为key添加到dictionary中
            distances[distance].append(sample)
        else:
            distances[distance] = [sample]
   
    
    
    ##--end of your code--##
    
    sorted_samples = [] #the sorted list of samples in data
    ##--below, input your code for sortig the samples--##
    for key in sorted(distances.keys()):
        sorted_samples.extend(distances[key])   # sorted_samples中的元素是每一个sample
    
    k_nearest_neighbors = sorted_samples[:k]    # 取sorted——samples的前k个 (距离最近的k个)
    # print(k_nearest_neighbors)
    
    ##--end of your code--##
     
    label_votes = { l:0 for l in LABELS } #dict of votes per label {'Setosa': 0, 'Versicolor': 0, 'Virginica': 0}
    
    ##--below, input your code for finding the max label--##
    for x in k_nearest_neighbors:
        label_votes[x.get_label()] += 1
    
    # print("label_votes", label_votes)
    max_label = 'Setosa' #modify it to a correct expression
    ## above forces a fixed label: remove them
    max_vote = 0
    for l in LABELS:
        if label_votes[l] > max_vote:
            max_label = l
    ##--end of your code--##
    p.set_label(max_label)
    

if __name__ == "__main__":
    # load data
    f = open('iris.csv', 'r')
    raw_data = f.readlines()
    attributes = raw_data[0].split(',')[2:4] #take the last two features
    # print(attributes) ['"petal.length"', '"petal.width"']
    for i in range(len(attributes)):
        attributes[i] = attributes[i].strip()[1:-1]     # 将['"petal.length"', '"petal.width"']变为['petal.length', 'petal.width']
    data = [] 
    for item in raw_data[1:]:
        sample = Sample(attributes)
        item_list = item.split(',')
        sample.set_attributes(item_list[2:4]) #take the last two features
        sample.set_label(item_list[-1].strip()[1:-1])
        data.append(sample)
        
    K = 3
    def onclick(event):
        # Creating a new point and finding the k nearest neighbours
        new = Sample(attributes)
        new.set_attributes([str(event.xdata), str(event.ydata)])
        knn(new, data, K)
        # draw the new point
        data.append(new)
        plt.scatter(event.xdata, event.ydata, \
                      label = new.get_label(), \
                      marker = MARKS[LABELS.index(new.get_label())], \
                      color = COLORS[LABELS.index(new.get_label())])
        plt.draw()
    # start plotting
    fig = plt.figure()
    cid = fig.canvas.mpl_connect('button_press_event', onclick)  
    plot_samples(data, attributes[0], attributes[1])
   