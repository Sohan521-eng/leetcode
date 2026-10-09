class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total_sum = sum(nums)
    
        if total_sum % 2 != 0:
            return False
        
        target = total_sum // 2
        dp = {0}
        
        for num in nums:
            next_dp = set(dp)
            for t in dp:
                if t + num == target:
                    return True
                if t + num < target:
                    next_dp.add(t + num)
            dp = next_dp
            
        return target in dp