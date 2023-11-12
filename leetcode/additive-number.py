class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def is_valid(num1, num2, remaining):
            if not remaining:
                return True

            sum_str = str(int(num1) + int(num2))
            if remaining.startswith(sum_str):
                return is_valid(num2, sum_str, remaining[len(sum_str):])
            else:
                return False

        length = len(num)
        for i in range(1, length // 2 + 1):
            for j in range(i + 1, length):
                num1, num2 = num[:i], num[i:j]
                if (len(num1) > 1 and num1[0] == '0') or (len(num2) > 1 and num2[0] == '0'):
                    continue  # Invalid leading zeros

                if is_valid(num1, num2, num[j:]):
                    return True

        return False

# Example usage:
sol = Solution()
print(sol.isAdditiveNumber("112358"))  # Output: True
print(sol.isAdditiveNumber("199100199"))  # Output: True