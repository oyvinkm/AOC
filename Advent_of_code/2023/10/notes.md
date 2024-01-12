The pipes are arranged in a two-dimensional grid of tiles:

- | is a vertical pipe connecting north and south.
- - is a horizontal pipe connecting east and west.
- L is a 90-degree bend connecting north and east.
- J is a 90-degree bend connecting north and west.
- 7 is a 90-degree bend connecting south and west.
- F is a 90-degree bend connecting south and east.
- . is ground; there is no pipe in this tile.
- S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.



Find the tiles that are the furthest away. 
Method: search through connecting pipes starting from S. 
Search both ways from S, save the minimum distance, when you reach a node that has a distance, which is less then the current distance stop. 