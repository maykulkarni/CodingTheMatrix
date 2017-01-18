from __future__ import division

from collections import OrderedDict

import matplotlib.pyplot as plt


def plot(list_of_points):
    for x in list_of_points:
        print x
    x = [z[0] for z in list_of_points]
    y = [z[1] for z in list_of_points]
    plt.xlim(-15, 15)
    plt.ylim(-15, 15)
    plt.plot([0, 0], [-15, 15], color='black')
    plt.plot([-15, 15], [0, 0], color='black')
    plt.scatter(x, y)
    plt.show()


def vadd(vector_one, vector_two):
    return [a+b for a, b in zip(vector_one, vector_two)]


def vmul(alpha, vector):
    return [alpha*x for x in vector]


# point = [3, 2]
# plot([vadd(vmul(alpha, point), [0.5, 1]) for alpha in np.arange(0, 1+0.05, 0.05)])

class Vec:
    def __init__(self, lables, function):
        self.D = lables
        self.f = function

    def __str__(self):
        return str(self.D) + '\n' + str(self.f)


def zero_vector(lables):
    D = lables
    d = OrderedDict()
    for x in lables:
        d[x] = 0
    return Vec(D, d)


def setitem(vec, d, val):
    vec.f[d] = val


def getitem(vec, d):
    return vec.f[d] if d in vec.f else 0


v = zero_vector(['A', 'B', 'C', 'D'])
print v
setitem(v, 'X', 10)
print getitem(v, 'Z')
