#!/bin/bash

# Setup files in the manim Docker container

#export MEDIA_DIR="/presentation/movie_files"
#apt-get update
#apt-get install inkscape dbus
#pip install pandas
#pip install scikit-learn

mkdir /manim/assets
#mkdir /manim/assets/svg_images
#mkdir /manim/assets/raster_images

# We patch the scene_file_writer.py file so that it will be able to render 4K
#patch /manim/manimlib/scene/scene_file_writer.py /presentation/patches/scene_file_writer.patch

# We need to convert all text in svg images into paths so that the render properly
#cd svg
#for i in *.svg; do dbus-run-session inkscape $i --export-text-to-path --export-plain-svg /manim/assets/svg_images/$i; done
#cd ..
#cp raster/* /manim/assets/raster_images/
ln -s /presentation/animation_scenes.py /manim/animation_scenes.py
ln -s /presentation/raster /manim/assets/raster_images
ln -s /presentation/svg /manim/assets/svg_images
