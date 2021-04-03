# game-boy-rom-generator

#### Main Branch
![IntegrationTests](https://github.com/ikarth/game-boy-rom-generator/workflows/IntegrationTests/badge.svg?branch=main)
#### Develop Branch
![IntegrationTests](https://github.com/ikarth/game-boy-rom-generator/workflows/IntegrationTests/badge.svg?branch=develop)

# Game Boy ROM Generator

To run: `python -m rom_generator.unified`

To import new GBS templates: `python -m rom_generator.scenes.import -i "gbs_projects/<name of GBS file>.gbsproj"`


## Notes

The automatic compilation is a hack that only works on Windows, so you'll have to manually compile the games on other operating systems. This isn't a priority to fix, because the 2.0 version uses a different architecture that makes it less of an issue.

## Installation

(with Anaconda)
```
conda env create -f environment.yml
conda activate genboy_1
conda install -y matplotlib
conda install -y ipython
pip install pyglet==1.5.11
pip install gym-retro
pip install wordfilter
```
