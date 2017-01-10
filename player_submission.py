#!/usr/bin/env python

# This file is your main submission that will be graded against. Only copy-paste
# code on the relevant classes included here from the IPython notebook. Do not
# add any classes or functions to this file that are not part of the classes
# that we want.

# Submission Class 1
class OpenMoveEvalFn():
    """Evaluation function that outputs a 
    score equal to how many moves are open
    for your computer player on the board."""
    def score(self, game, maximizing_player_turn=True):
        # TODO: finish this function!
        return len(game.get_legal_moves())
        

# Submission Class 2
class CustomEvalFn():
    """Custom evaluation function that acts
    however you think it should. This is not
    required but highly encouraged if you
    want to build the best AI possible."""
    def score(self, game, maximizing_player_turn=True):
        # TODO: finish this function!
        return eval_func

# Submission Class 3
class CustomPlayer():
    # TODO: finish this class!
    """Player that chooses a move using 
    your evaluation function and 
    a depth-limited minimax algorithm 
    with alpha-beta pruning.
    You must finish and test this player
    to make sure it properly uses minimax
    and alpha-beta to return a good move
    in less than 1000 milliseconds."""
    def __init__(self,  search_depth=3, eval_fn=OpenMoveEvalFn()):
        # if you find yourself with a superior eval function, update the
        # default value of `eval_fn` to `CustomEvalFn()`
        self.eval_fn = eval_fn
        self.search_depth = search_depth
        
    
    def move(self, game, legal_moves, time_left):
        best_move, utility = self.alphabeta(game,time_left, depth=self.search_depth)
        return best_move


    def utility(self, game, maximizing):
        if maximizing:
            if not game.get_opponent_moves():
                return float("inf")
            if not game.get_legal_moves():
                return float("-inf")

            return self.eval_fn.score(game)

        else:
            if not game.get_legal_moves():
                return float("inf")
            if not game.get_opponent_moves():
                return float("-inf")

            return self.eval_fn.score(game)


    def minimax(self, game, time_left, depth=float("inf"), maximizing_player=True):
        legal_moves = game.get_legal_moves()
        
        if not depth or not legal_moves:
            return None, self.utility(game, maximizing_player)

        if maximizing_player:
            best_move = None
            best_val =  float("-inf")

            for move in legal_moves:
                _, val = self.minimax(game.forecast_move(move), time_left, depth -1, False )
                if val > best_val:
                    best_val = val
                    best_move = move

        else:
            best_move = None
            best_val = float("inf")

            for move in legal_moves:
                _, val = self.minimax(game.forecast_move(move), time_left, depth -1, True)
                if val < best_val:
                    best_val = val
                    best_move = move

        return best_move, best_val

    def alphabeta(self, game, time_left, depth=float("inf"), alpha=float("-inf"), beta=float("inf"), maximizing_player=True):
        legal_moves = game.get_legal_moves()

        if not depth or not legal_moves:
            return None, self.utility(game, maximizing_player)

        if maximizing_player:
            val = float("-inf")
            best_move = None
            for move in legal_moves:
                node = game.forecast_move(move)
                _, new_val = self.alphabeta(node, time_left, depth-1, alpha, beta, False)

                if new_val > val:
                    val = new_val
                    best_move = move

                alpha = max( alpha, val)

                if beta <= alpha:
                    return best_move, beta
            return best_move, val

        else:
            val = float("inf")
            best_move = None
            for move in legal_moves:
                node = game.forecast_move(move)
                _, new_val = self.alphabeta(node, time_left, depth -1 , alpha, beta, True)

                if new_val < val:
                    val = new_val
                    best_move = move

                beta = min(beta, val)

                if beta <= alpha:
                    return best_move, alpha

            return best_move, val
