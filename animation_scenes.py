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

        autometa_circles = [ [] for i in range(8) ]

        with open(coordinates_file, 'r') as coordinates:
            for line in coordinates:
                line_list = line.rstrip().split('\t')
                x_coord = float(line_list[0])
                y_coord = float(line_list[1])
                radius = float(line_list[2])
                color = line_list[3]

                current_circle = Dot(np.array([x_coord, y_coord, 0]), color = color, radius = radius)

                if x_coord < -4.67:
                    autometa_circles[0].append(current_circle)
                elif x_coord < -3.01:
                    autometa_circles[1].append(current_circle)
                elif x_coord < -1.84:
                    autometa_circles[2].append(current_circle)
                elif x_coord < -0.09:
                    autometa_circles[3].append(current_circle)
                elif x_coord < 2.32:
                    autometa_circles[4].append(current_circle)
                elif x_coord < 3.98:
                    autometa_circles[5].append(current_circle)
                elif x_coord < 5.15:
                    autometa_circles[6].append(current_circle)
                else:
                    autometa_circles[7].append(current_circle)

        # Now we come up with random coordinates for where the circles begin
        # We initialize within a bounding box of X -6.6 to 6.6 and Y -3.6 to 3.6
        initial_circles = [ [] for i in range(8) ]

        for i in range(8):
            for j in range(len(autometa_circles[i])):
                initial_circle = autometa_circles[i][j].deepcopy().move_to(np.array([random.uniform(-6.6,6.6), random.uniform(-3.6,3.6), 0])).set_color(GREY)
                initial_circles[i].append(initial_circle)

        # Now we make the transforms
        fade_in_animations = list() # Simple list of each object FadeIn
        autometa_transforms = [ [] for i in range(8) ] # List of lists, each list contains transformation of dots to form a single letter

        for i in range(8):
            for j in range(len(initial_circles[i])):
                fade_in_animations.append(FadeIn(initial_circles[i][j]))

        for i in range(8):
            for j in range(len(initial_circles[i])):
                autometa_transforms[i].append(Transform(initial_circles[i][j], autometa_circles[i][j]))

        autometa_animationgroups = list()

        for i in range(8):
            autometa_animationgroups.append(AnimationGroup(*autometa_transforms[i], lag_ratio = 0))
            
        self.play(*fade_in_animations)
        #self.wait()
        self.play(AnimationGroup(*autometa_animationgroups, lag_ratio = 0.2))
        self.wait(5)