class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        max_wealth = 0
        
        # Step 2: Loop through each customer (each row in accounts)
        for customer in accounts:
            # Step 3: Add up all the bank balances of this customer
            wealth = sum(customer)
            
            # Step 4: Compare with current max_wealth
            if wealth > max_wealth:
                # Step 5: Update max_wealth if this customer is richer
                max_wealth = wealth
        
        # Step 6: Return the richest wealth after checking all customers
        return max_wealth


# Example usage:
solution = Solution()
print(solution.maximumWealth([[1,2,3],[3,2,1]]))       # Output: 6
print(solution.maximumWealth([[1,5],[7,3],[3,5]]))     # Output: 10
print(solution.maximumWealth([[2,8,7],[7,1,3],[1,9,5]])) # Output: 17
        