from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:    # Use a breakpoint in the code line below to debug your script.
        unique_values_seen = set()

        while nums:
            value = nums.pop()
            if value in unique_values_seen:
                return True
            else:
                unique_values_seen.add(value)

        return False