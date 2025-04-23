#******************************************************************************************************
#                                       WELLCOME TO THE CODE OF HOUSIE
#******************************************************************************************************


#Libraries
from playsound import playsound
import random
import mysql.connector


#Initiating Database
mydb=mysql.connector.connect(host="localhost",user="root",passwd="olopcs")
mc=mydb.cursor()
mc.execute("create database if not exists tic_tec_toe")
mc.execute("use tic_tec_toe ")
mc.execute("""create table if not exists winner(name varchar(20),position int,date datetime)""")


#default Setting           
voice="female"
sound_s="off"
auto_win="on"
winner=[]
pcard=True

#****************************************************Functions******************************************************  

#Function for checking winners
def win(x,y):
    flag="true"
    for i in range(1,16):
        if y[i] in x:
            
            flag="true"    
        else:
            flag="False"
            break
    if flag=="true":
        m=y[0]
        if namel[m] not in winner:
            winner.append(namel[m])
            print(" "*30,namel[m],"WON!!!!!!!!!!!")
            playsound("win.mp3")
            sql="""insert into winner values(%s,%s,now())"""
            val=(namel[m],len(winner))
            mc.execute(sql,val)
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")


#for showing winner            
def show_winner():
    c=input("Enter the name of player you want to see the history of")
    if c=="all" or c=="All" or c=="ALL":
        mc.execute("""select * from winner;""")
        temp_store=mc.fetchall()
        print("\n\n")
        print(30*" ",41*"*")
        print(30*" ","|{0:^8}|{1:^8}|{2:^8}          |".format("Name","Position","Date & Time"))
        print(30*" ",41*"*")
        for i in temp_store:
            print(30*" ","|{0:^8}|{1:^8}|".format(i[0],i[1]),i[2],"|")
        
        j=input()    
        print("\n\n\n\n")
    else:
        mc.execute("""select * from winner where name='"""+c+"';")
        temp_store=mc.fetchall()
        print("\n\n")
        print(30*" ",41*"*")
        print(30*" ","|{0:^8}|{1:^8}|{2:^8}          |".format("Name","Position","Date & Time"))
        print(30*" ",41*"*")
        for i in temp_store:
            print(30*" ","|{0:^8}|{1:^8}|".format(i[0],i[1]),i[2],"|")
            
        j=input()    
        print("\n\n\n\n")

#Settings menue
def setting():
        global sound_s
        global voice
        global auto_win
        print("  *********************          *************************   ") 
        print("  *  1.Sound Setting  *          *  2.Gameplay settings  *   ")
        print("  *********************          *************************   ") 
        setting_c=input("---->")
        if setting_c=="1":
            if sound_s=="on" or sound_s=="On" or sound_s=="On":
                sound_s_temp="off"
            elif sound_s=="Off" or sound_s=="OFF" or sound_s=="off" :
                sound_s_temp="on"
            if voice=="male":
                voice_temp="female"
            else:
                voice_temp="male"
            
            print("Type '"+sound_s_temp+"'"" To turn",sound_s_temp,"The Sound")
            print("To change voice from",voice,"voice to",voice_temp,"voice type 'c'")
            setting_c1=input("---->")
            
            if setting_c1=="off" or setting_c1=="Off" or setting_c1=="OFF":
                sound_s="off"
                
            elif setting_c1=="on" or setting_c1=="ON" or setting_c1=="On":
                sound_s="on"
            
            elif setting_c1=='c' or setting_c1=="C":
                if voice=="male":
                    voice="female"
                else:
                    voice="male"
        else:
            global pcard
            print("To turn on Auto Win Type 'ON'\nTo turn off Auto Win Type'off'")
            print("\n")
            if pcard==True:
                print("If you do not want to have card Type 'n'\n                Note:Turning of this feature auto win will also be turned off")
            else:
                print("If you want to have card Type 'y'")
            c=input("---->")
            if c=='on' or c=='On' or c=='ON':
                auto_win="on"
            elif c=="n":
                pcard=False
                auto_win="off"
            elif c=="y":
                pcard=True
               
            else:
                auto_win="off"


#Showing player card
def print_card(crs,name):
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("card of",name,"is:-")
    print("|{0:^8}|{1:^8}|{2:^8}|{3:^8}|{4:^8}|".format(crs[1],crs[2],crs[3],crs[4],crs[5]))
    print("")
    print("|{0:^8}|{1:^8}|{2:^8}|{3:^8}|{4:^8}|".format(crs[6],crs[7],crs[8],crs[9],crs[10]))
    print("")
    print("|{0:^8}|{1:^8}|{2:^8}|{3:^8}|{4:^8}|".format(crs[11],crs[12],crs[13],crs[14],crs[15]))
    print("\n\n\n\n")


