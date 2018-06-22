import time

def memoin(valeur,place):
    f=open(place+".txt",'w')
    f.write(valeur)
    f.close()

def memoout(place):
    f=open(place+".txt","r")
    readen=f.read()
    f.close()
    return readen

def memoadd(valeur,place):
    f=open(place+".txt",'a')
    f.write("\n"+valeur)
    f.close()
#### edited
def memolineout(place):
    f=open(place+".txt","r")
    for line in f:
         print(line.replace("\n",""))
    f.close()
    return 0

def readlines(place):
    f=open(place+".txt","r")
    a=f.readlines()
    f.close()
    return a
hour=0
minute=0
nowcode=0
print("start" , time.strftime("%H,%M"))
counter=int(memoout("codetime"))#### read from file
print(counter , " minute(s) of code")
ctime=int(time.strftime("%M"))
while 1:

    if ctime  != int(time.strftime("%M")):
        ctime+=1
        counter+=1
        nowcode+=1
        minute=counter % 60
        memoin(str(counter),"codetime")
        print("minutes :" , counter,"(",minute,"mn and ",hour," hours" ,")"," now(",nowcode,")")
    if counter >= 60:
       hour=counter//60###
       minute=counter % 60
