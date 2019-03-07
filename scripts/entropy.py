from math import log
import numpy as np


def entropy(p):
    if p == 0 or p == 1:
        return 0
    else:
        p2 = 1 - p
        return -p * log(p, 2) - p2 * log(p2, 2)


def gain(n, start_num, a, b):
    start = start_num / n
    aa, pp = a / n, b / a
    pp2 = np.array([entropy(p) for p in pp])
    return entropy(start) - aa.dot(pp2)


# For all
n = 14.0
start_num = 9.0

# Wind
a = np.array([8.0, 6.0])
b = np.array([6.0, 3.0])
print 'wind', gain(n, start_num, a, b)

# Humidity
a = np.array([7.0, 7.0])
b = np.array([3.0, 6.0])
print 'humidity', gain(n, start_num, a, b)

# Temp
a = np.array([4.0, 6.0, 4.0])
b = np.array([2.0, 4.0, 3.0])
print 'temp', gain(n, start_num, a, b)

# Outlook
a = np.array([5.0, 4.0, 5.0])
b = np.array([2.0, 4.0, 3.0])
print 'outlook', gain(n, start_num, a, b)




# Outlook is sunny
n = 5.0
start_num = 2.0

# humidity
a = np.array([3.0, 2.0])
b = np.array([0.0, 2.0])
print 'humidity', gain(n, start_num, a, b)


# temp
a = np.array([2.0, 2.0, 1.0])
b = np.array([0.0, 1.0, 1.0])
print 'temp', gain(n, start_num, a, b)


# wind
a = np.array([2.0, 2.0, 1.0])
b = np.array([0.0, 1.0, 1.0])
print 'wind', gain(n, start_num, a, b)



# Outlook is rain
n = 5.0
start_num = 3.0

# humidity
a = np.array([2.0, 3.0])
b = np.array([1.0, 2.0])
print 'humidity', gain(n, start_num, a, b)


# temp
a = np.array([1.0, 3.0, 2.0])
b = np.array([1.0, 2.0, 1.0])
print 'temp', gain(n, start_num, a, b)


# wind
a = np.array([3.0, 2.0])
b = np.array([3.0, 0.0])
print 'wind', gain(n, start_num, a, b)



