#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

class Graph:
    def __init__(self):
	plt.figure(num=None, figsize=(10, 8), dpi=100, facecolor='w', edgecolor='k')
        plt.axis([0,24,0,300])
        plt.grid(True)
        plt.xlabel("Time of Day (24HR Format)")
        plt.ylabel("Glucose Level")
        plt.xticks([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23])
        plt.yticks([20,40,60,80,100,120,140,160,180,200,220,240,260,280,300])

    def title(self, t):
        plt.title(t)

    def single_line(self, X, Y, line_type):
        plt.plot(X, Y, line_type)

    def show(self):
        plt.show()
