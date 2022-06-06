# NVIDIA Geforce Shadowplay sort

> NVIDIA Shadowplay is a feature, that records your gaming sessions in the background. In case something super rare happens, you can easily save the last few minutes of the game.

## Introduction

Unfortunally, NVIDIA Shadowplay does not order the recorded sessions by time. This is a problem, because you can't easily find the clip you were searching for.
To solve this problem, I created this tool.

### Structure before sorting

- Videos / Recordings / Valorant / Valorant 2022.06.05 - 22.03.42.05.DVR.mp4
- Videos / Recordings / Valorant / Valorant Screenshot 2022.06.05 - 22.05.37.85.png

### Structure after sorting

- Videos / Recordings / Valorant / 2022 / 06 / 05 / videos / Valorant 2022.06.05 - 22.03.42.05.DVR.mp4
- Videos / Recordings / Valorant / 2022 / 06 / 05 / screenshots / Valorant Screenshot 2022.06.05 - 22.05.37.85.png

## Usage

### Nix & NixOS

```bash
# run the package from the repository
nix run .#shadowplay-sort

# run the package from anywhere
nix run 'github:mayniklas/shadowplay-sort'

# build the package
nix build .#shadowplay-sort
```

### Linux & MacOS

```bash
# create virtual environment
python3 -m venv .venv

# use virtual environment
source .venv/bin/activate

# install dependencies from requirements.txt
pip3 install -r requirements.txt

# install pre-commit hooks
pre-commit install

# install package, but any changes will immediately take effect.
python setup.py develop

# execute the package from your games recordings folder
shadowplay_sort
```
