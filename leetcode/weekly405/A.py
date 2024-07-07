class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        n = len(s)
        
        encrypted_string = ""
        
        for i in range(n):
            new_index = (i + k) % n
            encrypted_string += s[new_index]
        
        return encrypted_string

'''3210. Find the Encrypted String'''