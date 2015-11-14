def countAndSay(n):
        """
        :type n: int
        :rtype: str
        """
        
        curr_num = 1
        for i in range(1,n):
            curr_num = generate(curr_num)
        
        return str(curr_num)

def generate(n):
    num_str = list(str(n))
    num_str.append(" ")
    ret_str = ""
    count = 0
    for i in range (0, len(num_str)-1):
        count += 1
        if not num_str[i] == num_str[i+1]:
            ret_str += str(count)
            ret_str += str(num_str[i])
            count = 0
    return int(ret_str)

print countAndSay(1)
print countAndSay(5)
print countAndSay(9)