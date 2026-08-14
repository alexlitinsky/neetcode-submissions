class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        digits = digits[::-1]
        carry = 1
        idx = 0

        while carry:
            if idx == len(digits): break
            if digits[idx] == 9:
                digits[idx] = 0
                carry = 1
                idx += 1
            else:
                digits[idx] += 1
                carry = 0
        
        if carry:
            digits.append(1)
        
        return digits[::-1]
        