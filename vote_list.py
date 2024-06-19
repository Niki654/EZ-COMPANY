vote=[]
pct=0
qct=0
rct=0
sct=0
while True:
    c=int(input("Enter 1 if u want to vote \n p=1\n q=2 \n r=3 \n s=4 and 0 to check to votes"))
    if c==1:
        v=int(input("Enter number whom u want to vote"))
        vote.append(int(v))
    elif c==0:
        j=vote.count(1)+vote.count(2)+vote.count(3)+vote.count(4)
        for i in range(j):
            if 1==vote[i]:
                pct=pct+1
            elif 2==vote[i]:
                qct=qct+1
            elif 3==vote[i]:
                rct=rct+1
            elif 4==vote[i]:
                sct=sct+1
        print( max(pct,qct,rct,sct))
        print("P",pct)
        print("q-",qct)
        print("r-",rct)
        print("s-",sct)





vote=list(map(int,input("Enter the votes: ").split(" ")))
count=[0]*6
for i in vote:
       count[i-1]=count[i-1]+1

print(v,count)




