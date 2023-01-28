# Cmput 455 sample code
# Solve TicTacToe with Boolean Minimax
# Written by Martin Mueller

from game_basics import BLACK, WHITE, EMPTY, colorAsString
from tic_tac_toe import TicTacToe
from pns_gpt import PNS

def solveAndPrint(state, solver): 
    print("Board:")
    state.print()
    print(colorAsString(state.toPlay), "to play")
    solver(state)

    #print("Win for Black: {}\nTime used: {:.4f}\n".format(
        #isWinForBlack, timeUsed))

# An example game, with some mistakes by both. 
# Call solve after every move.
def testGame(solver):
    t = TicTacToe()
    t.resetGame()
    nextBlack = 6
    nextWhite = 0
    t.play(nextBlack)
    t.play(nextWhite)

    #t.print()

    solveAndPrint(t, solver)
    # t.play(0)
    # solveAndPrint(t, solver)
    # t.play(3)
    # solveAndPrint(t, solver)
    # t.play(1)
    # solveAndPrint(t, solver)
    # t.play(4)
    # solveAndPrint(t, solver)
    # t.play(5)
    # solveAndPrint(t, solver)
    # t.play(2)
    # solveAndPrint(t, solver)
    # t.play(6)
    # solveAndPrint(t, solver)
    # t.play(7)
    # solveAndPrint(t, solver)
    # t.play(8)
    # solveAndPrint(t, solver)

testGame(PNS)
