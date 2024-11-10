ploca=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
def prikaz():
    for j in range(3):
        print(ploca[j])
prikaz()
igr='drugi'
polja=0
while polja<9:
    polje=int(input())
    pro=False
    if polje<1 or polje>9:
        print(f"Polje {polje} Nije valjano polje")
    else:
        for i in range(len(ploca)):
            for j in range(3):
                if ploca[i][j]==polje:
                    if igr=='drugi':
                        ploca[i][j]='X'
                        igr="prvi"
                        prikaz()
                        polja+=1
                        pro=True
                    else:
                        ploca[i][j]='O'
                        igr="drugi"
                        prikaz()
                        polja+=1
                        pro=True
        if pro==False:
            print(f"Polje {polje} je veÄ‡ zauzeto")
    for i in range(3):
        if ploca[i][0]==ploca[i][1]==ploca[i][2]:
            print(f"Pobijedio je {igr} igraÄ‡!")
            break
    for i in range(3):
        if ploca[0][i]==ploca[1][i]==ploca[2][i]:
            print(f"Pobijedio je {igr} igraÄ‡!")
            break
    if ploca[0][0]==ploca[1][1]==ploca[2][2] or ploca[0][2]==ploca[1][1]==ploca[2][0]:
        print(f"Pobijedio je {igr} igraÄ‡!")
        break
    if polja==9:
        print("Igra je zavrĹˇila nerijeĹˇeno")
        break
