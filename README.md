# Autometa Animations

This repository contains the source code for the [https://github.com/3b1b/manim](manim) scenes I used to make the animations used in 
the [https://autometa.readthedocs.org](Autometa documentation) and the [https://www.youtube.com/channel/UC6gKlYZ89fct4cJyj5sQBSg](Kwan lab YouTube channel).

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


