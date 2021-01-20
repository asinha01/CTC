from collections import Counter

def verify_permutation(string1, string2):
    count_string1, count_string2 = Counter(string1), Counter(string2)

    if len(count_string1) != len(count_string2):
        return False
    for element in count_string1:
        if element in count_string2:
            if count_string2[element] == count_string1[element]:
                  continue
            else:
                return False
        else:
            return False
    return True
# T.C - create 2 dicts, run for loop over length - O(n)

def main():
    result = verify_permutation("aba","aab")
    print(result)
main()