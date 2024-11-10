niz=input().split()
def Mogucnosti(i, poc, kraj):
    if poc==kraj:
        print(" ".join(map(str, niz)))
    else:
        for j in range(poc, kraj+1):
            i[poc], i[j] = i[j], i[poc]
            Mogucnosti(i, poc+1, kraj)
            i[poc], i[j] = i[j], i[poc]
Mogucnosti(niz, 0, len(niz)-1)
