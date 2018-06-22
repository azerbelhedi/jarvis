#kalatus.org.bap :........... JDC admin login
#dect -ls : ...............list of dectionaires
#dect : ...............work with dectionaires
#mkdect :.............. make a new dectionaire
# user -ls :........................get users names and passwords
#dect -st : ................statistics(dectionaires/words)
#jdc -t : tree of dectionaires
#dect -s : search dectionaire
#user -s
#user -ls
#mkans
#ans -ls
#rmans
#rmdect
#history
#history -al
#history -n ++
#history -l
#alias
#alias -ls
#alias -cl
#history -cl
#dect -ad
#dect -more ++
#dect -dl
#ans -ad
#ans -dl
#cd <directory>
#cd
#pwd
#cd ..

#ans -more
#alias -dl
#history -dl -n (delete one history line)

### to do (jdc3) 

#bash -r (run code)
#bash -ls (list of codes)
#bash (type a new code)
#bash -h (bash help)
#help <argument> (argument special help)

## log interface ## :: / multi-users / pass config /

#####################################################################################
import os
import time
import weblib
####################################################################################
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
#............................................................................#
def readlines(place):
    f=open(place+".txt","r")
    a=f.readlines()
    f.close()
    return a
#...........................................................................#
def sdlt(s):
    for i in range(len(s)):
        if s[0]==" ":
            s=s[1:len(s)]
        
    for i in range(len(s)):
        if s[len(s)-1]==" ":
            s=s[0:len(s)-2]
    return s        
#............................................................................#        
def bash():
    conda=1
    while 1:
      b=input("bash_code:")
      b=sdlt(b)
      if b=="end":
          conda=0
          break
      elif b+"\n" in readlines("bash.admin"):
          print(b+" already used")
          b=""

      elif b!="":
          break

    if conda==1:
     try:
      memoin("bash_code:"+b,b+".bsh")
      memoadd(b,"bash.admin")
      while(1):
        beta=input()
        memoadd(beta,b+".bsh")
        if beta=="end":
            break
     except:
        print("bash_error")

#..............................................................................#        
def fldlt(s,n):
    print("start delete line")
######################################################################################
pwd=""
jdc="JDC:"
sudo=""
kal=""
workcondition=0
logcondition=1
vcondition=0
while logcondition:
  pwd=""
  if workcondition==1:
   try:
    for i in range (len(readlines("pwd.admin"))):
      pwd=pwd+"/"+readlines("pwd.admin")[i].replace("\n","")
   except:
      pwd=""
  welcome=(input(jdc+kal+pwd+sudo))
  repeat=1
#***************************************************************************#
  for i in range(len(welcome)):
      if welcome[i] != ' ':
          welcome=welcome[i:len(welcome)]
          break
  for i in range(len(welcome)):
      if welcome [len(welcome)-1-i]!=" ":
          welcome=welcome[0:len(welcome)-i]
          break
#***************************************************************************#

  while(repeat):
      repeat=0
      if welcome !="":
          memoadd(welcome,"hiscom.admin")
      if welcome == "kalatus.org.bap" or welcome=="kalatus.org.bap()" :
               passsudo=input("admin password:")
               if passsudo =="admin0000":
                   workcondition=1
                   kal="kalatus.org.bap:"
                   sudo="~$"
               else:
                   print("password invalid")
      elif welcome=="kalatus.v":
          vcondition=1
          workcondition=0
          kal="kalatus.v:"
          sudo=""
          pwd=""
#######################################################################################
      elif welcome=="user -ls" and workcondition==1:
         ##print users name and passwords
         for i in range(len(readlines("usernames"))):
             print(readlines("usernames")[i].replace("\n","")+"  >>>>  "+memoout(readlines("usernames")[i].replace("\n","")))
#######################################################################################
      elif welcome=="dect -ls"and (workcondition==1 or vcondition ==1):
          memolineout("dectionaire")
