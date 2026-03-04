class Solution:
    def letterCasePermutation(self, s: str) -> list[str]:
        
        def dfs(sub = "", idx = 0):
            if (idx == len(s)):
                res.append(sub)
                return
            else:
                # print(sub + s[idx])
                if (s[idx].isalpha()):
                    dfs(sub + s[idx], idx + 1)
                dfs(sub + s[idx].swapcase(), idx + 1)

        res = []
        dfs()
        return res