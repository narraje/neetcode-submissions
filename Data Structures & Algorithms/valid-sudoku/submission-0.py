class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
       # for row in range(9):
        #    seen = set()
       #     for i in range(9):
        #        if board[row][i] == ".":
         #           continue
          #      if board[row][i] in seen:
           #         return False
            #    seen.add(board[row][i])

    #    for col in range(9):
     #       seen = set()
      #      for i in range(9):
       #         if board[i][col] == ".":
        #            continue
         #       if board[i][col] in seen:
          #          return False
           #     seen.add(board[i][col])  

   #     for box in range(9):
    #        seen = set()
     #       for i in range(3):
      #          for j in range(3):
       #             row = (box//3) * 3 + i
        #            col = (box%3) * 3 + j
         #           if board[row][col] == ".":
          #              continue
           #         if board[row][col] in seen:
            #            return False
             #       seen.add(board[row][col])
    #    return True 

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue

                box_index = (r // 3) * 3 + (c // 3)

                if val in rows[r] or val in cols[c] or val in boxes[box_index]:
                    return False  

                rows[r].add(val)
                cols[c].add(val)
                boxes[box_index].add(val)
        return True        

