f = open(r'tmp2.json')
data = json.load(f)
f.close()

#shred1
excl={}
incl={}
melded={}
excl['nextupdate']=1
incl['drives']=2
melded['start']=4
melded['end']=4
excl['plays']=4
excl['crntdrv']=3
global daty
daty=[]
rider=[]
level=1
for firstlevelkey, firstlevelval in data.items():
    rider2=copy.deepcopy(rider)
    iterprint(daty,firstlevelkey,firstlevelval,incl,excl,melded,level,rider2)
#print(daty)
x=pivt(daty,4)
for ro in x:
    print(ro)
	

#shred2
excl={}
incl={}
melded={}
excl['nextupdate']=1
incl['drives']=2
incl['plays']=4
excl['players']=6
excl['crntdrv']=3
global daty
daty=[]
rider=[]
level=1
for firstlevelkey, firstlevelval in data.items():
    rider2=copy.deepcopy(rider)
    iterprint(daty,firstlevelkey,firstlevelval,incl,excl,melded,level,rider2)
print(daty)


#shred3
incl={}
excl={}
melded={}
excl['nextupdate']=1
incl['drives']=2
incl['plays']=4
incl['players']=6
excl['crntdrv']=3
global daty
daty=[]
rider=[]
for firstlevelkey, firstlevelval in data.items():
    rider2=copy.deepcopy(rider)
    iterprint(daty,firstlevelkey,firstlevelval,incl,excl,melded,level,rider2)
print(daty)


#shred4
incl={}
excl={}
melded={}
incl['stats']=3
incl['home']=2
incl['away']=2
excl['team']=4
excl['nextupdate']=1
global daty
daty=[]
rider=[]
level=1
for firstlevelkey, firstlevelval in data.items():
    rider2=copy.deepcopy(rider)
    iterprint(daty,firstlevelkey,firstlevelval,incl,excl,melded,level,rider2)
print(daty)
