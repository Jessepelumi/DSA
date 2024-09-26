# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

# Example 1
# Input: x = 123
# Output: 321

# Example 2
# Input: x = -123
# Output: -321

# Example 3
# Input: x = 120
# Output: 21

class Solution:
    def reverse(self, x: int) -> int:
        # integer range
        int_min, int_max = -2**31, 2**31 - 1

        # variable to store revd int
        rev = 0

        # get the sign
        sign = -1 if x < 0 else 1

        x = abs(x)

        while x != 0:
            # store the last digit
            pop = x % 10

            # remove the last digit & terminate loop
            x //= 10

            if rev > (int_max - pop) // 10:
                return 0
            
            rev = rev * 10 + pop

        return sign * rev
    
    
solution = Solution()

class CaseOne:
    input = 123

class CaseTwo:
    input = -123

caseOne = CaseOne()
caseTwo = CaseTwo()

resultOne = solution.reverse(caseOne.input)
resultTwo = solution.reverse(caseTwo.input)

print(f"Result one: {resultOne}\nResult two: {resultTwo}")