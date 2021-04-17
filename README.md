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


#How it looks?</br>
Enter the Height of the board:5</br>
Enter the Width of the board:5</br>
Enter the depth to search(MORE THAN 5 INCREASES, THE TIME):2</br>

AI is thinking ...</br>
[2, 2, 2, 2, 2]</br>
move made 0, since max score is 2</br>
Time taken by AI is 0.005008956999517977</br>
</br>
|   |   |   |   |   |</br>
|   |   |   |   |   |</br>
|   |   |   |   |   |</br>
|   |   |   |   |   |</br>
| O |   |   |   |   |</br>
  0   1   2   3   4</br>

 -------- Your Turn is 1----------</br>
Enter the column to make move:1</br>
|   |   |   |   |   |</br>
|   |   |   |   |   |</br>
|   |   |   |   |   |</br>
|   |   |   |   |   |</br>
| O | X |   |   |   |</br>
  0   1   2   3   4</br>
</br>
AI is thinking ...</br>
[12, 2, -8, -8, -8]</br>
move made 0, since max score is 12</br>
Time taken by AI is 0.005008956999517977</br>
</br>
|   |   |   |   |   |</br>
|   |   |   |   |   |</br>
|   |   |   |   |   |</br>
| O |   |   |   |   |</br>
| O | X |   |   |   |</br>
  0   1   2   3   4</br>
</br>
 -------- Your Turn is 2----------</br>
Enter the column to make move:0</br>
|   |   |   |   |   |</br>
|   |   |   |   |   |</br>
| X |   |   |   |   |</br>
| O |   |   |   |   |</br>
| O | X |   |   |   |</br>
  0   1   2   3   4</br>

AI is thinking ...</br>
[12, 32, 12, 12, 12]</br>
move made 1, since max score is 32</br>
Time taken by AI is 0.0015974459984136047</br>
</br>
|   |   |   |   |   |</br>
|   |   |   |   |   |</br>
| X |   |   |   |   |</br>
| O | O |   |   |   |</br>
| O | X |   |   |   |</br>
  0   1   2   3   4</br>

 -------- Your Turn is 3----------</br>
Enter the column to make move:1</br>
|   |   |   |   |   |</br>
|   |   |   |   |   |</br>
| X | X |   |   |   |</br>
| O | O |   |   |   |</br>
| O | X |   |   |   |</br>
  0   1   2   3   4</br>

AI is thinking ...</br>
[32, 32, 42, 32, 32]</br>
move made 2, since max score is 42</br>
Time taken by AI is 0.004912111999146873</br>
</br>
|   |   |   |   |   |</br>
|   |   |   |   |   |</br>
| X | X |   |   |   |</br>
| O | O |   |   |   |</br>
| O | X | O |   |   |</br>
  0   1   2   3   4</br>

 -------- Your Turn is 4----------</br>
Enter the column to make move:2</br>
|   |   |   |   |   |</br>
|   |   |   |   |   |</br>
| X | X |   |   |   |</br>
| O | O | X |   |   |</br>
| O | X | O |   |   |</br>
  0   1   2   3   4</br>

AI is thinking ...</br>
[-78, -78, 22, -68, -78]</br>
move made 2, since max score is 22</br>
Time taken by AI is 0.004054094999446534</br>
</br>
|   |   |   |   |   |</br>
|   |   |   |   |   |</br>
| X | X | O |   |   |</br>
| O | O | X |   |   |</br>
| O | X | O |   |   |</br>
  0   1   2   3   4</br>

 -------- Your Turn is 5----------</br>
Enter the column to make move:0</br>
|   |   |   |   |   |</br>
| X |   |   |   |   |</br>
| X | X | O |   |   |</br>
| O | O | X |   |   |</br>
| O | X | O |   |   |</br>
  0   1   2   3   4</br>
</br>
AI is thinking ...</br>
[-10098, -10078, -10078, 32, -10088]</br>
move made 3, since max score is 32</br>
Time taken by AI is 0.004728001000330551</br>
</br>
|   |   |   |   |   |</br>
| X |   |   |   |   |</br>
| X | X | O |   |   |</br>
| O | O | X |   |   |</br>
| O | X | O | O |   |</br>
  0   1   2   3   4</br>
</br>
 -------- Your Turn is 6----------</br>
Enter the column to make move:4</br>
|   |   |   |   |   |</br>
| X |   |   |   |   |</br>
| X | X | O |   |   |</br>
| O | O | X |   |   |</br>
| O | X | O | O | X |</br>
  0   1   2   3   4</br>
</br>
AI is thinking ...</br>
[12, 32, 32, 62, 42]</br>
move made 3, since max score is 62</br>
Time taken by AI is 0.007528742000431521</br>
</br>
|   |   |   |   |   |</br>
| X |   |   |   |   |</br>
| X | X | O |   |   |</br>
| O | O | X | O |   |</br>
| O | X | O | O | X |</br>
  0   1   2   3   4</br>
</br>
 -------- Your Turn is 7----------</br>
Enter the column to make move:3</br>
|   |   |   |   |   |</br>
| X |   |   |   |   |</br>
| X | X | O | X |   |</br>
| O | O | X | O |   |</br>
| O | X | O | O | X |</br>
  0   1   2   3   4</br>
</br>
AI is thinking ...</br>
[52, 172, 72, 1172, 82]</br>
move made 3, since max score is 1172</br>
Time taken by AI is 0.006541709000885021</br>
</br>
|   |   |   |   |   |</br>
| X |   |   | O |   |</br>
| X | X | O | X |   |</br>
| O | O | X | O |   |</br>
| O | X | O | O | X |</br>
  0   1   2   3   4</br>
Average time taken by AI is 0.005042583374915921</br>
AI wins!</br>



