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
#
#
#The Most Optimal way is to move one of the sides first then continue with the problem
#
#Moving the middle part first will block the final 2 peices infront of each other
#
def CombineChoose(board , SolutionWhite, SolutionBlack):
    IndexW2H=1
    Hole=[]
    while len(SolutionBlack) + len(SolutionWhite) > 0:
        for elements in range(len(SolutionBlack)):
                if SolutionWhite[elements][len(SolutionWhite[elements])-1]==Hole:
                    IndexW2H=elements
        for j in range(len(SolutionWhite[IndexW2H])):
            if board[SolutionWhite[IndexW2H][j][0]][SolutionWhite[IndexW2H][j][1]]=="b":
                Holed=True
                Hole=SolutionWhite[IndexW2H][0]
                SolutionWhite[IndexW2H].pop(0)
                SolutionWhite[IndexW2H].pop(0)
                SolutionWhite.append(SolutionWhite[IndexW2H])
                SolutionWhite.pop(IndexW2H)
                break
            if board[SolutionWhite[IndexW2H][j][0]][SolutionWhite[IndexW2H][j][1]]==".":
                movePiece(board,SolutionWhite[IndexW2H][j-1],SolutionWhite[IndexW2H][j])
        if Holed is False:
            Hole=SolutionWhite[IndexW2H][0]
            SolutionWhite.pop(IndexW2H)
        Holed=False

#################################^^^^^^^White^^^^^^^^####################################
        if len(SolutionBlack) > 0:
            for elements in range(len(SolutionBlack)):
                    if SolutionBlack[elements][len(SolutionBlack[elements])-1]==Hole:
                        IndexB2H=elements
            for j in range(len(SolutionBlack[IndexB2H])):
                if board[SolutionBlack[IndexB2H][j][0]][SolutionBlack[IndexB2H][j][1]]=="w":
                    Last=(possibleMoves(board,SolutionWhite[0][0][0],SolutionWhite[0][0][1]))
                    # choose where to place the white on the board
                    for whitePossibility in Last:
                        if whitePossibility not in SolutionBlack[IndexB2H]:
                            # move the white away from black path
                            movePiece(board, SolutionWhite[0][0], whitePossibility)
                            # store the new position in white's solution
                            SolutionWhite[0].insert(0, whitePossibility)
                if board[SolutionBlack[IndexB2H][j][0]][SolutionBlack[IndexB2H][j][1]]==".":
                    movePiece(board,SolutionBlack[IndexB2H][j-1],SolutionBlack[IndexB2H][j])
            if Holed is False:
                Hole=SolutionBlack[IndexB2H][0]
                SolutionBlack.pop(IndexB2H)
            Holed=False

def main():
    board = [["b", "b", "b"], [".", ".", "."], [".", ".", "."], ["w" ,"w" ,"w"]]
    blackBoard = board.copy()
    blackBoard[3] = [".", ".", "."]
    solutionBlack = solveSubProblem(blackBoard)
    whiteBoard = board.copy()
    whiteBoard[0] = [".", ".", "."]
    solutionWhite = solveSubProblem(whiteBoard)
    board2 = [["b", "b", "b"], [".", ".", "."], [".", ".", "."], ["w" ,"w" ,"w"]]
    CombineChoose(board2,solutionWhite,solutionBlack)
    
if __name__ == "__main__":
    main()