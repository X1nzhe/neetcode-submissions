class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n, m = len(board), len(board[0])
        sub_set = defaultdict(set)
        row_set = defaultdict(set)
        col_set = defaultdict(set)

        for i in range(n):
            for j in range(m):
                num = board[i][j]

                if num == '.':
                    continue
                sub_index = (i // 3) * 3 + (j // 3)

                if num in col_set[i] or num in row_set[j] or num in sub_set[sub_index]:
                    return False

                sub_set[sub_index].add(num)
                col_set[i].add(num)
                row_set[j].add(num)

        return True
        