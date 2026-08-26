class Solution(object):
     def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
       
        # Step 1: Convert the list into a set (sets remove duplicates automatically)
        unique_nums = set(nums)
        
        # Step 2: Compare lengths
        # If the set is smaller, that means duplicates were removed → return True
        if len(unique_nums) < len(nums):
            return True
        else:
            return False


# Example usage:
solution = Solution()
print(solution.containsDuplicate([1,2,3,1]))       # Output: True
print(solution.containsDuplicate([1,2,3,4]))       # Output: False
print(solution.containsDuplicate([1,1,1,3,3,4,3,2,4,2])) # Output: True
