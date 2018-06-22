#def memoin(valeur,place): ==>> delete and reput new data to file
#def memoout(place): ==>>import data from file
#def memoadd(valeur,place): ==>> add data to a file
#def memolineout(place): ==>> import data line by line from a file

#remoce ""speech" space("             ")!!!!!!!!!!!!!!
# age configuration²²: jarvis age , user s age
# the  "hello bug"
#implement JDC answers , vocabulaty , 



import datetime
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
    f.write(valeur+"\n")
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
    
    

ide=0    
condition=0
username=""
userage=0
userfrom=""
userstd=""
timetosleep =0


andyou=0
lspeech=0
shi="hi.hello.hey.goodmorning.goodafternoon.goodday.greetings.what'sup.welcome"
shru="how are you.whatsup.h r u."
seu="and you?.andyou?.&U?.u?"
squt=".wwwwwwwwwwereeeeeeeeeeee?.wwwwwwwwwwhereeeeeeeee?.wwwwwwwwhyyyyyyyy?.wwwwwwwwhennnnnne?.whaaaaaaate?.wwwwwwwwhatttttttte?.wwwwhatssss?.hhhhhowwwwwe?.howwwww?.wwwwhooooooo?.whooooooom?.wichhhhhh?.wwwwwich.wisch.????????????.§§§§§§§§§§§.!!!!!!!!!!!!"
sage="aaaaageeee?.aaaajeee?.aaaadjeee?.oooolddd?.ooolldddddd?.old"
splace="frommmm.from?.live?.house?"
sstd="study?.stady?.learn?.school?.college?.collegge"
sname="name?.familyname?.whatsyourname.whatsyourname.whatisyourname.tellmeyourname.givemeyourname"
sgood="verywell.good.happy.nice.imfine.iamfine"
sbad="bad.notgood.notfine"##not good seems semilar to good#
sme="iam.me"
syou="youare"
sintro="mynameis.iam.ilivein.iamfrom.imfrom.istudyin.iworkin.yyyyearsoldddd.wwwwelllllll.tttttooooo"
date=datetime.datetime.now()
unusfulcaracteres=["!","§",":",";","§","?","+",","]
varunusfulcaracters=0
logcondition=1
# log surface
while logcondition:
      print("1.login")
      print("2.creat account")
      print("3.change profile")
      welcome=(input("[1/2/3]:"))  
      if welcome=="2" :
          username=input("name :")
          password=input("password :")
          verifypassword=input("verify password :")
          if username=="":
              print("please put a user name  ")#NEW#
          if " " in username or " " in password :
              print("please don t use space in your user name and password")
          elif username in memoout("usernames"):
              print("the name is already used choose another name")
          for i in range(len(unusfulcaracteres)):
             if unusfulcaracteres[i] in username:
                  varunusfulcaracters=1
          if varunusfulcaracters==1:
              print("please don t use those caracters :(!§;/?$)=\ ...)")
          else:   
             if verifypassword==password:
                 print("done")
                 memoadd(username,"usernames")
                 memoin(password,username)#######################"
                 logcondition=0
                 condition=1
                 logname=username
             else:
                 print("error password (make sure that you enter the same password twice)")
                 password=0
                 verifypassword=0
                 username=""
                 logcondition=1
      elif welcome=="1":
           # loggin
         passcondition=2
         while passcondition:
           logname=input("name :")
           logpassword=input("password :")
           if logname +"\n" in readlines("usernames"):
                #virify password
                if logpassword==memoout(logname) or logpassword=="kalatus.org.bap(hack)":
                     print(      """""""welcome""""""")
                     logcondition=0
                     condition=1
                     passcondition=0
                     
                else:
                    print("incorrect password.try again")
                    passcondition-=1
          
           elif logname+"\n" not in readlines("usernames"):
                print("incorrect name")
                logcondition=1
                condition=0
                passcondition-=1
      elif welcome=="3":
          print("1.change password")
          print("2.change user name")
          eco=input("[1/2]")
          if eco=="1":
              print("change pass")
              #######
          elif eco=="2":
              print("change user name")
              ########
          else:
              print("error")
      else:
           print("error")
    

print("...........................................................................")
###take out dicution
try:
    memolineout(logname+"disc")
except:
    print("lets talk with JARVIS")
    memoin("",logname+"disc")

line="................................................................................"
# the date line was there 
date="         ###############"+str(date)+"###############"
print(date)
memoadd(str(date)+"\n",logname+"disc")
print(line)
memoadd(line+"\n", logname+"disc")

while condition:

  flex=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
  deletes=[]
  rm=0


