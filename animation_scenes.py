#!/usr/bin/env python

from manimlib.imports import *
import pandas as pd
import numpy
import math
from sklearn.cluster import DBSCAN
import random
import statistics
from copy import deepcopy
import pdb

class Logo(Scene):
	def construct(self):
		# We first parse the coordinates
        coordinates_file = 'svg/logo_coordinates.tsv'

        autometa_circles = list()

        with open(coordinates_file, 'r') as coordinates:
            for line in coordinates:
                line_list = line.rstrip().split('\t')
                x_coord = float(line_list[0])
                y_coord = float(line_list[1])
                radius = float(line_list[2])
                color = line_list[3]

                current_circle = Circle(fill_color=color, radius=radius, stroke_width=0).move_to(np.array([x_coord, y_coord, 0]))
                autometa_circles.append(current_circle)

        for circle in autometa_circles:
            self.add(circle)

        self.wait(5)