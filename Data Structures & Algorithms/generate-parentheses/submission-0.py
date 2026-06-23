class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(curr_str, left_count, right_count):
            if len(curr_str) == 2 * n:
                res.append(curr_str)
                return
            if left_count < n:
                dfs(curr_str + '(', left_count+1, right_count)
            if right_count < left_count:
                dfs(curr_str +')', left_count, right_count+1)
        
        dfs('', 0, 0)

        return res

        