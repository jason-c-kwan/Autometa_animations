# Autometa Animations

This repository contains the source code for the [manim](https://github.com/3b1b/manim) scenes I used to make the animations used in 
the [Autometa documentation](https://autometa.readthedocs.org) and the [Kwan lab YouTube channel](https://www.youtube.com/channel/UC6gKlYZ89fct4cJyj5sQBSg).

## Rendering the animations

First you need to start the manim Docker container, making sure to mount the git repository directory, like this:

```bash
docker run -it --rm -v path/to/Autometa_animations:/presentation jasonkwan/manim:latest
```

Then at the bash prompt within the docker container, we need to run the setup script.

```bash
cd presentation
source ./setup_files.sh
```

To do a low-quality test render of a scene:

```bash
cd /manim
./manim.py -l --video_output_dir /presentation/videos animation_scenes.py Logo
```

...where "Logo" can be replaced by the name of any scene in `animation_scenes.py`. To re-do a render in 4K:

```bash
./manim.py -r "2160,3840" --video_output_dir /presentation/videos animation_scenes.py Logo
```