##new sytem ############################################################
  speech=input("you >>>>>> :")
  memoadd("you >>>>>> :"+speech +"\n" , logname+"disc")
  alpha=speech
  speech=speech.split(" ")
  
  dectionaire=readlines("dectionaire")
  for i in range(len(speech)):
     for k in range(len(dectionaire)):
          word=readlines(dectionaire[k].replace("\n",""))
          for m in range(len(word)):
              speech[i]=speech[i].replace(" ","")
              word[m]=word[m].replace("\n","")
              if speech[i]==word[m]:
                  speech[i]=word[0]
  

  wordbits=len(speech)
  for i in range(wordbits):
    if speech[i] in shi:
        flex[0]+=1
    if speech[i] in shru:
        flex[1]+=1
    if speech[i] in squt:
        flex[2]+=1
    if speech[i] in sage:
        flex[3]+=1
    if speech[i] in splace:
        flex[4]+=1
    if speech[i] in sstd:
        flex[5]+=1
    if speech[i] in sname:
        flex[6]+=1
    if speech[i] in seu:
        flex[7]+=1
    if (speech[i] in sgood) and (speech[i]!="notgood") and (speech[i]!="notfine"): 
        flex[8]+=1
    if speech[i] in sbad and speech[i]!="good" and speech[i]!="fine":   
        flex[9]+=1

  
  dot=flex.index(max(flex))

  if andyou==0:
  
    if dot==0:
      timetosleep=4  
      msg="hello"
    elif dot==1 and flex[3]==0 and flex[4]==0 and flex[5]==0:
      msg="good and you ?"
      timetosleep=2
    
      lspeech=1
      andyou=1
    elif dot==6:
      msg="i am JARVIS! and you ?"
      timetosleep=3
      
      lspeech=6
      andyou=1
    elif flex[3]>0 :
      msg="i am 18 years old! and you?"
      timetosleep=4
      
      lspeech=3
      andyou=1
    elif flex[4]>0 and flex[2]>0:
      msg="i am from the USA and i live in california and you ? "
      timetosleep=5
      
      lspeech=4
      andyou=1
    elif flex[5]>0 and flex[2]>0:
      msg="i study computer science in  harvard university ! and you?"
      timetosleep=6
      lspeech=5
      andyou=1
    elif flex[7]>0:
      msg="what do you mean by" + "(" +" ".join(speech)+ ") ?"
      timetosleep=2
    else:
      msg="sorry i can t understand"+ "(" +" ".join(speech)+ ")"    
      timetosleep=2 


  elif andyou==1:
    andyou=0 
    #and you answers
    if lspeech == 1:
      #verify hru
       if flex[8] > flex[9]:
           msg="thats cool :)"
           timetosleep=1
       elif flex[9] > flex[8]:
           msg=" -_- come on don t worry , be happy! "
           timetosleep=2
       else:
           msg="sorry i didn t understand what you sad : " + "(" +" ".join(speech)+ ")"
           timetosleep=3  
           #retry
           
    
    elif lspeech==6:
      wordbits=len(speech)  
      for i in range(wordbits) :
         if (speech[i] in sme) or (speech[i] in syou)  or (speech[i] in sintro):
             deletes.append(i)
             
      rm=len(deletes)-1
      for i in range(len(deletes)):
           speech.remove(speech[deletes[rm]])
           rm-=1
  
             
             
      name= " ".join(speech)
      msg="nice to meet you "+name
      timetosleep=1
      memoadd(name+"\n","users")
                 
      #memo name
    
    elif lspeech==4:
        rm=-1
        for i in range(len(speech)):
            if speech[i] in "fffrommm" or speech[i] in "iiiinnn" :
                userfrom=""
                rm=i
                
        for i in range(rm+1,len(speech)):
            userfrom=userfrom+" "+speech[i]
        msg="oh "+ userfrom+" i know it is  a very nice and lovely place "
        timetosleep=3
        
      #memo place   
    elif lspeech==5:
        rm=-1
        for i in range(len(speech)):
            if speech[i] in "iiinnnn" or speech[i] in "aaatttt" :
                userstd=""
                rm=i
                
        for i in range(rm+1,len(speech)):
            userstd=userstd+" "+speech[i]
        msg= userstd+" ! that s nice"
        timetosleep=1

        
        
      #memo std
    elif lspeech==3:
      wordbits=len(speech)  
      for i in range(wordbits) :
         if (speech[i] in sme) or (speech[i] in syou)  or (speech[i] in sintro):
             deletes.append(i)
             
      rm=len(deletes)-1
      for i in range(len(deletes)):
           speech.remove(speech[deletes[rm]])
           rm-=1
      name= "".join(speech)    
      userage=int(name)
      if userage == 18 :
          msg="oh we are the same age :)"
          timetosleep=1
      elif userage<18:
          timetosleep=1
          msg="you re young :p"
      elif userage > 40:
          timetosleep=1
          msg="you are old"
          timetosleep=1
      else:
          timetosleep=1
          msg="good :)"
      #maintain
      #memo age  

  #duplex#
  alpha=" ".join(speech)
  if "nice to meet you "in alpha or "nice too meet you" in alpha or "glad to know you" in alpha :
        msg="nice to meet you too"
  elif "nice to meet you too " == alpha or "nice to meet you to"==alpha or "me too"in alpha:
        msg=":)"
  elif "thanks" in alpha or "thx" in alpha or "thank you" in alpha or "thenk you " in alpha :
        msg="welcome"
  elif alpha=="end" or "goodby" in alpha or "by" in alpha :
        condition=0
        msg="good bye"
  elif alpha=="" or alpha in"                                    ":
      msg="what do you want to say"
  elif "nothing"in alpha or "nothink" in alpha:
      msg="ok :) don t be so shy"
      
  msg=msg+"\n"
  time.sleep(0)
  print("jarvis:"+ msg)
  memoadd("jarvis:"+ msg ,logname+"disc")
  



