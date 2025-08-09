class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        board.reverse()
        def squareToPosition(square):
            r = (square - 1) // n
            c = (square - 1) % n
            if r%2:
                c = n - 1 - c
            return r, c
        visited = set()
        q = deque([[1, 0]])
        while q:
            square, move = q.popleft()
            for i in range(1, 7):
                nextSquare = square + i
                r, c = squareToPosition(nextSquare)
                if board[r][c] != -1:
                    nextSquare = board[r][c]
                if nextSquare == n*n:
                    return move + 1
                if nextSquare not in visited:
                    visited.add(nextSquare)
                    q.append([nextSquare, move + 1])
        return -1


        
        