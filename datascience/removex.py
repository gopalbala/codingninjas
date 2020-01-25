def removex(str):
    return temp(str,0)
def temp(str,l):
    r = ""
    if l == len(str):
        return ""
    temp(str,l+1)
    if str[l] == 'x':
        r=  "" + temp(str,l+1)
    else:
        r += str[l] + temp(str,l+1)
    return r

s = input()
print(removex(s))