def isIsomorphic(s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        s_form = []
        t_form = []
        s_chars = []
        t_chars = []

        for c in s:
        	if not c in s_chars:
        		s_chars.append(c)
        	s_form.append(s_chars.index(c))

        for c in t:
        	if not c in t_chars:
        		t_chars.append(c)
        	t_form.append(t_chars.index(c))

        for i in range(0, len(s_form)):
        	if s_form[i] != t_form[i]:
        		return False
        return True

print "Testing egg, add: %s" % (isIsomorphic("egg", "add"))
print "Testing , : %s" % (isIsomorphic("", ""))
print "Testing foo, bar: %s" % (isIsomorphic("foo", "bar"))
print "Testing paper, title: %s" % (isIsomorphic("paper", "title"))