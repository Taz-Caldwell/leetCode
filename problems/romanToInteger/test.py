import Solution


def main():
    test = Solution.Solution()

    NUM = 'MLXCV'
    result = test.romanToInt(NUM)

    print(f"\nThe decimal value of {NUM} Roman Numeral is: ", result)


if __name__ == '__main__':
    main()
