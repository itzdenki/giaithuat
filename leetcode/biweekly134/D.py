'''100338. Number of Subarrays With AND Value of K'''

from typing import List
from collections import defaultdict

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = 0
        prev_results = defaultdict(int)

        for num in nums:
            curr_results = defaultdict(int)

            if num == k:
                count += 1
            curr_results[num] = 1

            for val, freq in prev_results.items():
                new_and_result = val & num
                if new_and_result == k:
                    count += freq
                curr_results[new_and_result] += freq
            
            prev_results = curr_results

        return count