#***********************************************GAMEPLAY****************************************************************************************

    
while True:
    mc.execute("""create table if not exists Player_card(id int,val1 int,val2 int,val3 int,val4 int,val5 int,val6 int,val7 int,val8 int,val9 int,val10 int,val11 int,val12 int,val13 int,val14 int,val15 int)""")
     #StartUp Menue
    print("             ********************************          ************************************")
    print("             **                            **          **                                **")
    print("             **     Press 1.  To  Start    **          **    Press 2.  For   Settings    **")
    print("             **                            **          **                                **")
    print("             ********************************          ************************************")
    print()
    print("                              ******************************************")
    print("                              **                                      **")
    print("                              **    Press 3.  For   Winner History    **")
    print("                              **                                      **")
    print("                              ******************************************")
    print("\n\n")
    print("******************************************************************************************************")
    print("\n\n\n\n")
    start_c=input("")
    if start_c=="1":
        print("                          ****************************************************")
        print("                          *                  Settings Review                 *")
        print("                          ****************************************************")
        print("                                           Sound     --->",sound_s)
        print("                                           Auto Win  --->",auto_win)

        if sound_s=="on" or sound_s=="ON" or sound_s=="On":
            print("                                           Voice     --->",voice)
        print("                                                                             press s to go to setting")
        print("                                                                                press enter to start:)")
        bw=input()
        if bw=="s" or bw=="S":
            setting()
        

        print("Enter the no of Plyers Playing The Game")
        player=input("----->")
        
        np=int(player)
        cr=0
        namel=[]
        p_id=-1
        
        for i in range(0,np):
            p_id=p_id+1
            crs=[]
            print("Enter The name of player")
            name=input()
            namel.append(name)
            for z in range(1,17):
                while cr in crs:
                        cr=random.randint(1,100)
                crs.append(cr)
            if pcard==True:
                print_card(crs,name)
            
            msql="insert into Player_card values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            val=(p_id,crs[1],crs[2],crs[3],crs[4],crs[5],crs[6],crs[7],crs[8],crs[9],crs[10],crs[11],crs[12],crs[13],crs[14],crs[15])
            mc.execute(msql,val)
            mydb.commit()
            
        
        print(50*" ","To stop the game press 's'")
        st=[]
        ran=0
        for i in range(1,101):
            
            while ran in st:
                ran=random.randint(1,100)
            st.append(ran)
            nex=input("To Get The Next Number Press 'enter'")
            if nex=="s" or nex=="S":
                break
            print()
            print("And the no is",ran,"!!!")
            print("\n\n")
            
            if auto_win=="on":
               mc.execute("select id,val1,val2,val3,val4,val5,val6,val7,val8,val9,val10,val11,val12,val13,val14,val15 from player_card")
               r=mc.fetchall()
               for row in r:
                   
                   win(st,row)
            
            print(len(st))
            if sound_s=="on" or sound_s=="On" or sound_s=="On": 
                tempString=str(ran)
                playsound("d.m4a")
                if voice=="female":
                    for i in tempString:
                        if i=="0":
                            playsound("0.mp3")                               #For Playing Sound
                        elif i=="1":
                            playsound("1.mp3")
                        elif i=="2":
                            playsound("2.mp3")
                        elif i=="3":
                            playsound("3.mp3")
                        elif i=="4":
                            playsound("4.mp3")
                        elif i=="5":
                            playsound("5.mp3")
                        elif i=="6":
                            playsound("6.mp3")
                        elif i=="7":
                            playsound("7.mp3")
                        elif i=="8":
                            playsound("8.mp3")
                        elif i=="9":
                            playsound("9.mp3")
                else:
                    for i in tempString:
                        if i=="0":
                            playsound("0M.mp3")
                        elif i=="1":
                            playsound("1M.mp3")
                        elif i=="2":
                            playsound("2M.mp3")
                        elif i=="3":
                            playsound("3M.mp3")
                        elif i=="4":
                            playsound("4M.mp3")
                        elif i=="5":
                            playsound("5M.mp3")
                        elif i=="6":
                            playsound("6M.mp3")
                        elif i=="7":
                            playsound("7M.mp3")
                        elif i=="8":
                            playsound("8M.mp3")
                        elif i=="9":
                            playsound("9M.mp3")
            c=0
            if np==(len(winner)+1):
                break
        print(2*"\n")                
        print(41*" ","***Game Ended***")
        print(5*"\n")
        if pcard==False or auto_win=="off" :
            print("Do You Want To register winners?? y or n")
            i=input()
            if i=="y" or i=="Y":
                for x in range(0,np):
                    name=input("Enter the name of player:- ")
                    pos=int(input("Enter the position of player:-"))
                    sql="""insert into winner values(%s,%s,now())"""
                    val=(name,pos)
                    mc.execute(sql,val)
                
        print(39*" ","Winners are:-")
        
        for i in range(0,len(winner)):
            c=c+1
            print(34*" ",c,":-",winner[i])
        print(5*"\n")
        mc.execute("drop table Player_card")
        mydb.commit()    
    elif start_c=="2":
        setting()

    elif start_c=="3":
        show_winner()
        
        
#*****************************************THE END!!!!!!!!!!!!!!!!!!!!**********************************

            
