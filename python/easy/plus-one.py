class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in raneg(len(digits) - 1, -1 , -1):
            s = digits[i] + carry
            digits[i] = s % 10
            carry = s // 10
        if carry:
            digits.insert(0, 1)
        return digits