'''100351. Alternating Groups II'''

from functools import cache

class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        
        N = len(colors)
        colors = colors + colors
        
        @cache
        def is_alternative(b):
            if b > 0 and is_alternative(b - 1):
                return colors[b + k -1] != colors[b + k - 2]
            for i in range(b, b + k - 1, 1):
                if colors[i] == colors[i + 1]:
                    return False
            return True
        
        ans = 0
        for i in range(N):
            if is_alternative(i):
                ans += 1
        return ans