# Pokérandom

A tool to keep track of the random locations in randomized Pokémon.
Credits to the randomization to
[PointCrow](https://www.youtube.com/c/PointCrow).
See [here](https://www.reddit.com/r/pokemon/comments/qel5h4/) for the Reddit
post explaining how it works (for Emerald).

Written in Python, using [PySide6](https://doc.qt.io/qtforpython) (Qt 6). I
hope that this will work on Windows out of the box, but cannot guarantee that.


## Getting started
Create a `virtualenv`, and do

    pip install pyside6
    mv data/links.sqlite.empty data/links.sqlite
    python main.py

## Roadmap:

I *just* started on this project, it does not work yet.

 * **Create initial working version for Platinum**
 * Improve mapping experience (clicking on map, shortcuts, searching)
 * Ensure Windows/OS X support
 * Add Pokémon Emerald support
