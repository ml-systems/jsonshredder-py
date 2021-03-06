import json
import types
from io import StringIO
import copy

def iterprint(dat,objkey,objval,included={},excluded={},melded={},level=1,rider=[]):
#    print('printing')
#    if str(objkey)==includekey and level==includelevel
#    print(str(level)+','+str(isinstance(objval,list)))
#    print ('prea'+str(objkey))
#    print ('a,'+str(melded.get(str(objkey),"")))
#    print ('c,'+str(level))
    global daty
    daty=dat
    if included.get(str(objkey),"")==level or level not in included.values():
        if excluded.get(str(objkey),"")!=level:
            if isinstance(objval,dict):
                if not rider:
                    #if isinstance( objkey, int ):
                        #print(objkey)
                    rider.append(objkey)
                else:
                    
                    if melded.get(str(objkey),"")==level:
                        if rider[len(rider)-1][-1]=='-':
                            rider[len(rider)-1]+=(str(objkey)+'-')
                        else:
                            rider.append(str(objkey)+'-')
                    else:
                        if rider[len(rider)-1][-1]=='-':
                            rider[len(rider)-1]+=str(objkey)
                        else:
                            rider.append(objkey)
                level+=1
                for dictkey, dictval in objval.items():
                    rider2 = copy.deepcopy(rider)  
                    iterprint(daty,dictkey,dictval,included,excluded,melded,level,rider2)
            elif isinstance(objval,list):
                if not rider:
                    rider.append(objkey)
                else:
                    if melded.get(str(objkey),"")==level:
                        if rider[len(rider)-1][-1]=='-':
                            rider[len(rider)-1]+=(str(objkey)+'-')
                        else:
                            rider.append(str(objkey)+'-')
                    else:
                        if rider[len(rider)-1][-1]=='-':
                            rider[len(rider)-1]+=str(objkey)
                        else:
                            rider.append(objkey)

                level+=1
                for itm in objval:
                    if isinstance(itm,dict):
                        for dictkey, dictval in itm.items():
                            rider2 = copy.deepcopy(rider)
                            iterprint(daty,dictkey,dictval,included,excluded,melded,level,rider2)
                    elif isinstance(itm,list):
                        lkey=''
                        for lval in itm:
                            rider2 = copy.deepcopy(rider) 
                            iterprint(daty,lkey,lval,included,excluded,melded,level,rider2)
                    else:
                        if rider[len(rider)-1][-1]=='-':
                            rider[len(rider)-1]+=(str(objkey))
                            rider.append(objval)
                            #rider.append("\"%s\"" % objval if type(objval)==str else str(objval)) 
                            #print(rider)
                            daty.append(rider)
                            #print(daty)
                            rider=[]
                        else:
                            rider.append(objkey)
                            rider.append(objval)
                            #rider.append("\"%s\"" % objval if type(objval)==str else str(objval))
                            #print(rider)
                            daty.append(rider)
                            #print(daty)
                            rider=[]
            else:
                if not rider:
                    rider.append(objkey)
                    rider.append(objval)
                    #rider.append("\"%s\"" % objval if type(objval)==str else str(objval))
                    #print(rider)
                    daty.append(rider)
                    #print(daty)
                    rider=[]
                else:
                    if rider[len(rider)-1][-1]=='-':
                        rider[len(rider)-1]+=(str(objkey))
                        rider.append(objval)
                        #rider.append("\"%s\"" % objval if type(objval)==str else str(objval))
                        #print(rider)
                        daty.append(rider)
                        #print(daty)
                        rider=[]
                    else: 
                        rider.append(objkey)
                        rider.append(objval)
                        #rider.append("\"%s\"" % objval if type(objval)==str else str(objval))
                        #print(rider)
                        daty.append(rider)
                        #print(daty)
                        rider=[]


def gameidof(jsonobj):
    for key, value in jsonobj.items():
        if key!='nextupdate':
            return str(key)
        
        

def pivt(originallist,pivotedcolumn):
    
