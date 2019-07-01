snnf=input()
ll=list(set(snnf))
sffx=1
aa=0
check=False
while True:
    ch=ll[aa]
    for j in range(0,len(snnf)-sffx):
        if ch in snf[j:j+sffx]:
            check=True
        else:
            check=False
            aa+=1
            if aa>=len(ll):
             aa=0
             sffx+=1
            break

    if check==True:
        break
print(sffx)
