d = {1:2, "abc":5, "def":7}
print(d.get(0,5))

d = {1:2, "abc":5, "def":7}
if 2 in d:
    print('Present')
else:
    print('Not Present')
    
a = {1:2,'list':[1,2],3:5}
b = {4:5,3:7}
a.update(b)
print(a[3])

a = {1:2,'list':[1,2],3:5}
a.pop('list')
a['list'] = [3,5]
print(a['list'])