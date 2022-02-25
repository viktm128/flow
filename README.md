# Flow Free
This is a pet project based on the set of mobile games called Flow Free created by Big Duck Games. I have always loved playing these games and thought I'd take a crack at an algorithmic approach to solving these puzzles.

## A Brief Overview of the Game
All puzzles begin with a gridded board. The orignal levels were n x n squares with n between 5-15 inclusive. On each board, there are pairs of different colored start and end dots that occupy spaces on the board. The objective of each level is to find a continuous path for each color through the board such that 

- none of the paths intersect
- each path connects the start and end point of each color
- the entire board is filled up

Here is an example of a unsolved and solved level below for n = 5.

[comment] # (TODO added in a complete and incomplete picture)


As the game became more complicated, multiple variants were added to the game included different shapes and sizes of boards, bridges, wormholes, and different numbers of connections per node in each board. We will start by just trying to solve square and rectangular boards.


## Data Structure?
Since we are starting with a rectangular board, a list of list seems like a natural choice of data structure. To begin, we will mark each start and end node with pairs of alphabetical letters. For example a 5x5 board with 4 flows to complete might be viewed like this

[comment] # (TODO add in a picture of a starting array, Flow Free Classic Pack Level 11)

We then will fill complete the flows by filling in the array with corresponding numbers. So a --> 0, b --> 1, c --> 2, etc. A completed board may look like this

[comment] # (TODO add in a picture of a completed board)  

### File Structure
All boards will follow these specifications
- first line will have the height and width separated by a space
- each flow will have 1 line starting with a letter (indicating what flow we are on) followed by a colon. The line will then list node indices. The coordinates will be listed as space separated. Each line will always have at least 2 nodes for start and end
- any intermediary nodes that are already filled in will be listed between the starting and ending nodes

Consider this example file below which represents the graph above
`
5 5
a: 0 0 0 2
b: 1 0 1 4
c: 2 0 4 4
d: 0 4 2 2
`

## Algorithms


## Test Suite