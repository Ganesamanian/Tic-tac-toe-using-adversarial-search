# Tic-tac-toe-using-adversarial-search

Implemented a simple Connect 4 game to demonstrate the use of adversarial search for determinis-
tic, fully observable, two player turn-taking zero-sum games. This is based on the minmax with alpha-beta pruning agent that allows you to play against the computer.

#How to play?
* Clone the repository
* Navigate to src folder
* Run adversarial_search.py using "$python3 adversarial_search.py"
* Enter the height of the board
* Enter the width of the board
* Enter the depth of search (more than 5 takes more time to process)
* Enter the column to place the coin (AI takes the first turn)


#How it looks?
Enter the Height of the board:5
Enter the Width of the board:5
Enter the depth to search(MORE THAN 5 INCREASES, THE TIME):2

AI is thinking ...
[2, 2, 2, 2, 2]
move made 0, since max score is 2
Time taken by AI is 0.005008956999517977

|   |   |   |   |   |
|   |   |   |   |   |
|   |   |   |   |   |
|   |   |   |   |   |
| O |   |   |   |   |
  0   1   2   3   4

 -------- Your Turn is 1----------
Enter the column to make move:1
|   |   |   |   |   |
|   |   |   |   |   |
|   |   |   |   |   |
|   |   |   |   |   |
| O | X |   |   |   |
  0   1   2   3   4

AI is thinking ...
[12, 2, -8, -8, -8]
move made 0, since max score is 12
Time taken by AI is 0.005008956999517977

|   |   |   |   |   |
|   |   |   |   |   |
|   |   |   |   |   |
| O |   |   |   |   |
| O | X |   |   |   |
  0   1   2   3   4

 -------- Your Turn is 2----------
Enter the column to make move:0
|   |   |   |   |   |
|   |   |   |   |   |
| X |   |   |   |   |
| O |   |   |   |   |
| O | X |   |   |   |
  0   1   2   3   4

AI is thinking ...
[12, 32, 12, 12, 12]
move made 1, since max score is 32
Time taken by AI is 0.0015974459984136047

|   |   |   |   |   |
|   |   |   |   |   |
| X |   |   |   |   |
| O | O |   |   |   |
| O | X |   |   |   |
  0   1   2   3   4

 -------- Your Turn is 3----------
Enter the column to make move:1
|   |   |   |   |   |
|   |   |   |   |   |
| X | X |   |   |   |
| O | O |   |   |   |
| O | X |   |   |   |
  0   1   2   3   4

AI is thinking ...
[32, 32, 42, 32, 32]
move made 2, since max score is 42
Time taken by AI is 0.004912111999146873

|   |   |   |   |   |
|   |   |   |   |   |
| X | X |   |   |   |
| O | O |   |   |   |
| O | X | O |   |   |
  0   1   2   3   4

 -------- Your Turn is 4----------
Enter the column to make move:2
|   |   |   |   |   |
|   |   |   |   |   |
| X | X |   |   |   |
| O | O | X |   |   |
| O | X | O |   |   |
  0   1   2   3   4

AI is thinking ...
[-78, -78, 22, -68, -78]
move made 2, since max score is 22
Time taken by AI is 0.004054094999446534

|   |   |   |   |   |
|   |   |   |   |   |
| X | X | O |   |   |
| O | O | X |   |   |
| O | X | O |   |   |
  0   1   2   3   4

 -------- Your Turn is 5----------
Enter the column to make move:0
|   |   |   |   |   |
| X |   |   |   |   |
| X | X | O |   |   |
| O | O | X |   |   |
| O | X | O |   |   |
  0   1   2   3   4

AI is thinking ...
[-10098, -10078, -10078, 32, -10088]
move made 3, since max score is 32
Time taken by AI is 0.004728001000330551

|   |   |   |   |   |
| X |   |   |   |   |
| X | X | O |   |   |
| O | O | X |   |   |
| O | X | O | O |   |
  0   1   2   3   4

 -------- Your Turn is 6----------
Enter the column to make move:4
|   |   |   |   |   |
| X |   |   |   |   |
| X | X | O |   |   |
| O | O | X |   |   |
| O | X | O | O | X |
  0   1   2   3   4

AI is thinking ...
[12, 32, 32, 62, 42]
move made 3, since max score is 62
Time taken by AI is 0.007528742000431521

|   |   |   |   |   |
| X |   |   |   |   |
| X | X | O |   |   |
| O | O | X | O |   |
| O | X | O | O | X |
  0   1   2   3   4

 -------- Your Turn is 7----------
Enter the column to make move:3
|   |   |   |   |   |
| X |   |   |   |   |
| X | X | O | X |   |
| O | O | X | O |   |
| O | X | O | O | X |
  0   1   2   3   4

AI is thinking ...
[52, 172, 72, 1172, 82]
move made 3, since max score is 1172
Time taken by AI is 0.006541709000885021

|   |   |   |   |   |
| X |   |   | O |   |
| X | X | O | X |   |
| O | O | X | O |   |
| O | X | O | O | X |
  0   1   2   3   4
Average time taken by AI is 0.005042583374915921
AI wins!