#######################################################################################
          # elif "new dectionaire"
      elif welcome=="mkdect" and workcondition==1 :
              newdectionairename=input("new dectionaire name :")
              memoin(newdectionairename.replace("\n",""),newdectionairename.replace("\n",""))
              memoadd(newdectionairename.replace("\n","").replace("\n",""),"dectionaire")
              newdectionairecondition=1
              while newdectionairecondition:
                  newdectionaireword=input("new word :").replace("\n","")
                  if newdectionaireword =="end":
                     newdectionairecondition=0
                  elif newdectionaireword != "new":
                    memoadd(newdectionaireword.replace("\n",""),newdectionairename.replace("\n",""))
#####################################################################################
      elif welcome=="help" and (workcondition==1  or vcondition==1):
          print("+ help :JDC's fonctions")
          print("+ kalatus.org.bap :........... JDC admin login")
          print("+ mkdect : ....................make a new dectionaire ")          
          print("+ dect -ls : ..................list of dectionaires")
          print("+ dect -ad : ..................add words to dectionaire")          
          print("+ dect -st : ..................statistics(dectionaires/words)")
          print("+ dect -s : ...................search dectionaire")
          print("+ dect -more : ................shows dectionaire 's words") 
          print("+ dect -dl : ..................delete words from dectionaire")           
          print("+ user -ls : ..................get users names and passwords")
          print("+ user -s : ...................search user ")          
          print("+ jdc -t : ....................tree of dectionaires")
          print("+ mkans : .....................made new answer")
          print("+ ans -ls : ...................list of answers")
          print("+ rmans : .....................removes answer")
          print("+ rmdect : ....................removes dectionaire")
          print("+ history : ...................shows commands history")
          print("+ history -al : ...............shows all the commands history")
          print("+ history -l : ................shows the last 25 commands history")
          print("+ history -n : ................runs a spesific history command")
          print("+ history -cl : ...............cleans the history ")
          print("+ alias : .....................made a link to a a command  ")
          print("+ alias -ls : .................shows the alias list")
          print("+ alias -cl : .................cleans the alias memory")
          print("+ cd <directory> : ............direct pwd to a spesific directoty")
          print("+ cd : ........................back to desktop (pwd)")
          print("+ pwd : .......................shows current directory details")
          print("+ cd .. : .....................back one degree in (pwd)")
          print("+ ans -ad : ...................adds a random answer to a spesific answer")
          print("+ ans -dl : ...................delete a random answer from a spesific answer")
        
########################################################################################          
      elif welcome == "dect -st" and (workcondition ==1 or vcondition==1):
          #<stat>
          print(str(len(readlines("dectionaire")))+" dectionaires" )
          #words#
          nwords=0
          for i in range (len(readlines("dectionaire"))):
              lista=readlines("dectionaire")
              nwords=nwords+len(readlines(lista[i].replace("\n","")))
          print(str(nwords)+" words")

          #</stat>
#######################################################################################
      elif ( (welcome=="tree") or(welcome =="jdc -t")) and (workcondition ==1 or vcondition==1):
          #<tree>#
          lista=readlines("dectionaire")
          for i in range (len(readlines("dectionaire"))):
              dect=lista[i].replace("\n","")
              print(dect+"____")
              for y in range (len(readlines(dect))):
                wordt=readlines(dect)[y].replace("\n","")
                print(" "*len(dect)  +"  |----+"+ wordt)
              print(" "*len(dect)  +"  |__ \n")
######################################################################################
           ##</tree>
      elif welcome =="dect -s" and workcondition ==1:
          sdex=input("dectionaire name:")
          lista=readlines("dectionaire")
          for i in range (len(readlines("dectionaire"))):
              if sdex in lista[i].replace("\n",""):
                  print(lista[i].replace("\n",""))
#######################################################################################
      elif  welcome=="user -s" and workcondition==1:
         ##print users name and passwords
         suser=input("user name:  " )

         for i in range(len(readlines("usernames"))):
             if suser in readlines("usernames")[i].replace("\n",""):
                print(readlines("usernames")[i].replace("\n","")+"  >>>>  "+memoout(readlines("usernames")[i].replace("\n","")))
