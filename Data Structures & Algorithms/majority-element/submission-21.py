# BEtter SOlution RMB for next time
import random
class Solution:
    def majorityElement(self, nums):
        n = len(nums)
        while True: # keeps running til it stops
            candidate = random.choice(nums) # random since majority element > 0
            if nums.count(candidate) > n // 2: # checks if the random picked is >= 2
                return candidate # returns