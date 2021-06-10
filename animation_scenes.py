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
import random

class Logo(Scene):
    def construct(self):
        # We first parse the coordinates for where the circles are going to end up
        coordinates_file = '/presentation/svg/logo_coordinates.tsv'

        autometa_circles = list()

        with open(coordinates_file, 'r') as coordinates:
            for line in coordinates:
                line_list = line.rstrip().split('\t')
                x_coord = float(line_list[0])
                y_coord = float(line_list[1])
                radius = float(line_list[2])
                color = line_list[3]

                current_circle = Dot(np.array([x_coord, y_coord, 0]), color = color, radius = radius)
                autometa_circles.append(current_circle)

        # Now we come up with random coordinates for where the circles begin
        # We initialize within a bounding box of X -6.6 to 6.6 and Y -3.6 to 3.6
        initial_circles = list()

        for i in range(len(autometa_circles)):
            initial_circle = autometa_circles[i].deepcopy().move_to(np.array([random.uniform(-6.6,6.6), random.uniform(-3.6,3.6), 0]))
            initial_circles.append(initial_circle)

        # We make an enlarged set so that we start with a zoomed in version
        enlarged_circles = list()
        for i in range(len(initial_circles)):
            old_circle_center = initial_circles[i].get_center()
            new_x = old_circle_center[0] * 5
            new_y = old_circle_center[1] * 5

            old_radius = initial_circles[i].get_width() / 2
            new_radius = old_radius * 5

            color = initial_circles[i].get_color()

            new_circle = Dot(np.array([new_x, new_y, 0]), color = color, radius = new_radius)
            enlarged_circles.append(new_circle)

        # Now we make the transforms
        fade_in_animations = list()
        zoom_out_transforms = list()
        autometa_transforms = list()

        for i in range(len(enlarged_circles)):
            fade_in_animations.append(FadeIn(enlarged_circles[i]))
            zoom_out_transforms.append(Transform(enlarged_circles[i], initial_circles[i]))
            autometa_transforms.append(Transform(enlarged_circles[i], autometa_circles[i]))
            

        self.play(*fade_in_animations)
        #self.wait()
        self.play(*zoom_out_transforms)
        #self.wait()
        self.play(*autometa_transforms)
        self.wait(5)