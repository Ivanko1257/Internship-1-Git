k=int(input())
zvje=-1
if k%2==0:
    m=k//2
else:
    m=k//2+1
zvij=1+2*(m-1)
for i in range(m):
    zvje+=2
    prostor=(zvij-zvje)//2
    print(' '*prostor + '*'*zvje + ' '*prostor)
if k%2==0:
    zvje+=2
for i in range(m):
    zvje-=2
    prostor=(zvij-zvje)//2
    print(' '*prostor + '*'*zvje + ' '*prostor)
