#Bankers Safety Algorithm
def Bankersafety(l,a,b,av):
    curra=[]
    for i in range(0,b):
        s=0
        for j in range(0,a):
            s+=l[j][0][i]
        curra.append(s)
    for i in range(0,b):
        curra[i]=av[i]-curra[i]
    print("Current Available is",curra)
    temp=l.copy()
    state=1
    while True:
        if state!=1:
            return "Deadlock"

        if (len(temp)==0):
            return "No Deadlocks found"

        for i in temp:
            f=True
            for j in range(0,b):
                if (i[2][j]>curra[j]):
                    f=False
            if (f==True):
                print(i[3])
                for j in range(0,b):
                    curra[j]+=i[0][j]
                print("Current Available is",curra)
                temp.remove(i)
                state=0
        state+=1

#Sam T Robin 21BRS1445
a = int(input("Enter number of processes\n"))
b = int(input("Enter number of resources\n"))
avail=list(map(int,input("Enter the total available\n").split()))
l=[]
for i in range(0,a):
    allocmax=[]
    print("Enter allocation of resources to process ",i+1)
    r=list(map(int,input().split()))
    allocmax.append(r)
    print("Enter maximum of resource to process ",i+1)
    r=list(map(int,input().split()))
    allocmax.append(r)
    l.append(allocmax)
for i in l:
    n=[]
    for j in range(0,b):
        s=i[1][j]-i[0][j]
        n.append(s)
    i.append(n)
    s="P"+str(l.index(i)+1)
    i.append(s)
print("\n",Bankersafety(l,a,b,avail),"\n")
#bankers request allocation
while True:
    ch=input("Would you like to check for request with bankers request allocation algorithm? (y/n) : ")
    if ch=="y":
        r=list(map(int,input("\nEnter the request :\n").split()))
        pro=int(input("\nEnter the process number : "))
        flag=True
        for j in range(0,b):
            if (l[pro-1][2][j]<r[j]):
                flag=False
    
        if (flag==True):
            for i in range(0,b):
                l[pro-1][0][i]+=r[i]

            for i in range(0,b):
                l[pro-1][2][i]=l[pro-1][1][i]-l[pro-1][0][i]
        
            s=Bankersafety(l,a,b,avail)
            if (s=="Deadlock"):
                print("\nThis request cannot be followed through due to occurence of a deadlock\n")
                
            else:
                print("\nThe request has been completed successfully\n")

        else:
            print("\nThe request cannot be followed through because request is larger than max of process\n")

    else:
        break

        