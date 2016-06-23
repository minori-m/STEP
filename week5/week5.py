
import sys

f = open(sys.argv[1],'r')

def makedictfromdata(f):
    numofcell = f.readline()
    print numofcell

    for i in range(0, int(numofcell)):
        line = f.readline()
        if i==0 :
            dict = {line.strip():[100.0,0.0]}
        else :
            dict.update({line.strip():[100.0,0.0]})

#print dict

    line = f.readline()
    numofdirection = line

    for i in range(0,int(numofdirection)):
        line = f.readline()
        line = line.split()
        #print '%s,%s\n'%(line[0],line[1])
        dict[line[0]].append(line[1])

    return dict

def distribute(dict):
    for key in dict:
        if len(dict[key])-2 > 0:
            for i in range(0,len(dict[key])-2):
                dict[dict[key][2+i]][1] += dict[key][0]/(len(dict[key])-2)
        else : dict[key][1] += dict[key][0]
    return dict

def updatedict(dict):
    for key in dict:
        dict[key][0] = dict[key][1]
        dict[key][1] = 0.0
    return dict

def maxdifference(dict):
    max = 0.0
    for key in dict:
        if abs(dict[key][0]-dict[key][1]) > max : max =abs(dict[key][0]-dict[key][1])
    return max

def confirm(dict):
    sum = 0.0
    for key in dict:
        sum += dict[key][0]
    return sum

def show(dict):
    famous = 0
    person = "a"
    for key in dict:
        if famous < dict[key][0] :
            famous = dict[key][0]
            person = key
        print '%s : %s\n'%(key,dict[key][0])
    print 'most famous is %s'% (person)
    return famous

#main
dict = makedictfromdata(f)
max = 2.0

#print dict

while max>1:
    dict = distribute(dict)
    max = maxdifference(dict)
    dict = updatedict(dict)
#    print dict

show(dict)
print 'sum=%s'% (confirm(dict))