ee1,ff=map(int,input().split())
if ee1<=ff:
  gg=ee1
else:
  gg=ff
x=[]
for i in range(0,gg):
  x.append(sorted(list(map(int,input().split()))))
x=sorted(x)
for i in range(0,len(x[0])):
  for j in range(0,len(x)-1):
    if x[j][i]>x[j+1][i]:
      x[j][i],x[j+1][i]=x[j+1][i],x[j][i]
for i in x:
  print(*i)
