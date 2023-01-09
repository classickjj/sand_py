# A falling Sandgame

This game is based on the concepts of cellular automata. In a nutshell that means the state of each cell/particle in 
the next computed iteration is based on the state of its neighboring cells/particles.
If you are familiar with Conway's "Game of Life", it is the same concept, with different rules.

## For example, take "Sand"
In Conway's "Game of Life" we are always computing if a cell is alive or dead in the next cycle, based on how many 
of its eight neighbors are alive.
In a sandgame it gets somewhat more complex. Sand for example will not be "dead" if it has no neighbors, rather if
it has no "neighboring" sand or obstacles below it, it will "fall" down to the ground, until it reaches an 
obstacle or other sand-particles that block its way. 
So this is like a cellular automata, but just implemented with different rules.

Also compared to the game of life, there are not only cells that are either dead or alive but multiple types 
of cells/particles. They just need their own ruleset to compute their behaviour.

### Notes:
I started this because Conway's "Game of Life" already fascinated me, so i wanted to learn more about it and also 
use this as another opportunity to work with python! 

There is still a lot TODO, since i only started this project in the winter holidays 2022. 
But since this is more a fun project to me, it can take a while to finish because of other priorities.

If anyone has suggestions or questions, im happy to hear about them!

