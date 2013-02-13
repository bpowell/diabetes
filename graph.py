#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

class Graph:
    def __init__(self):
        #plt.figure(num=None, figsize=(10, 8), dpi=100, facecolor='w', edgecolor='k')
        plt.grid(True)
        plt.xlabel("Time of Day (24HR Format)")
        plt.ylabel("Glucose Level")

    def title(self, t):
        plt.title(t)

    def single_line(self, X, Y, line_type):
        plt.plot(X, Y, line_type)

    def show(self):
        plt.show()

    def axis(self, a, xtick, ytick):
        plt.axis(a)
        plt.xticks(xtick)
        plt.yticks(ytick)
