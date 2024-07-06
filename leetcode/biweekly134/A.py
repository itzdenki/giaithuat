'''100336. Alternating Groups I'''

from typing import List

class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        n = len(colors)
        if n < 3:
            return 0
        
        count = 0
        for i in range(n):
            if colors[i] != colors[(i + 1) % n] and colors[(i + 1) % n] != colors[(i + 2) % n] and colors[i] == colors[(i + 2) % n]:
                count += 1
                
        return count