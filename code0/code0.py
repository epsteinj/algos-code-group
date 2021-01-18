import numpy as np
import matplotlib.pyplot as plt

#param int n: number of digits of pi to be summed
def Average(n):
    #open file
    pi = open('pi', 'r')
    #read n digits, convert to numpy array of type int
    digits = np.array(list(pi.read(n)), dtype=int)
    #take the mean and return it
    mean = np.mean(digits)
    return mean

print(Average(1000000000))

#instantiate x and run Average over all x to instantiate y
x = list(range(1, 1001))
y = list(map(Average, x))

#graph using matplotlib
plt.autoscale()
plt.scatter(x, y, s=5)
plt.title('Average of Pi vs Number of Digits of Pi')
plt.xlabel('# of digits of pi')
plt.ylabel('average')