#!/usr/bin/env python2.7

def isset(array, idx):
    try:
        array.index(idx)
        return True
    except:
        return False


groupids = []
groupnames = []
usernames = []
usergroupids = []

groupfile = open("/etc/group", "r")

for groupline in groupfile:
    string = groupline
    groupid = string.split(":")[2]
    groupids.append(groupid)
    
    groupname = string.split(":")[0]
    groupnames.append(groupname)

groupfile.close()


passwdfile = open("/etc/passwd", "r")

for userline in passwdfile:
    string = userline
    usergroupid = string.split(":")[3]
    usergroupids.append(usergroupid)
    
    username = string.split(":")[0]
    usernames.append(username)

passwdfile.close()

print("GROUPS")
nouser = []

i = 0
for groupid in groupids:
    if(isset(usergroupids, groupid)):
        print("|-[" + groupids[i] + "  " + groupnames[i] + "]")
    
        o = 0
        for usergroupid in usergroupids:
            if(usergroupid == groupid):
                print "|  +" + usernames[o]
            o +=1
    else:
        nouser.append(groupid + " " + groupnames[i])
    i +=1
    
print("\nGroups with no users in it:")
print nouser