#######################################################################################
      elif welcome=="mkans" and workcondition ==1:
          #<make answer>
              newans=input("answer title :")
              memoin("",newans.replace("\n","")+".ans")
              memoadd(newans.replace("\n","").replace("\n",""),"answers")
              newansc=1
              while newansc:
                  newdectionaireword=input("answer :").replace("\n","")
                  if newdectionaireword =="end":
                     newansc=0
                  elif newdectionaireword != "new":
                    memoadd(newdectionaireword.replace("\n",""),newans.replace("\n","")+".ans")
######################################################################################
            #</makeanswer>
      elif welcome=="ans -ls"and (workcondition==1 or vcondition==1):
          memolineout("answers")
######################################################################################
      elif welcome=="rmans"and workcondition==1:
           nsrm=input("answer to remove :")
           try:
             os.remove(nsrm+".ans.txt")
             print("<"+nsrm+"> has been removed")
             #remove from the list answer #
             deleteddectionaire=(readlines("answers"))
             deleteddectionaire.remove(nsrm.replace("\n",""))
             for i in range(len(deleteddectionaire)):
                  if i==0:
                      memoin(deleteddectionaire[i].replace("\n",""),"answers")
                  else:
                     memoadd(deleteddectionaire[i].replace("\n",""),"answers")
           except :
               print("<"+nsrm+"> not found")
#####################################################################################
      elif welcome=="rmdect"and workcondition==1:
           nsrm=input("dectionaire to remove :")
           try:
             os.remove(nsrm+".txt")
             print("<"+nsrm+"> has been removed")
             #remove from the list answer #
             deleteddectionaire=readlines("dectionaire")

             deleteddectionaire.remove((nsrm+"\n"))

             for i in range(len(deleteddectionaire)):
                  if i==0:
                      memoin(deleteddectionaire[i].replace("\n",""),"dectionaire")
                  else:
                     memoadd(deleteddectionaire[i].replace("\n",""),"dectionaire")
           except :
            print("<"+nsrm+"> not found")
#######################################################################################
      elif welcome=="history -al" and workcondition ==1:
          hist=readlines("hiscom.admin")
          for i in range(len(hist)-1):
              print(str(i)+"/ "+hist[i].replace("\n",""))
######################################################################################
      elif welcome=="history" and workcondition ==1:
          hist=readlines("hiscom.admin")
          for i in range(len(hist)-1):
              if hist[i] in readlines("commands.admin") or hist[i] in readlines("alias.admin"):
                  print(str(i)+"/ "+hist[i].replace("\n",""))
######################################################################################
      elif welcome=="history -l" and workcondition==1:
          hist=readlines("hiscom.admin")
          for i in range(len(hist)-1):
              if i>= len(hist)-27:
                  print(str(i)+"/ "+hist[i].replace("\n",""))
#######################################################################################
      elif welcome[0:11] =="history -n " and workcondition ==1:
            try:
              n=int(welcome[11:len(welcome)])
              welcome=(readlines("hiscom.admin"))[n].replace("\n","")
              
              repeat=1
            except :
                print()
          ######### <alias interface>
######################################################################################
      elif welcome == "alias -ls" and workcondition ==1:
           for i in range (0,len(readlines("alias.admin"))-1,2):
               print(readlines("alias.admin")[i].replace("\n","")+"....."+readlines("alias.admin")[i+1].replace("\n",""))
######################################################################################          
      elif welcome=="alias -cl" and workcondition ==1:
         try:
          os.remove("alias.admin.txt")
          memoin("h","alias.admin")
          memoadd("history","alias.admin")
          print("alias clean")
         except:
             print("error 0007 : alias file not found")
          ###### <alias interface/>
#####################################################################################
      elif welcome[0:5] =="alias" and "=" in welcome and workcondition ==1 and welcome!="alias -ls":
          ncom=""
          try:
            for i in range(6,len(welcome)):
              if welcome[i]!="=":
                  ncom=ncom+welcome[i]
                  index=i+1
              else:
                  break
            com=""
            for i in range(index+1,len(welcome)):
                if welcome[i]!='"':
                  com=com+welcome[i]
            if ncom+"\n" in readlines("alias.admin"):
                print("<"+ncom+"> already used")                

            else:
                memoadd(ncom,"alias.admin")
                memoadd(com,"alias.admin")
                print("alias : <"+ncom +"> saved as <"+com +">")

          except:
              print()
