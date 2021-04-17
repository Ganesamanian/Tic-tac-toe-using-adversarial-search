#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 15:28:09 2018

@author: iswariya
"""

import argparse
import math
import timeit
from helper import Connect4


def play_game(option):
    """Function to start playing the game.
    Here you will have to create two players
    * Human
    * AI agent
    Both of these players should be given alternate turns
    to play the game.
    Each step SHOULD BE PRINTED on the console.
    If an invalid position (already occupied position) is
    entered then the player should be asked to enter again.
    If a 4 streak is reached by a particular player, then the
    game should end. The winner should be declared.

    Parameters
    ----------
    option : int
        Decides whether Minimax with or without Alpha-Beta pruning
    

    """
    initial_config = Connect4()    
    board = Connect4(orig=initial_config)
    AI_agent = True
    global depth_limit
    depth_limit = int(input("Enter the depth to search(MORE THAN 5 INCREASES, THE TIME):")or "5")
    turn_counter=0
    time_list = list()
    while(True):

        #finds the move to make using Evalution Function
        if AI_agent:
            if option==1:
                start_time = timeit.default_timer()
                print("\nAI is thinking ...")
                score, move, evalution_value = minimax(board,depth_limit,1) 
                end_time = timeit.default_timer()   
                print(evalution_value)
                print("move made {}, since max score is {}".format(move,score))
                time_list.append(end_time-start_time)
                print("Time taken by AI is {}\n".format(time_list[turn_counter-1]))
               
                
            else:
                start_time = timeit.default_timer()
                print("\nAI is thinking ...")
                score, move, evalution_value = alpha_beta_pruning(board, depth_limit, 1, float("-inf"), float("inf")) 
                end_time = timeit.default_timer()   
                print(evalution_value)
                print("move made {}, since max score is {}".format(move,score))
                time_list.append(end_time-start_time)
                print("Time taken by AI is {}\n".format(time_list[turn_counter-1]))
                
                

        else:
            turn_counter+=1
            print("\n -------- Your Turn is {}----------".format(turn_counter))
            move = int(input("Enter the column to make move:"))
            
            while(board.valid_move(move)):
                print("----Invalid move, enter a proper move-----")
                move = int(input("Enter the column to make move:"))
            
                


        #makes the move
        board.insert_coin(move)
        board.printboard()

        #determines if the game is over or not
        game_Over = board.is_game_over()
        if game_Over >=0:
            print("Average time taken by AI is {}".format(sum(time_list)/len(time_list)))
        if game_Over == 0:
            print("It is a draw!")
            break
        elif game_Over == 1:
            print("AI wins!")
            break
        elif game_Over == 2:
            print("Player 2 wins!")
            break
        else:
            AI_agent = not AI_agent

    # FILL IN YOUR CODE HERE

    return


def minimax(board, depth, player):
    """Function to implement minimax algorithm.
    Please use the functions in helper.py to complete the algorithm.
    Please do not clutter the code this file by adding extra functions.
    Additional functions if required should be added in helper.py

    Parameters
    ----------
    board : list
        contains current configuration of the board
    depth: int
        Specifies how much depth to search
    Player: int
        If its 1 takes Max, Zero takes Min, default its 1

    Returns
    -------
    bestScore: int
        Return the overall best score for the best position as computed
    bestMove: int
        Return best position to insert the coin
    val: list
        Contains evalution score for each position

    """
    if board.is_game_over() == 0:
        return float("-inf") if player else float("inf"), -1
    elif depth == 0:
        return board.evaluation_func(board,depth_limit), -1
        

    if player:
        bestScore = float("-inf")
        min_or_max = lambda x: x > bestScore
    else:
        bestScore = float("inf")
        min_or_max = lambda x: x < bestScore
    val =[]
    #print("bestscore {}".format(bestScore))
    bestMove = -1

    children = board.children()
    for child in children:
        move, childboard = child
        score = minimax(childboard, depth-1, not player)[0]
        if depth == depth_limit:
            val.append(score)    
    
        #print(score,move)

        if min_or_max(score) or len(val)==1:
            bestScore = score
            bestMove = move
            
    return bestScore, bestMove, val

    #raise NotImplementedError


def alpha_beta_pruning(board, depth, player, alpha, beta):
    """Function to implement alpha-beta pruning.
    Please use the functions in helper.py to complete the algorithm.
    Please do not clutter the code this file by adding extra functions.
    Additional functions if required should be added in helper.py

    Parameters
    ----------
    board : list
        contains current configuration of the board
    depth: int
        Specifies how much depth to search
    Player: int
        If its 1 takes Max, Zero takes Min, default its 1

    Returns
    -------
    bestScore: int
        Return the overall best score for the best position as computed
    bestMove: int
        Return best position to insert the coin
    val: list
        Contains evalution score for each position

    """
    if board.is_game_over() == 0:
        return float("-inf") if player else float("inf"), -1
    elif depth == 0:
        return board.evaluation_func(board,depth_limit), -1

    if player:
        bestScore = float("-inf")
        min_or_max = lambda x: x > bestScore
    else:
        bestScore = float("inf")
        min_or_max = lambda x: x < bestScore

    bestMove = -1
    val =[]
    children = board.children()
    for child in children:
        move, childboard = child
        score = alpha_beta_pruning(childboard, depth-1, not player, alpha, beta)[0]
        if depth == depth_limit:
            val.append(score)
        if min_or_max(score) or len(val)==1:
            bestScore = score
            bestMove = move
        if player:
            alpha = max(alpha, score)
        else:
            beta = min(beta, score)
        if alpha >= beta:
            break
    return bestScore, bestMove, val
    #raise NotImplementedError


if __name__ == "__main__":
   
    parser = argparse.ArgumentParser()
    parser.add_argument('--option', choices=[1, 2], type=int)
    args = parser.parse_args()

    
    opt = args.option

    if opt == 1:
        print("\nMin - Max algorithm\n")
    elif opt == 2:
        print("\nMin - Max algorithm with Alpha-Beta pruning\n")

    
    play_game(opt)
