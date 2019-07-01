nn=input()
ss="dhoni"
cc=0
if(len(nn)==5):
    for i in range(0,len(ss)):
        if(nn[i] in ss):
            cc=cc+1
    if(cc==5):
        print("yes")
    else:
        print("no")
else:
    print("no")
