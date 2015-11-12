def isPowerOfTwo(n):
        """
        :type n: int
        :rtype: bool
        """
        
        if n == 0:
            return False
        
        while n != 0:
            if n == 1:
                return True
            if n % 2 == 1:
                return False
            n /= 2
        
        return True

print isPowerOfTwo(0)
print isPowerOfTwo(1)
print isPowerOfTwo(16)
print isPowerOfTwo(12)
print isPowerOfTwo(25)