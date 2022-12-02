###################################################################################
# Class to solve palindrome problem with strings for leetcode.
#
# Resources: https://www.geeksforgeeks.org/reverse-string-python-5-different-ways/
# Author: MaTais Caldwell (mkcaldwe@go.olemiss.edu)
# Date: Dec 2, 2022
###################################################################################

class Solution(object):
    def isPalindrome(self, x: int) -> bool:
        """_summary_

        Args:
            x (int): number to be tested to see if it is
            a palendrome.

        Returns:
            bool: returns true if number is palendrome.
        """
        userInput = str(x)

        original = userInput
        # flip the user input
        reverse = userInput[::-1]

        if original == reverse:
            solution = True
        else:
            solution = False

        return solution
