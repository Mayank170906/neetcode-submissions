class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        r=len(board)
        c=len(board[0])
        valid=True
        for i in range(r):
            temp=set()
            for j in range(c):
                if board[i][j]==".":
                    continue
                if board[i][j] in temp:
                    return False
                else:
                    temp.add(board[i][j])

        for i in range(c):
            temp=set()
            for j in range(r):
                if board[j][i]==".":
                    continue
                if board[j][i] in temp:
                    return False
                else:
                    temp.add(board[j][i])  

        x=0
        while x<9:
            y=0
            while y<9:
                temp=set()
                for i in range(x,x+3):
                    for j in range(y,y+3):
                        if board[i][j]==".":
                            continue
                        if board[i][j] in temp:
                            return False
                        else:
                            temp.add(board[i][j])
                y+=3
            x+=3
        return valid









