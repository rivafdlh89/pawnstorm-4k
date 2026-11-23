import json,os,sys,urllib.request as u
U=os.environ.get("MAKEFUN_ENV_URL") or sys.exit(1)
def P(p,b):
 r=u.Request(U+p,data=json.dumps(b).encode(),headers={"content-type":"application/json"})
 try:
  with u.urlopen(r)as x:return json.load(x)
 except Exception:sys.exit(1)
V=[0,100,320,330,500,900,0]
KN=[-21,-19,-12,-8,8,12,19,21]
KI=[-11,-10,-9,-1,1,9,10,11]
DI=[-11,-9,9,11]
OR=[-10,-1,1,10]
B=[7]*120
S=1;C=0;E=0;H=0;W=25;X=95;N=0;L=180000
T={};Y=[];KL=[0]*128
class Z(Exception):pass
def F(f):
 global S,C,E,H,W,X
 B[:]=[0 if 21<=i<99 and i%10 not in(0,9) else 7 for i in range(120)]
 p=f.split()
 for i,r in enumerate(p[0].split("/")):
  q=0
  for c in r:
   if c.isdigit():q+=int(c)
   else:
    v="PNBRQKpnbrqk".index(c);v=v+1 if v<6 else 5-v
    s=91-i*10+q;B[s]=v;q+=1
    if v==6:W=s
    if v==-6:X=s
 S=1 if p[1]=="w" else -1
 C=("K"in p[2])+("Q"in p[2])*2+("k"in p[2])*4+("q"in p[2])*8
 E=0 if p[3]=="-" else 21+ord(p[3][0])-97+(int(p[3][1])-1)*10
 H=int(p[4])
PS="00000000122,,2211/.00./1000440001125521122466422::::::::00000000&(****(&(,0110,(*123321**034430**134431**023320*(,0000,(&(****(&,......,.100001..222222..022220..112211..012210..000000.,......,00011000/000000//000000//000000//000000//000000/1222222100000000,..//..,.010001..111111.0011110//011110/.011110..000000.,..//..,4620026444000044.,,,,,,.,**((**,*((&&((**((&&((**((&&((**((&&((*&******&**0000***.4664.**.6886.**.6886.**.4664.**,.00.,*&(*,,*(&"
PT=[(ord(c)-48)*5 for c in PS]
def A(s,c):
 if B[s-9*c]==c or B[s-11*c]==c:return 1
 for o in KN:
  if B[s+o]==2*c:return 1
 for o in KI:
  if B[s+o]==6*c:return 1
 for o in DI:
  t=s+o
  while B[t]!=7:
   if B[t]:
    if B[t]==3*c or B[t]==5*c:return 1
    break
   t+=o
 for o in OR:
  t=s+o
  while B[t]!=7:
   if B[t]:
    if B[t]==4*c or B[t]==5*c:return 1
    break
   t+=o
 return 0
