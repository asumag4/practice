from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:

        if not s or len(s) == 1:
            return False

        # Use a queue
        q = deque()

        mapping = {
            ')' : '(',
            '}' : '{',
            ']' : '[',
        }

        for i in s:

            # print("=================")
            # print(f"Q: {q}")
            # print(f"iter: {i}")

            if i in mapping.values():
                q.append(i)
            else:
                if q:
                    n = q.pop()
                    if mapping[i] == n:
                        print("Valid")
                        continue
                    else:
                        return False
                else: 
                    return False
            
        return False if len(q) > 0 else True 
