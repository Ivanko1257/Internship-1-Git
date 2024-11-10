m=int(input())
n=int(input())
rijeci=str(input()).split()
print(rijeci)
red=''
for i in range(len(rijeci)):
    mjesto=m-len(red)-len(rijeci[i])
    if mjesto>=1:
        red+=rijeci[i]+' '
    elif mjesto==0:
        red+=rijeci[i]
        odmak=(n-len(red))//2
        print(' '*odmak + red)
        red=''
    else:
        odmak=(n-len(red))//2
        print(' '*odmak + red)
        red=rijeci[i]+' '
odmak=(n-len(red))//2
print(' '*odmak + red)
