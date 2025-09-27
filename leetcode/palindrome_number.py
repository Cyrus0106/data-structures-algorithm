def isPalindrome(x):
        """
        :type x: int
        :rtype: bool
        """
        if str(x) == str(x)[::-1]:
            return True
        else:
            return False
        
print(isPalindrome(10))

def isPalindrome3(x):
        if x < 0: return False

        if x == 0: return True
        rev = 0
        num = x
        while num != 0:
            rev = rev * 10 + num % 10
            num = num // 10

        return rev == x 