#create set (unique collection) of the pivoted column values -pivotedcolumnset

    pivotedcolumnset=set()
    for originallistrow in originallist:
        #print(len(originallistrow))
        pivotedcolumnset.add(originallistrow[(pivotedcolumn-1)])
    pivotedcolumnsetlist=list(pivotedcolumnset)
    #convert that set into a dict with values (see b) pivotedcolumnsetdict
    #print('pivotedcolumnsetlist:')
    #print(pivotedcolumnsetlist)
    #print('')
    #print('')
    pivotedcolumnsetdict = {}
    vals = range(len(originallist[0])-1,len(originallist[0])+len(pivotedcolumnset)-1)
    for i in vals:
        pivotedcolumnsetdict[pivotedcolumnsetlist[i-len(originallist[0])-1]] = i

    #print('pivotedcolumnsetdict:')
    #for k in pivotedcolumnsetdict.keys():
    #    print(str(k) + ":" + str(pivotedcolumnsetdict[k]))
    #print('')
    #print('')

    #create set of every row (less pivoted column) -uniquewithoutpivotedmdlist

    withoutpivotedmdlist=[]
    for row in originallist:
        currentrowlist=[]
        for index, col in enumerate(row):
            if (index!=(pivotedcolumn-1) and index!=(len(row)-1)): currentrowlist.append(col)
            withoutpivotedmdlist.append(currentrowlist)

    #print('uniquewithoutpivotedmdlist:')
    #print(*uniquewithoutpivotedmdlist, sep='\n')
    #print('')
    #print('')

    #create new mdset with the column removed (automatically makes unique values- see link a)
    uniquewithoutpivotedmdlist = [list(x) for x in set(tuple(x) for x in withoutpivotedmdlist)]

    #add a column for each of the pivoted values in pivotedcolumnset
    #print('pivotedcolumnsetlist:')
    #print(*pivotedcolumnsetlist, sep='\n')
    #print('')
    #print('')

    for row in uniquewithoutpivotedmdlist:
        for key,val in pivotedcolumnsetdict.items():
            row.append('')

    #add a column for each of the pivoted values in pivotedcolumnset
    #print('pivotedcolumnsetlist:')
    #print(*pivotedcolumnsetlist, sep='\n')
    #print('')
    #print('')
    
    j=0        
            
    for pivotedcolumnsetdictkey, pivotedcolumnsetdictval in pivotedcolumnsetdict.items():
        for uniquewithoutpivotedmdlistrow in uniquewithoutpivotedmdlist:
            preuniquewpivoted=uniquewithoutpivotedmdlistrow[:(pivotedcolumn-1)]+[pivotedcolumnsetdictkey]+uniquewithoutpivotedmdlistrow[pivotedcolumn:-1]
            uniquewpivoted=preuniquewpivoted[:len(originallistrow)-1]
            for originallistrow in originallist:
                #print(originallistrow[:(pivotedcolumn-1)] + originallistrow[(pivotedcolumn) :-1])
                #print(originallistrow[(pivotedcolumn-1)])
                #print(''.join(map(str, originallistrow[:-1])))
                #print(''.join(map(str, uniquewpivoted)))
                #print(originallistrow[:-1])
                #print(uniquewpivoted[:len(originallistrow)-1])
                #if (originallistrow[:(pivotedcolumn-1)] + originallistrow[(pivotedcolumn) :-1]==uniquewithoutpivotedmdlistrow) and (str(originallistrow[(pivotedcolumn-1)])==str(pivotedcolumnsetdictkey):
                if originallistrow[:-1]==uniquewpivoted:
                    #j+=1
                    #print('hi')
                    #print(pivotedcolumnsetdictval)
                    #print(len(uniquewithoutpivotedmdlistrow))
                    #print(len(uniquewithoutpivotedmdlistrow[3]))
                    #print(uniquewithoutpivotedmdlistrow[pivotedcolumnsetdictval-1])
                    uniquewithoutpivotedmdlistrow[pivotedcolumnsetdictval-1]=originallistrow[-1]
    #print(j)
    return uniquewithoutpivotedmdlist