# helper functions
def nodeToIndex(i, j):
    return i * 3 + j + 1

def possibleMoves(board, i, j):
    possible = []
    moveMap = [[2, 1], [2, -1], [-2 , 1], [-2,-1], [1, 2] , [-1, 2], [1 , -2], [-1,-2]]
    for move in moveMap:
        newI = i + move[0]
        newJ = j + move[1]
        if newI < len(board) and newI >= 0 and newJ < len(board[newI]) and newJ >= 0:
            possible.append([newI, newJ])
    return possible

def printBoard(board):
    for row in board:
        for piece in row:
            print(piece, end=" ")
        print()
    print()

moveCount = 0
def movePiece(board, initial , final):
    global moveCount
    moveCount += 1
    piece = board[initial[0]][initial[1]] 
    board[initial[0]][initial[1]] = '.'
    board[final[0]][final[1]] = piece
    printBoard(board)

def solveSubProblem(board):
    solution = []
    goalState = 3
    if board[0][0] == ".":
        goalState = 0
    indexes = [0, 2, 1]
    for i in indexes:
        isDone = False
        visited = []
        path = []
        possible = []
        currentNode = [goalState, i]
        while not isDone:
            visited.append(currentNode)
            path.append(currentNode)
            possibleFromCurrent = possibleMoves(board, currentNode[0], currentNode[1])
            possible += possibleFromCurrent
            for space in possible:
                if board[space[0]][space[1]] == "b" or board[space[0]][space[1]] == "w":
                    currentNode = space
                    visited.append(space)
                    path.append(space)
                    board[space[0]][space[1]] = "X"
                    isDone = True
            if not isDone:
                for space in possible:
                    if board[space[0]][space[1]] == "." and space[0] != goalState and space not in visited:
                        currentNode = space
            if currentNode not in possibleFromCurrent:
                path.pop(-1)
        solution.append(list(reversed(path)))
    return solution

def main():
    board = [["w", "w", "w"], [".", ".", "."], [".", ".", "."], ["b" ,"b" ,"b"]]
    blackBoard = board.copy()
    blackBoard[0] = [".", ".", "."]
    solutionBlack = solveSubProblem(blackBoard)
    whiteBoard = board.copy()
    whiteBoard[3] = [".", ".", "."]
    solutionWhite = solveSubProblem(whiteBoard)
    print(solutionWhite)
    print(solutionBlack)
    
if __name__ == "__main__":
    main()