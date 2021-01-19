def verify_with_set(string):
    set_string = set(string)
    print(set_string)
    if len(string) > len(set_string):
        return False
    else:
        return True



def verify_with_dict(string):
    dictionary = {}
    count = 1
    for element in string:
        if element not in dictionary:
            dictionary[element] = count
        else:
            return False
    for val in dictionary.values():
        print(val)
    return True                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
# do it without extra space
def inplace_verify(string):
    # sort the list and look at adjacent elements
    string = "".join(sorted(string))
    print("sorted",string)
    for i in range(0,len(string)-1):
        if string[i] == string[i+1]:
            return False
    return True 
print("set",verify_with_set("aabcc"))
print("dict False",verify_with_dict("aabcc"))
print("dict",verify_with_dict("abc"))
print("in place",inplace_verify("babbca"))

