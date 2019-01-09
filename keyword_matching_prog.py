import pandas as pd
import csv
from food import food_fun
from edu_and_PD import edu_and_PD_fun
from healthfitness import healthfitness_fun
from travel import travel_fun
from expand_database import expand_database_fun
def keywordmatching(pas):
#def keywordmatching():

#########################################################################
#FOR VIDEO'S KEYWORD
    #l1="Kwality Walls Ice Cream Sandwich Chocolate and Vanilla (LWGaiMjceeo)"
    #l1="travel is Life"
    #l1="learn time"
    #l1="fitness vibes"
    l1=pas
    m=[]
    m.append(l1)
    #print(m)
    for teststring in m:
        #print(teststring)
        teststring=teststring+' '#adding ' ' at last
        
    videokeywordlist=[]
    ch=""
    
    for z in range(0,len(teststring)):
        if(teststring[z]!=' '):
            ch=ch+teststring[z]
        elif(teststring[z]==' '):
            videokeywordlist.append(ch)
            ch=""
    #print(videokeywordlist)
####################################################################
#FOR FILE "KEYWORD.CSV" LIST
    
    healthkeywordfile = pd.read_csv('health_keyword.csv', encoding='latin-1')
    Xh = healthkeywordfile.iloc[:, 0].values
    
    foodkeywordfile = pd.read_csv('food_keywords.csv', encoding='latin-1')
    Xf = foodkeywordfile.iloc[:, 0].values
    
    travelkeywordfile = pd.read_csv('travel_keywords.csv', encoding='latin-1')
    Xt = travelkeywordfile.iloc[:, 0].values
    
    edukeywordfile = pd.read_csv('edu_and_PD_keywords.csv', encoding='latin-1')
    Xe = edukeywordfile.iloc[:, 0].values
    
    
    
    ############################################################
    #print(len(X))
    #keywordlisttemp=[]
    healthkeywordlist=[]
    healthkeywordlist.append(Xh)
    hkeywordlist=[]
    for hi in healthkeywordlist:
        l1=hi[1]
    for key in range(0,len(healthkeywordfile)):
        #print(i[key])
        hkeywordlist.append(hi[key])
    
    
    
    edukeywordlist=[]
    edukeywordlist.append(Xe)
    ekeywordlist=[]
    for ei in edukeywordlist:
        l1=ei[1]
    for key in range(0,len(edukeywordfile)):
        #print(i[key])
        ekeywordlist.append(ei[key])
    
   
    foodkeywordlist=[]
    foodkeywordlist.append(Xf)
    fkeywordlist=[]
    for fi in foodkeywordlist:
        l1=fi[1]
    for key in range(0,len(foodkeywordfile)):
        #print(i[key])
        fkeywordlist.append(fi[key])

    travelkeywordlist=[]
    travelkeywordlist.append(Xt)
    tkeywordlist=[]
    for ti in travelkeywordlist:
        l1=ti[1]
    for key in range(0,len(travelkeywordfile)):
        #print(i[key])
        tkeywordlist.append(ti[key])
    
    
    
    #print(len(foodkeywordlist))
    for i in foodkeywordlist:
        l1=i[1]
    for key in range(0,14238):
        #print(i[key])
        fkeywordlist.append(i[key])
    
###############################################
 
    #MATCHING
    hmatchcount=0
    fmatchcount=0
    tmatchcount=0
    ematchcount=0
    
    for j in range(0,len(videokeywordlist)):
        for k in range(0,len(hkeywordlist)):
            if(videokeywordlist[j]==hkeywordlist[k]):
                hmatchcount+=1
    if(hmatchcount>0):
        print("Number of matches = ",hmatchcount)
        print("THE FOLLOWING VIDEO BELONGS TO HEALTH AND FITNESS BLOG")
        healthfitness_fun()
    
    
    for j in range(0,len(videokeywordlist)):
        for k in range(0,len(fkeywordlist)):
            if(videokeywordlist[j]==fkeywordlist[k]):
                fmatchcount+=1
    if(fmatchcount>0):
        print("Number of matches = ",fmatchcount)
        print("THE FOLLOWING VIDEO BELONGS TO FOOD VIDEO BLOG")
        food_fun()
    
    for j in range(0,len(videokeywordlist)):
        for k in range(0,len(tkeywordlist)):
            if(videokeywordlist[j]==tkeywordlist[k]):
                tmatchcount+=1
    if(tmatchcount>0):
        print("Number of matches = ",tmatchcount)
        print("THE FOLLOWING VIDEO BELONGS TO TRAVELO BLOG")
        travel_fun()
        
    for j in range(0,len(videokeywordlist)):
        for k in range(0,len(ekeywordlist)):
            if(videokeywordlist[j]==ekeywordlist[k]):
                ematchcount+=1
    if(ematchcount>0):
        print("Number of matches = ",ematchcount)
        print("THE FOLLOWING VIDEO BELONGS TO EDUCATIONAL BLOG")
        edu_and_PD_fun()
    
    if(hmatchcount==0 and fmatchcount==0 and tmatchcount==0 and ematchcount==0):
        print("NO VIDEO CATEGORY FOUND")
        choice=""
        
        
        choice=input("DO YOU WANT TO CATEGORISE VIDEO MANUALLY?(Y/N):")
        if(choice=='y' or choice=='Y'):
            print("SELECT CATEGORY OF VIDEO....")
            print("\n1. ICE-CREAM BRAND")
            print("\n2. HEALTH AND FITNESS")
            print("\n3. TRAVEL")
            print("\n4. EDUCATION AND PERSONALITY DEVELOPMENT")
            c=int(input("\nENTER YOUR CHOICE:"))
            
            
            if(c==1):
                c1=input("DO YOU WANT TO UPDATE CURRENT DATABASE?(y/n):")
                if(c1=='y' or c1=='Y'):
                    expand_database_fun("food_keywords.csv",videokeywordlist)
                    food_fun()
                elif(c1=='n' or c1=='N'):
                    food_fun()
                    
            
            elif(c==2):
                c1=input("DO YOU WANT TO UPDATE CURRENT DATABASE?(y/n):")
                if(c1=='y' or c1=='Y'):
                    expand_database_fun("health_keyword.csv",videokeywordlist)
                    healthfitness_fun()
                elif(c1=='n' or c1=='N'):
                    healthfitness_fun()
            
            
            elif(c==3):
                c1=input("DO YOU WANT TO UPDATE CURRENT DATABASE?(y/n):")
                if(c1=='y' or c1=='Y'):
                    expand_database_fun("travel_keywords.csv",videokeywordlist)
                    travel_fun()
                elif(c1=='n' or c1=='N'):
                    travel_fun()
            
            
            elif(c==4):
                c1=input("DO YOU WANT TO UPDATE CURRENT DATABASE?(y/n):")
                if(c1=='y' or c1=='Y'):
                    expand_database_fun('edu_and_PD_keywords.csv',videokeywordlist)
                    edu_and_PD_fun()
                elif(c1=='n' or c1=='N'):
                    edu_and_PD_fun()
            
            
            else:
                print("ENTER VALID CHOICE")
                
            
    
    
#keywordmatching()