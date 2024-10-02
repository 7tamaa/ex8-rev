from numpy import*
def saisie():
    n=int(input("n="))
    while not(4<=n and n<=100):
        n=int(input("n="))
    return n
        
def test1(d):
    test=True
    for i in range (len(d)):
        if not d[i]<"10" and d[i]>="0":
            if not d[i]<="F" and d[i]>="B":
                test=False
    return test

def test2(d):
    test=True
    for i in range(len(d)):
        if d[i]!="0" and d[i]!="1":
            test=False
    return test

def remplissage(n,b):
    for i in range (n):
        d=dict()
        d["id"]=input("d[id]=")
        while test1(d["id"])==False:
            d["id"]=input("d[id]=")
        d["bin"]=input("d[bin]=")
        while test2(d["bin"])==False:
            d["bin"]=input("d[bin]=")
        d["dominant"]=input("d[dominant]=")
        while test2(d["dominant"])==False:
            d["dominant"]=input("d[dominant]=")
        b[i]=d

def valid(i,b,k,l):
    ch=b[i]["bin"]
    ch=str(ch)
    for j in range(len(ch)):
        if ch[j]=="1":
            k=k+1
        else:
            l=l+1
    if k>l and b[i]["dominant"]=="1":
        return True
    if l>k and b[i]["dominant"]=="0":
        return True
    else:
        return False

def remplissage_v(v,n,b):
    global n1
    global k
    global l
    k=0
    l=0
    for i in range (n):
        if valid(i,b,k,l):
            d=dict()
            h=str(b["id"])
            d["id"]=h
            d["compression"]=k+"1"+l+"0"
            v[i]=d
        else:
            n1=n-1
             
def affichage(v,n1):
    for i in range (n1):
        print("--------")
        print(v[i]["id"])
        print(v[i]["compression"])
        
#programme principale
n=saisie()
b=array([dict]*n)
remplissage(n,b)
v=array([dict]*n)
remplissage_v(v,n,b)
affichage(v,n1)