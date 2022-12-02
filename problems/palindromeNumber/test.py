import Solution


def main():

    demo = Solution.Solution()
    TEST_NUM = 1234321
    answer = demo.isPalindrome(TEST_NUM)

    if (answer == True):
        print(f"\nThe number {TEST_NUM}, is a palindrome.")
    else:
        print(f"\nThe number {TEST_NUM}, is not a palindrome.")


if __name__ == '__main__':
    main()
