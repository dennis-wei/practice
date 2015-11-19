def reverseWords(s):
        """
        :type s: str
        :rtype: str
        """
        
        list_ = s.split()
        list_.reverse()
        ret_str = ' '.join(list_)
        return ret_str

print reverseWords("this is a test")
print reverseWords("")
print reverseWords("test")