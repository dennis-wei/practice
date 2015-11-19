def compareVersion(version1, version2):
    """
    :type version1: str
    :type version2: str
    :rtype: int
    """
        
    list_1 = version1.split(".")
    list_2 = version2.split(".")
        
    if len(list_1) < len(list_2):
        for i in range(0, len(list_2) - len(list_1)):
            list_1.append(0)
    if len(list_1) > len(list_2):
        for i in range(0, len(list_1) - len(list_2)):
            list_2.append(0)
        
    for i in range(0, len(list_1)):
        if int(list_1[i]) < int(list_2[i]):
            return -1
        elif int(list_1[i]) > int(list_2[i]):
            return 1
    
    return 0

print compareVersion("1.1", "1")
print compareVersion("1.2", "1.1")
print compareVersion("1", "2")