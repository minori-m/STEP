import urllib2
import json

req = urllib2.urlopen("http://alice.fantasy-transit.appspot.com/net?format=json")
js = json.load(req)

def transit(dep,arr):
    for i in range(0,5):
        if dep in js[i]["Stations"]:
            print js[i]["Name"]
    return 0

def searchforline(station):
    line=[]
    for i in range(0,5):
        if station in js[i]["Stations"]:
            line.append(js[i]["Name"])
    if line == []:
        return 0
    else:
        print line
        return(line)

def searchfornext(station):
    line=[]
    for i in range(0,5):
        if station in js[i]["Stations"]:
            if js[i]["Stations"].count(station)==1:
                if js[i]["Stations"].index(station)>0:
                    if not js[i]["Stations"][js[i]["Stations"].index(station)-1] in line:
                        line.append(js[i]["Stations"][js[i]["Stations"].index(station)-1])
                if js[i]["Stations"].index(station)<len(js[i]["Stations"]):
                    if not js[i]["Stations"][js[i]["Stations"].index(station)+1] in line:
                        line.append(js[i]["Stations"][js[i]["Stations"].index(station)+1])
            else:
                print "else"
                if js[i]["Stations"][js[i]["Stations"].index(station):].index(station)>0:
                    if not js[i]["Stations"][js[i]["Stations"].index(station)-1] in line:
                        line.append(js[i]["Stations"][js[i]["Stations"][js[i]["Stations"].index(station):].index(station)-1])
                if js[i]["Stations"][js[i]["Stations"].index(station):].index(station)<len(js[i]["Stations"][js[i]["Stations"].index(station):]):
                    if not js[i]["Stations"][js[i]["Stations"].index(station)+1] in line:
                        line.append(js[i]["Stations"][js[i]["Stations"][js[i]["Stations"].index(station):].index(station)+1])
    



    return line


#transit("Seaside Beach",0)
print searchfornext("Tulgey Wood")
#print js[0]["Stations"].index("Seaside Beach")
