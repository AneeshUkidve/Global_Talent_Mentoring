from tkinter import *
print("Welcome to vaastu aayadhi calculator\n")
print("Would you like to enter your measurement in milimeter,feet or inches?")


def dinam(q):
    q*=8
    r=q%27
    if r==0:
        print("\nDinam = Good")
    if r==1 or r==10 or r==19:
        print("\nDinam = Good")
    if r==2 or r==11 or r==20:
        print("\nDinam = Good")
    if r==3 or r==12 or r==21:
        print("\nDinam = Not Good")
    if r==4 or r==13 or r==22:
        print("\nDinam = Good")
    if r==5 or r==14 or r==23:
        print("\nDinam = Not Good")
    if r==6 or r==15 or r==24:
        print("\nDinam = Good")
    if r==7 or r==16 or r==25:
        print("\nDinam = Not Good")
    if r==8 or r==17 or r==26:
        print("\nDinam = Good")
    if r==9 or r==18 or r==27:
        print("\nDinam = Good")
def aayam(q):
    q*=8
    r=q%12
    if r==0:
        print("Aayam = Substance")
    if r==1:
        print("Aayam = Unexpected Benefit")
    if r==2:
        print("Aayam = Pleasure")
    if r==3:
        print("Aayam = Renown")
    if r==4:
        print("Aayam = Heroism")
    if r==5:
        print("Aayam = Agricultural Wealth")
    if r==6:
        print("Aayam = Prosprity")
    if r==7:
        print("Aayam = Happiness, Spiritual Tranquility")
    if r==8:
        print("Aayam = Principles, Value")
    if r==9:
        print("Aayam = Wisdom")
    if r==10:
        print("Aayam = Meditation or Communication with the self")
    if r==11:
        print("Aayam = Accomplishment")
   
def vyayaa(q):
    q*=9
    r=q%10
    if r==0:
        print("Vyayaa = Intimacy or Love")
    if r==2:
        print("Vyayaa = Release From Sadness")
    if r==3:
        print("Vyayaa = Auspiciousness")
    if r==4:
        print("Vyayaa = Growth or Prosperity")
    if r==5:
        print("Vyayaa = Wealth")
    if r==6:
        print("Vyayaa = Monetary Benefits")
    if r==7:
        print("Vyayaa = Greatness")
    if r==8:
        print("Vyayaa = Destruction")
    if r==9:
        print("Vyayaa = Riot")
    if r==1:
        print("Vyayaa = Pleasure, Enjoyment")

def yoni(q):
    q*=3
    r=q%8
    if r==1:
        print("Yoni = East")
    if r==2:
        print("Yoni = South-East")
    if r==3:
        print("Yoni = South")
    if r==4:
        print("Yoni = South-West")
    if r==5:
        print("Yoni = West")
    if r==6:
        print("Yoni = North-West")
    if r==7:
        print("Yoni = North")
    if r==0:
        print("Yoni = North-East")

def amsham(q):
    q*=4
    r=q%9
    if r==1:
        print("Amsham = Not Good")
    if r==2:
        print("Amsham = Good")
    if r==3:
        print("Amsham = Good")
    if r==4:
        print("Amsham = Good")
    if r==5:
        print("Amsham = Good")
    if r==6:
        print("Amsham = Not Good")
    if r==7:
        print("Amsham = Good")
    if r==8:
        print("Amsham = Not Good")
    if r==0:
        print("Amsham = Good")

def vaaram(q):
    q*=9
    r=q%7
    if r==1:
        print("Vaaram = Not Good")
    if r==2:
        print("Vaaram = Good")
    if r==3:
        print("Vaaram = Not Good")
    if r==4:
        print("Vaaram = Good")
    if r==5:
        print("Vaaram = Good")
    if r==6:
        print("Vaaram = Good")
    if r==0:
        print("Vaaram = Not Good")


    
        
    

def mmt():
    o=float(input("\nEnter meausurement:"))
    i=o/25.4
    h=float(i/33.0)
    a=int(round(h*24))
    dinam(a)
    aayam(a)
    vyayaa(a)
    yoni(a)
    amsham(a)
    vaaram(a)    

def ftt():
    o=float(input("\nEnter meausurement:"))
    i=float(o*12)
    h=float(i/33.0)
    a=int(round(h*24))
    dinam(a)
    aayam(a)
    vyayaa(a)
    yoni(a)
    amsham(a)
    vaaram(a)
    
def ict():
    o=input("\nEnter meausurement:")
    i=float(o*1)
    h=float(i/33.0)
    a=int(round(h*24))
    dinam(a)
    aayam(a)
    vyayaa(a)
    yoni(a)
    amsham(a)
    vaaram(a)




c=Tk()
mm=Button(c,text="mm",command=mmt)
ft=Button(c,text="feet",command=ftt)
ic=Button(c,text="inches",command=ict)
mm.pack()
ft.pack()
ic.pack()
mm.mainloop()
ft.mainloop()
ic.mainloop()