####################################################################################              
      elif welcome+"\n" in readlines("alias.admin") and workcondition==1:
          for i in range(len(readlines("alias.admin"))-1):
              if readlines("alias.admin")[i].replace("\n","")==welcome:
                  welcome=readlines("alias.admin")[i+1].replace("\n","")
                  repeat=1
                  break
#####################################################################################
      elif welcome=="history -cl" and workcondition ==1:
         try:
          os.remove("hiscom.admin.txt")
          memoin("history -cl","hiscom.admin")
          print("history clean")
         except:
             print("error 0008 : history file not found")
#####################################################################################
      elif welcome== "dect -ad" and workcondition ==1:
          dectionairename=input("dectionaire name : ")
          dectionairenamecondition=1
          if dectionairename+"\n" in readlines("dectionaire"):
           while dectionairenamecondition:
            decnamea=input("word :")
            if decnamea=="end":
                dectionairenamecondition=0
            else:
                memoadd(decnamea,dectionairename)
          else :
              print("<"+dectionairename+"> not found ")
######################################################################################         
      elif welcome=="dect -more" and (workcondition==1 or vcondition==1):
          #to modify
          dectionairename=input("dectionaire name : ")
          try:
           for i in range (len(readlines(dectionairename))):
               print(str(i)+"/ "+readlines(dectionairename)[i].replace("\n",""))
          except:
              print("<"+ dectionairename +"> not found ")
######################################################################################
      elif welcome=="dect -dl" and workcondition==1:
        dectionairename=input("dectionaire name : ")
        if dectionairename+"\n" in readlines("dectionaire"):
          dectionairecondition=1
          while dectionairecondition :
            alphaword=input("delete word :")
            if alphaword=="end":
                dectionairecondition=0
            else :
                deleteddectionaire=(readlines(dectionairename))
                try:
                  deleteddectionaire.remove(alphaword)
                except:
                    print("<"+alphaword +"> not in <"+dectionairename+"> dectioniare")
                for i in range(len(deleteddectionaire)):
                    if i==0:
                        memoin(deleteddectionaire[i].replace("\n",""),dectionairename)
                    else:
                        memoadd(deleteddectionaire[i].replace("\n",""),dectionairename)
        else:
            print("<"+dectionairename +"> not found")
#####################################################################################
      elif welcome== "ans -ad" and workcondition ==1:
          dectionairename=input("answer title : ")
          dectionairenamecondition=1
          for i in range(len(readlines(dectionairename+".ans"))):
              print(str(i)+"/ "+ readlines(dectionairename+".ans")[i].replace("\n",""))
          if dectionairename+"\n" in readlines("answers"):
           while dectionairenamecondition:
            decnamea=input("answer :")
            if decnamea=="end":
                dectionairenamecondition=0
            else:
                memoadd(decnamea,dectionairename+".ans")
          else :
              print("<"+dectionairename+"> not found ")
###################################################################################### 
      elif welcome=="ans -dl" and workcondition==1:
        dectionairename=input("answer title : ")
        if dectionairename+"\n" in readlines("answers"):
          dectionairecondition=1
          for i in range(len(readlines(dectionairename+".ans"))):
              print(str(i)+"/ "+ readlines(dectionairename+".ans")[i].replace("\n",""))
          while dectionairecondition :
            alphaword=input("delete answer :")
            if alphaword=="end":
                dectionairecondition=0
            else :
                deleteddectionaire=(readlines(dectionairename+".ans"))
                try:
                  deleteddectionaire.remove(alphaword+"\n")
                except:
                    print("<"+alphaword +"> not in <"+dectionairename+"> answer")
                for i in range(len(deleteddectionaire)):
                    if i==0:
                        memoin(deleteddectionaire[i].replace("\n",""),dectionairename+".ans")
                    else:
                        memoadd(deleteddectionaire[i].replace("\n",""),dectionairename+".ans")
        else:
            print("<"+dectionairename +"> not found")
