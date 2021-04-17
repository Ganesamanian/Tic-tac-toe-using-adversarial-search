#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 15:28:09 2018

@author: iswariya
"""


class Connect4:
    """ Class for creating Connect4 game environment.
    This class has been implemented to provide a minimalistic
    game environment to you. Please fill in the necessary
    functions.
    """

    HEIGHT = int(input("Enter the Height of the board:")or "6")
    WIDTH = int(input("Enter the Width of the board:")or "7")

    def __init__(self, orig=None):
        """Class Constructor for initializing the board

        Parameters
        ----------
        orig : list
            Initial position of the board obtained from user
        """
        
        if(orig):
            self.board = [list(col) for col in orig.board]
            self.numMoves = orig.numMoves
            self.lastMove = orig.lastMove
            return
        else:
            self.board = [[] for x in range(self.WIDTH)]
            self.numMoves = 0
            self.lastMove = None
            return

    def evaluation_func(self, board, depth):
        """Class method to count the no. of 2/3/4 streaks for a given player.
        Please fill in by combining the no. of vertical, horizontal and
        diagonal streaks for a particular streak value. Possible streak values are
        2, 3, 4.

        Parameters
        ----------
        board : array / matrix
            Contains the board configuration of particular instance of call
        
        Returns
        -------
        Score: int
            Returns the score for particular board configuration
        """

        score = depth
        state = board.board
        for i in range(0, board.WIDTH):
            for j in range(0, board.HEIGHT):
                # check horizontal streaks
                try:
                    # add player one streak scores to heur
                    if state[i][j] == state[i + 1][j] == 0:
                        score += 10
                    if state[i][j] == state[i + 1][j] == state[i + 2][j] == 0:
                        score += 100
                    if state[i][j] == state[i+1][j] == state[i+2][j] == state[i+3][j] == 0:
                        score += 10000

                    # subtract player two streak score to heur
                    if state[i][j] == state[i + 1][j] == 1:
                        score -= 10
                    if state[i][j] == state[i + 1][j] == state[i + 2][j] == 1:
                        score -= 1000
                    if state[i][j] == state[i+1][j] == state[i+2][j] == state[i+3][j] == 1:
                        score -= 10000
                except IndexError:
                    pass

                # check vertical streaks
                try:
                    # add player one vertical streaks to heur
                    if state[i][j] == state[i][j + 1] == 0:
                        score += 10
                    if state[i][j] == state[i][j + 1] == state[i][j + 2] == 0:
                        score += 100
                    if state[i][j] == state[i][j+1] == state[i][j+2] == state[i][j+3] == 0:
                        score += 10000

                    # subtract player two streaks from heur
                    if state[i][j] == state[i][j + 1] == 1:
                        score -= 10
                    if state[i][j] == state[i][j + 1] == state[i][j + 2] == 1:
                        score -= 100
                    if state[i][j] == state[i][j+1] == state[i][j+2] == state[i][j+3] == 1:
                        score -= 100000
                except IndexError:
                    pass

                # check positive diagonal streaks
                try:
                    # add player one streaks to heur
                    if j+1 <= self.WIDTH and state[i][j] == state[i + 1][j + 1] == 0:
                        score += 10
                    if j+2 <= self.WIDTH and state[i][j] == state[i + 1][j + 1] == state[i + 2][j + 2] == 0:
                        score += 100
                    if j+3 <= self.WIDTH and state[i][j] == state[i+1][j + 1] == state[i+2][j + 2] == state[i+3][j + 3] == 0:
                        score += 1000

                    # add player two streaks to heur
                    if j+1 <= self.WIDTH and state[i][j] == state[i + 1][j + 1] == 1:
                        score -= 10
                    if j+2 <= self.WIDTH and state[i][j] == state[i + 1][j + 1] == state[i + 2][j + 2] == 1:
                        score -= 100
                    if j+3 <= self.WIDTH and state[i][j] == state[i+1][j + 1] == state[i+2][j + 2] == state[i+3][j + 3] == 1:
                        score -= 10000
                except IndexError:
                    pass

                # check negative diagonal streaks
                try:
                    # add  player one streaks
                    if j-1>=0 and state[i][j] == state[i+1][j - 1] == 0:
                        score += 10
                    if j-2>=0 and state[i][j] == state[i+1][j - 1] == state[i+2][j - 2] == 0:
                        score += 100
                    if j-3>=0 and state[i][j] == state[i+1][j - 1] == state[i+2][j - 2] == state[i+3][j - 3] == 0:
                        score += 1000

                    # subtract player two streaks
                    if j-1>=0 and state[i][j] == state[i+1][j - 1] == 1:
                        score -= 10
                    if j-2>=0 and state[i][j] == state[i+1][j - 1] == state[i+2][j - 2] == 1:
                        score -= 100
                    if j-3>=0 and state[i][j] == state[i+1][j - 1] == state[i+2][j - 2] == state[i+3][j - 3] == 1:
                        score -= 10000
                except IndexError:
                    pass
        return score   

        # FILL IN YOUR CODE HERE

    def insert_coin(self, column):
        """Class method to insert the coin alternatively 0 and 1 for the given column

        Parameters
        ----------
        column : list
            Contains the list to append the value
        
        Returns
        -------
            Alters the board configuration by inserting coin on the required place of the
            column
        """
        
        piece = self.numMoves % 2
        self.lastMove = (piece, column)
        self.numMoves += 1
        self.board[column].append(piece)
        return

    def valid_move(self, column):
        try:
            if column>=self.WIDTH or len(self.board[column])>=self.HEIGHT:
                return 1
            else:
                return 0
        except IndexError:
            pass

    def children(self):
        """Class method to explore the child of the node

        Parameters
        ----------
        
            Takes the current board configuration
        
        Returns
        -------
        children: list
            List of children for the particular node
        """

        children = []
        for i in range(self.WIDTH):
            if len(self.board[i]) < self.HEIGHT:
                child = Connect4(self)
                child.insert_coin(i)
                children.append((i, child))
        return children

    def is_game_over(self):
        """Class method to check if game is over

        Returns
        -------
        1,2,0,-1
            Return 0 if the board is full, 1 if AI agent wins, 2 if Human wins 
            and -1 for other state
        """

        for i in range(0,self.WIDTH):
            for j in range(0,self.HEIGHT):
                try:
                    if self.board[i][j]  == self.board[i+1][j] == self.board[i+2][j] == self.board[i+3][j]:
                        
                        return self.board[i][j] + 1
                except IndexError:
                    pass

                try:
                    if self.board[i][j]  == self.board[i][j+1] == self.board[i][j+2] == self.board[i][j+3]:
                        
                        return self.board[i][j] + 1
                except IndexError:
                    pass

                try:
                    if self.board[i][j] == self.board[i+1][j + 1] == self.board[i+2][j + 2] == self.board[i+3][j + 3]:
                        
                        return self.board[i][j] + 1
                except IndexError:
                    pass

                try:
                    if j-3>=0 and self.board[i][j] == self.board[i+1][j - 1] == self.board[i+2][j - 2] == self.board[i+3][j - 3]:
                        
                        return self.board[i][j] + 1
                except IndexError:
                    pass
        if self.is_board_full():
            return 0
        return -1

    def is_board_full(self):
        """Class method to check if board is full

        Returns
        -------
        bool
            Returns true if board is full
        """

        return self.numMoves == self.WIDTH*self.HEIGHT

    def printboard(self):
        """Class method to print the board after each move

        Parameters
        ----------
            Takes the current board configuration

        """

        for rowNum in range(self.HEIGHT - 1, -1, -1):
            row = "|"
            for colNum in range(self.WIDTH):
                if len(self.board[colNum]) > rowNum:
                    row += " " + ('X' if self.board[colNum][rowNum] else 'O') + " |"
                else:
                    row += "   |"
            print(row)
            
        print('  '+'   '.join(str(x) for x in range(self.WIDTH)))
        return
