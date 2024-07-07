from typing import List

class Solution:
    def validStrings(self, n: int) -> List[str]:
        if n == 1:
            return ["0", "1"]
        
        results = []
        
        def generate(current):
            if len(current) == n:
                results.append(current)
                return
            
            generate(current + "1")
            
            if current[-1] == "1":
                generate(current + "0")
        
        generate("0")
        generate("1")
        
        return results


'''3211. Generate Binary Strings Without Adjacent Zeros'''