class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        # Define the mapping of digits to letters
        digit_mapping = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        def backtrack(index, current):
            if index == len(digits):
                result.append(current)
                return

            for letter in digit_mapping[digits[index]]:
                backtrack(index + 1, current + letter)

        result = []
        if digits:
            backtrack(0, '')

        return result

solution = Solution()
print(solution.letterCombinations("23"))  # Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
print(solution.letterCombinations(""))     # Output: []
print(solution.letterCombinations("2"))    # Output: ["a","b","c"]