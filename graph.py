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

    def title(self, t):
        plt.title(t)

    def single_line(self, X, Y, line_type, xtick, ytick):
        plt.xticks(xtick)
        plt.yticks(ytick)
        plt.plot(X, Y, line_type)

    def show(self):
        plt.show()
