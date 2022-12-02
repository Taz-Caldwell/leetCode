# Class to solve palindrome problem with strings for leetcode.
#
# Resources: https://www.geeksforgeeks.org/reverse-string-python-5-different-ways/
# Author: MaTais Caldwell (mkcaldwe@go.olemiss.edu)
# Date: Dec 2, 2022
class solution:
    def isPalindrome(self, x: int) -> bool:
        userInput = input('\nGive me a number:')
        userInput = str(userInput)

        original = userInput
        reverse = userInput[::-1]

        if original == reverse:
            solution = True
        else:
            solution = False

        return solution
