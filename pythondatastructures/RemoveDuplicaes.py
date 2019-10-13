import collections
def uniqueChars(string):
    # Please add your code here
    s = ""
    map = collections.OrderedDict()
    for c in string:
        map[c] = 0
    for ele in map:
        s = s + ele
    return s

# Main
string = input()
print(uniqueChars(string))