def G(c):
 m=[]
 for s in range(21,99):
  p=B[s]
  if p==0 or p==7 or p*S<=0:continue
  a=p*S
  if a==1:
   d=10*S
   t=s+d
   if B[t]==0:
    r=t//10
    if r==9-(S<0)*7:
     for q in(5,4,3,2):m.append(s+(t<<7)+(q<<14))
    elif not c:
     m.append(s+(t<<7))
     if s//10==3+(S<0)*5 and B[t+d]==0:m.append(s+((t+d)<<7))
   for o in(9,11):
    t=s+o*S
    if B[t]==7:continue
    if B[t]*S<0 or t==E:
     r=t//10
     if r==9-(S<0)*7:
      for q in(5,4,3,2):m.append(s+(t<<7)+(q<<14))
     else:m.append(s+(t<<7))
  elif a==2 or a==6:
   for o in KN if a==2 else KI:
    t=s+o
    if B[t]!=7 and (B[t]*S<0 or B[t]==0 and not c):m.append(s+(t<<7))
   if a==6 and not c:
    for d in(2,-2):
     b=(1 if d>0 else 2)*(1 if S>0 else 4)
     if not C&b:continue
     f=25 if S>0 else 95
     t=f+d
     if B[f+d//2] or B[t] or d<0 and B[f-3]:continue
     if A(f,-S) or A(f+d//2,-S) or A(t,-S):continue
     m.append(f+(t<<7))
  else:
   D=DI if a==3 else OR if a==4 else KI
   for o in D:
    t=s+o
    while B[t]!=7:
     if B[t]==0:
      if not c:m.append(s+(t<<7))
      t+=o
     else:
      if B[t]*S<0:m.append(s+(t<<7))
      break
 return m
def mk(m):
 global S,C,E,H,W,X
 f=m&127;t=m>>7&127;q=m>>14
 p=B[f];v=B[t]
 u=(m,p,v,C,E,H)
 B[f]=0
 if p==S and t==E and not v:B[t-10*S]=0
 B[t]=q*S if q else p
 if p==6*S and abs(t-f)==2:
  if t>f:B[t-1]=B[t+1];B[t+1]=0
  else:B[t+1]=B[t-2];B[t-2]=0
 if p==6:W=t
 if p==-6:X=t
 if f==28 or t==28:C&=~1
 if f==21 or t==21:C&=~2
 if f==98 or t==98:C&=~4
 if f==91 or t==91:C&=~8
 if p==6:C&=~3
 if p==-6:C&=~12
 E=(f+t)//2 if p==S and abs(t-f)==20 else 0
 H=0 if p==S or v else H+1
 S=-S
 Y.append((tuple(B),S,C,E))
 return u
def uk(u):
 global S,C,E,H,W,X
 m,p,v,C,E,H=u
 f=m&127;t=m>>7&127
 S=-S
 B[f]=p;B[t]=v
 if abs(p)==1 and not v and t==E:B[t-10*S]=-S
 if p==6*S and abs(t-f)==2:
  if t>f:B[t+1]=B[t-1];B[t-1]=0
  else:B[t-2]=B[t+1];B[t+1]=0
 if p==6:W=f
 if p==-6:X=f
 Y.pop()
def ev():
 s=0;b1=0;b2=0;qq=0;wk=0;wb=0
 for i in range(21,99):
  p=B[i]
  if p==0 or p==7:continue
  a=p if p>0 else -p
  f=i%10-1;r=i//10-2
  j=f+r*8 if p>0 else f+(7-r)*8
  s+=(V[a]+PT[(a-1)*64+j])*(1 if p>0 else -1)
  if a==3:
   if p>0:b1+=1
   else:b2+=1
  if a==5:qq+=1
  if a==6:
   if p>0:wk=j
   else:wb=j
 if b1>1:s+=30
 if b2>1:s-=30
 if not qq:
  s-=PT[5*64+wk];s+=PT[6*64+wk]
  s+=PT[5*64+wb];s-=PT[6*64+wb]
 return s*S
def O(m):
 t=(m>>7)&127;v=B[t]
 return (V[abs(v)] if v else 0)*10-V[abs(B[m&127])]//32
def qs(a,b,pl):
 global N
 N+=1
 if N>L:raise Z
 k=W if S>0 else X
 c=A(k,-S)
 if not c:
  s=ev()
  if s>=b:return b
  if s>a:a=s
 ms=G(False) if c else G(True)
 ms.sort(key=lambda m:-O(m))
 lg=0
 for m in ms:
  if not c:
   v=B[(m>>7)&127]
   if v and V[abs(v)]+s+200<a:continue
  u=mk(m)
  s0=-S
  if A(W if s0>0 else X,-s0):
   uk(u);continue
  lg+=1
  sc=0 if H>=100 or Y.count(Y[-1])>1 else -qs(-b,-a,pl+1)
  uk(u)
  if sc>=b:return b
  if sc>a:a=sc
 if c and not lg:return -100000+pl
 return a
def sr(d,a,b,pl):
 global N,S,E,H
 N+=1
 if N>L:raise Z
 if H>=100:return 0
 k=(tuple(B),S,C,E)
 e=T.get(k)
 if e and e[0]>=d:
  if e[2]==0:return e[1]
  if e[2]==1 and e[1]>=b:return e[1]
  if e[2]==2 and e[1]<=a:return e[1]
 if d<=0:return qs(a,b,pl)
 if A(W if S>0 else X,-S):d+=1
 if d>=3 and not A(W if S>0 else X,-S):
  s1=S;e1=E;h1=H
  S=-S;E=0;H+=1
  Y.append((tuple(B),S,C,E))
  sc=-sr(d-3,-b,-b+1,pl+1)
  Y.pop()
  S=s1;E=e1;H=h1
  if sc>=b:return b
 ms=G(False)
 bm=e[3] if e else 0
 ms.sort(key=lambda m:(m==bm)*100000+O(m)+(500 if m==KL[pl*2] or m==KL[pl*2+1] else 0))
 best=-999999;bt=0;al=a
 ic=A(W if S>0 else X,-S)
 for j,m in enumerate(ms):
  v=B[(m>>7)&127]
  u=mk(m)
  s0=-S
  if A(W if s0>0 else X,-s0):
   uk(u);continue
  if H>=100 or Y.count(Y[-1])>1:sc=0
  elif j>=3 and d>=3 and not v and not m>>14 and not ic:
   sc=-sr(d-2,-a-1,-a,pl+1)
   if sc>a:sc=-sr(d-1,-b,-a,pl+1)
  else:sc=-sr(d-1,-b,-a,pl+1)
  uk(u)
  if sc>best:best=sc;bt=m
  if sc>a:a=sc
  if a>=b:
   if not v:
    KL[pl*2+1]=KL[pl*2];KL[pl*2]=m
   break
 if best==-999999:
  return -100000+pl if A(W if S>0 else X,-S) else 0
 T[k]=(d,best,2 if best<=al else 1 if best>=b else 0,bt)
 return best
def rt(ms):
 global N,S,C,E,H,W,X
 y0=len(Y)
 Y.append((tuple(B),S,C,E))
 N=0;best=ms[0];bs=[-999999]*len(ms)
 b0=B[:];s0=S;c0=C;e0=E;h0=H;w0=W;x0=X
 for d in range(1,40):
  try:
   nb=bs[:];al=-999999;bi=-1
   for k,i in enumerate(sorted(range(len(ms)),key=lambda j:-bs[j])):
    m=ms[i];u=mk(m)
    dr=H>=100 or Y.count(Y[-1])>1
    if dr:sc=0
    elif k==0:sc=-sr(d-1,-999999,999999,1)
    else:
     sc=-sr(d-1,-al-1,-al,1)
     if sc>al:sc=-sr(d-1,-999999,999999,1)
    uk(u);nb[i]=sc
    if sc>al:al=sc;bi=i
   bs=nb;best=ms[bi]
  except Z:break
 B[:]=b0;S=s0;C=c0;E=e0;H=h0;W=w0;X=x0;del Y[y0:]
 return best
while True:
 g=P("/game",{})
 if g["status"]=="done":break
 while g["status"]=="your_move":
  F(g["fen"])
  ms=[]
  for w in g["legal_moves"]:
   f=21+ord(w[0])-97+(int(w[1])-1)*10
   t=21+ord(w[2])-97+(int(w[3])-1)*10
   q="nbrq".index(w[4])+2 if len(w)==5 else 0
   ms.append(f+(t<<7)+(q<<14))
  m=rt(ms)
  f=m&127;t=m>>7&127;q=m>>14
  w="abcdefgh"[f%10-1]+str(f//10-1)+"abcdefgh"[t%10-1]+str(t//10-1)
  if q:w+="nbrq"[q-2]
  g=P("/move",{"game":g["game"],"move":w})
 print("game",g["game"],g["outcome"],file=sys.stderr)
