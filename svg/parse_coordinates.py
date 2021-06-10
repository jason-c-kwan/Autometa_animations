#!/usr/bin/env python

# Get the range of x and y values for all the circles in the file
# NOTE: not a general svg parser

input_file = 'Autometa_logo2.svg'
output_file = 'logo_coordinates.tsv'

colors = { 'st0':'#1C75BC', \
	'st1':'#DA1C5C', \
	'st2':'#7F3F98', \
	'st3':'#F15A29', \
	'st4':'#BE1E2D', \
	'st5':'#FFF200', \
	'st6':'#EF4136' }

output = open(output_file, 'w')

# The way SVG coordinates work is that they start at 0,0 at the top left corner, with Y increasing downwards and X increasing right
# The XY coordinate of rectangles is the top left
# The XY coordinate of circles is the center
# The bounding box of the logo, which is the same aspect ratio as the Manim screen is at X = 0.18 and Y = 35.1, with width = 841.22 
# and height = 480.7

# The manim coordinate system goes from bottom left (-7,-4) to top right (7,4)

# So to go from SVG to Manim:
# For X, (X/60.0875) - 7
# For Y, (Y - 35.1)/60.0875 - 4 
# For radius, R/60.0875

with open(input_file, 'r') as svg:
    for line in svg:
        if len(line) > 7 and line[:7] == '<circle':
            line_list = line.rstrip().split(" ")
            x_coord = float(line_list[2][4:-1])
            y_coord = float(line_list[3][4:-1])
            circle_class = line_list[1][7:-1]
            radius = float(line_list[4][3:-3])

            manim_x = (x_coord/60.0875) - 7
            manim_y = (((y_coord - 35.1)/60.0875) - 4)*(-1)
            manim_color = colors[circle_class]
            manim_radius = radius/60.0875

            output_string = '\t'.join([str(manim_x), str(manim_y), str(manim_radius), manim_color]) + '\n'

            output.write(output_string)
        elif len(line) > 14 and line[:14] == '<ellipse class':
            line_list = line.rstrip().split(" ")
            x_coord = float(line_list[2][4:-1])
            y_coord = float(line_list[3][4:-1])
            circle_class = line_list[1][7:-1]
            radius = float(line_list[4][4:-1])

            manim_x = (x_coord/60.0875) - 7
            manim_y = (((y_coord - 35.1)/60.0875) - 4)*(-1)
            manim_color = colors[circle_class]
            manim_radius = radius/60.0875

            output_string = '\t'.join([str(manim_x), str(manim_y), str(manim_radius), manim_color]) + '\n'

            output.write(output_string)
        elif len(line) > 18 and line[:18] == '<ellipse transform':
            line_list = line.rstrip().split(" ")
            x_coord = float(line_list[8][4:-1])
            y_coord = float(line_list[9][4:-1])
            circle_class = line_list[7][7:-1]
            radius = float(line_list[10][4:-1])

            manim_x = (x_coord/60.0875) - 7
            manim_y = (((y_coord - 35.1)/60.0875) - 4)*(-1)
            manim_color = colors[circle_class]
            manim_radius = radius/60.0875

            output_string = '\t'.join([str(manim_x), str(manim_y), str(manim_radius), manim_color]) + '\n'

            output.write(output_string)
        else:
            print(line)