###############################################################################
                            ######  -pwd- ######
#####################################################################################
      elif welcome[0:3]=="cd " and workcondition ==1 and welcome !="cd ..":
             if welcome[3:len(welcome)]!="":
                 repeata=1
                 welcome=welcome[3:len(welcome)]
                 while repeata:
                   repeata=0
                   aa=0
                   for i in range(len(welcome)):
                         if welcome[i]=="/":
                           aa=i
                           welcome2=welcome
                           welcome=welcome[0:i]
                           
                           repeata=1
                           break
                   try:
                    if len(readlines("pwd.admin"))!=0:   
                     memoadd(welcome[0:len(welcome)],"pwd.admin")
                   except :
                       memoin(welcome[0:len(welcome)],"pwd.admin")
                   pwd=pwd+welcome[0:len(welcome)]
                   if repeata==1:
                       welcome=welcome2[aa+1:len(welcome2)]
                       
###############################################################################
      elif welcome=="cd" and workcondition ==1:
         try: 
          os.remove("pwd.admin.txt")
         except:
             print("desktop")
##############################################################################
      elif welcome=="pwd" and workcondition==1:
         pwdf=pwd[1:len(pwd)]
         if len(pwd)==0:
          pwdf="desktop"  
          print("pwd >>>> "+ pwdf)
         else:
          try:
           print(readlines("pwd.admin"))
          except:
             print("error <file\"pwd\" not found> ")
##############################################################################
      elif welcome=="cd .."and workcondition ==1:
          try:
              if len(readlines("pwd.admin"))>1:
                  lista=readlines("pwd.admin")
                  lista.remove(lista[len(lista)-1])
                  for i in range(len(lista)):
                      if i==0:
                          memoin(lista[i].replace("\n",""),"pwd.admin")
                      else:
                          memoadd(lista[i].replace("\n",""),"pwd.admin")
              elif len(readlines("pwd.admin"))==1:
                  repeat=1
                  welcome="cd"
          except:
              print()
###############################################################################
      elif welcome=="logout":
          workcondition=0
          vcondition=0
          kal=""
          pwd=""
          sudo=""
##############################################################################
      elif welcome[0:4]=="echo":
          print(welcome[5:len(welcome)])
##############################################################################
      elif welcome=="bash":
          print("#jdc_bash")
          bash()
##############################################################################
      elif welcome=="bash -ls":
              try:
                  for i in range(len(readlines("bash.admin"))):
                   s=readlines("bash.admin")[i].replace("\n","")
                   if s!="":
                    print(readlines("bash.admin")[i].replace("\n",""))
              except:
                  print("bash not found")
##############################################################################
      elif welcome[0:7]=="bash -r":
          code_name=welcome[8:len(welcome)]
          print(code_name)
#############################################################################          
      elif welcome[0:8]=="bash -dl":
          code_name=welcome[9:len(welcome)]
          print(code_name)
###############################################################################
      else:
        weblib.test(welcome)
################################################################################
     # elif welcome=="sudo rm /rf":
          #remove system
###############################################################################
      #elif welcome=="sudo rm /rm":
          #clean and keep system
###############################################################################
     #mkfl (make file)
###############################################################################
     #file_name -more (open file)
###############################################################################
     #ls (list of files)
###############################################################################
     #(modify file from the prompt window)
###############################################################################
     #echo ( write function)
###############################################################################
     #mkdect -a <dect name>   (make an automatic dect from one original word)
##############################################################################
     #run "outJDC"codes (i.g : jcounter, jarvis)
##############################################################################
     #user <new account>
##############################################################################
     #propos <commnad>
##############################################################################     
     #configure kalatus.v and kalatus.org.bap rights
     # controle history more with more freedom (i.g : delete some hi-lines)
     #tools : (i.g : calculator , schudle , note , )
     #logout ==> close the JDC window (delay (5s))     
##############################################################################