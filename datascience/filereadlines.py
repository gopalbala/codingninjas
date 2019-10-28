f = open('Sample.txt')
fl = f.readlines()
cnt = 0
for s in fl:
    if cnt < 5:
        print(s)
        cnt+=1
    else:
        break