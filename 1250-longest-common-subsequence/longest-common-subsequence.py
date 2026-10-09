class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        # Ensure text2 is the shorter string to minimize space
        if len(text1) < len(text2):
            text1, text2 = text2, text1

        dp = [0] * (len(text2) + 1)

        for char1 in text1:
            prev_diag = 0  # Represents dp[i-1][j-1]
            for j in range(1, len(text2) + 1):
                temp = dp[j]  # Store value before updating
                if char1 == text2[j - 1]:
                    dp[j] = prev_diag + 1
                else:
                    dp[j] = max(dp[j], dp[j - 1])
                prev_diag = temp

        return dp[-1]