from numpy import array
from random import*

def remplissage(m,n):
    for i in range (n):
        for j in range (n):
           m[i,j]=randint(0,9)
           
def test(ch,n):   
    test1=True                                    
    test=False
    s=3
    for i in range (1,n):
        if ch[i]>ch[i-1] and (s==0 or s==3):
            test=True
            s=0
        else:
            if ch[i]<ch[i-1] and (s==1 or s==3):
                    test=True
                    s=1
            else:
                test1=False
    if test==True and test1==True:
        test=True
    else:
        test=False
    return test
        
def remplissage_t(t,n):
    for i in range (n):
        ch=""
        for j in range (n):
           ch=ch+str(m[i,j])
        d=dict()
        d["n"]=ch
        d["t"]=test(ch,n)
        t[i]=d
        
def affichage(t,n):
    for i in range (n):
        print(t[i]["n"])
        print(t[i]["t"])
        print("---------")

#programme principale
n=int(input("n="))
m=array([[int]*n]*n)
remplissage(m,n)
t=array([dict]*n)
remplissage_t(t,n)
affichage(t,n)