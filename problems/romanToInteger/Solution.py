class Solution(object):
    def romanToInt(self, s):
        """_summary_

        Args:
            s (string): String to be converted from roman numeral I think.
        """
        result = 0
        i = 0

        while (i < len(s)):

            # Getting value of symbol s[s]
            s1 = self.value(s[i])

            if (i + 1 < len(s)):

                # Getting value of symbol s[i + 1]
                s2 = self.value(s[i + 1])

                # Comparing both values
                if (s1 >= s2):

                    # Value of current symbol is greater
                    # of equal to the next symbol
                    result = result + s1
                    i = i + 1
                else:

                    # Value of current symbol is greater or equal to
                    # the next symbol.
                    result = result + s2 - s1
                    i = i + 2
            else:
                result = result + s1
                i = i + 1
        return result

    def value(self, r):
        if (r == 'I'):
            return 1
        if (r == 'V'):
            return 5
        if (r == 'X'):
            return 10
        if (r == 'L'):
            return 50
        if (r == 'C'):
            return 100
        if (r == 'D'):
            return 500
        if (r == 'M'):
            return 1000
        return -1
