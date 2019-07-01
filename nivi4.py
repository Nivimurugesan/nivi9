nn=int(input())
ll1=list(map(int,input().split()))
emm=1
ll=[]
for i in ll1:
  emm=emm*i
for i in ll1:
  ll.append(emm//i)
print(*ll)
