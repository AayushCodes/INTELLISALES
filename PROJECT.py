#!/usr/bin/env python
# coding: utf-8

# In[8]:


#IMPORTING THE NECESSARY LIBRARIES AND PACKAGES FOR THE PROGRAM
import ipywidgets as widgets
import csv
from datetime import datetime,timedelta
import os


# In[9]:


#DEFINITION OF START FUNCTION 
def start() :
    
    #DISPLAY
    
    #CREATION OF BUTTON OBJECT
    toggle = widgets.Button(description='DISPLAY')
    
    #CREATION OF OUTPUT OBJECT 
    output = widgets.Output()
    
    #DISPLAYING BUTTON
    display(toggle, output)
    
    #DEFITION OF ACTION WHEN BUTTON GETS CLICKED
    def on_button_clicked(b):
        with output:
            os.system(r"C:\Users\sachin\Desktop\stuff\Retails_records.csv")
            
    #CALLING FUNCTION TO BE EXECUTED
    toggle.on_click(on_button_clicked)
    
    
#X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X


    #SELL
    
    toggle = widgets.Button(description='SELL')
    output = widgets.Output()
    display(toggle, output)
    def on_button_clicked(b):
        with output:
            
            #DEFINING SELL FUNCTION
            def sell(NAME, QUANTITY):
                toggle = widgets.Button(description='CONFIRM')
                output = widgets.Output()
                display(toggle, output)
                def on_button_clicked(b):
                    with output:
                        f = open(r"C:\Users\sachin\Desktop\stuff\Retails_records.csv",'r')
                        
                        #READER OBJECT
                        rl = csv.reader(f)
                        
                        #L1 WILL CONTAIN A COPY OF THE DATA IN THE FILE
                        l1 = []
                        for i in rl:
                            if i!=[] :
                                l1.append(i)
                        for j in l1: 
                            if j!=[] :
                                if j[1]==NAME:
                                    a = j[2]
                                    
                                    #REDUCTION OF QUANTITY OF SOLD OBJECT
                                    j[2]=int(j[2]) - int(QUANTITY)
                                    
                                    #IF INSUFFICIENT STOCK LEFT
                                    if int(j[2]) < 0 :
                                        print("Only", a , "Units Available")
                                        f.close()
                                    else: 
                                        f = open(r"C:\Users\sachin\Desktop\stuff\Retails_records.csv",'w')
                                        write = csv.writer(f)
                                        write.writerows(l1)
                                        f.close()
                toggle.on_click(on_button_clicked)
                
            #ACCEPTING NAME AND QUANTITY OF PRODUCT FROM USER AS PARAMETERS FOR SELL 
            widgets.interact(sell,NAME="",QUANTITY="")
            
            #CLEARING OUTPUT AS SOON AS NEXT ACTION TAKES PLACE
            output.clear_output(wait = True)
    toggle.on_click(on_button_clicked)
    
    
#X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X


    #NEW ENTRY
    toggle = widgets.Button(description='NEW ENTRY')
    output = widgets.Output()
    display(toggle, output)
    def on_button_clicked(b):
        with output:
            f = open(r"C:\Users\sachin\Desktop\stuff\Retails_records.csv",'r')
            data = csv.reader(f)
            
            #NEW SERIAL NUMBER CREATION
            l = []
            for i in data :
                if i!=[] : 
                    l.append(i[0])
            l = l[::-1]
            l = int(l[0]) + 1
            f.close()
            
            #DEFINING ENTRY FUNCTION WHICH INPUTS DATA INTO FILE
            def entry(NAME,QUANTITY,PRICE,PURCHASE,EXPIRY,PROFIT,PH_NO):
                
                #CHANGING DATE FORMAT TO DESIRED FORMAT
                PURCHASE = PURCHASE + "00:00:00"
                toggle = widgets.Button(description='CONFIRM')
                output = widgets.Output()
                display(toggle, output)
                def on_button_clicked(b):
                    with output:
                        f = open(r"C:\Users\sachin\Desktop\stuff\Retails_records.csv",'a')
                        cw=csv.writer(f)
                        cw.writerow([l,NAME,int(QUANTITY),int(PRICE),PURCHASE,int(EXPIRY),int(PROFIT),int(PH_NO)])
                        f.flush()
                        f.close()
                        print("New Entry Added")
                toggle.on_click(on_button_clicked)
            widgets.interact(entry,NAME="",QUANTITY="",PRICE="",PURCHASE="",EXPIRY="",PROFIT ="",PH_NO="")
            output.clear_output(wait = True)
    toggle.on_click(on_button_clicked)
        
        
#X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X
    
    
    #BUY
    toggle = widgets.Button(description='BUY')
    output = widgets.Output()
    display(toggle, output)
    def on_button_clicked(b):
        with output:
            def buy(NAME, QUANTITY, PURCHASE, EXPIRY):
                PURCHASE = PURCHASE + "00:00:00"
                toggle = widgets.Button(description='CONFIRM')
                output = widgets.Output()
                display(toggle, output)
                def on_button_clicked(b):
                    with output:
                        f = open(r"C:\Users\sachin\Desktop\stuff\Retails_records.csv",'r')
                        rl = csv.reader(f)
                        l1 = []
                        for i in rl:
                            if i!=[] :
                                l1.append(i)
                        for j in l1: 
                            if j!=[] :
                                if j[1]==NAME:
                                    
                                    #ADDITION OF QUANTITY OF BOUGHT OBJECT
                                    j[2]=int(j[2]) + int(QUANTITY)
                                    j[5] = EXPIRY
                                    j[4] = PURCHASE
                        f.close()
                        f = open(r"C:\Users\sachin\Desktop\stuff\Retails_records.csv",'w')
                        write = csv.writer(f)
                        write.writerows(l1)
                        f.close()
                toggle.on_click(on_button_clicked)
            widgets.interact(buy,NAME="",QUANTITY="",PURCHASE="",EXPIRY="")
            output.clear_output(wait = True)
    toggle.on_click(on_button_clicked)
    
    
#X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X
    
    
    #CHECK EXPIRY
    toggle = widgets.Button(description='CHECK EXPIRY')
    output = widgets.Output()
    display(toggle, output)
    def on_button_clicked(b):
        with output:
            f=open(r"C:\Users\sachin\Desktop\stuff\Retails_records.csv",'r')
            
            #GATHERING CURRENT DATE
            today = datetime.now()
            def disclaimer():
                r=csv.reader(f)
                for i in r:
                    if i != [] : 
                        l = i[5]
                        if l != '' :
                            
                            #CHANGING DATE OF PURCHASE INTO DESIRED FORMAT
                            dop = datetime.strptime(i[4], '%d-%m-%Y %H:%M:%S')
                            if int(l) < 5 : 
                                
                                #DEFINITION OF BUFFER DAYS TO BE ADDED 
                                DD1 = timedelta(days=int(l)-2)
                                
                                #ADDITION OF BUFFER DAYS INTO DATE OF PURCHASE
                                j1=dop + DD1
                                
                                #CONDITION FOR ALERT TO OCCUR
                                if j1<=today:
                                    print(i[1] ,"will expire in less than 2 days" ) 
                            elif int(l) < 31 : 
                                DD2 = timedelta(days=int(l)-5)
                                j2=dop + DD2
                                if j2<=today:
                                    print(i[1],"will expire in less than 5 days")
                            elif int(l) < 181 : 
                                DD3 = timedelta(days=int(l)-20)
                                j3=dop + DD3
                                if j3<=today:
                                    print(i[1],"will expire in less than 20 days")
                            elif int(l) > 180 : 
                                DD4 = timedelta(days=int(l)-30)
                                j4=dop + DD4
                            
                                if j4<=today:
                                    print(i[1],"will expire in less than 30 days")
       
            disclaimer()
            f.close()
        output.clear_output(wait = True)
    toggle.on_click(on_button_clicked)
    
    
#X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X
    
    
    #CHECK AVAILABILITY
    toggle = widgets.Button(description='CHECK AVAILABILITY')
    output = widgets.Output()
    display(toggle, output)
    def on_button_clicked(b):
        with output:
            f=open(r"C:\Users\sachin\Desktop\stuff\Retails_records.csv",'r')
            r=csv.reader(f)
            for i in r:
                if i != [] :
                    #DISPLAYS QUANTITY LEFT AND SUPPLIER IF QUANTITY OF ITEM IS LESS THAN 5
                    if int(i[2])<=5:
                        print('Quantity of',i[1],"is",int(i[2]),'units')
                        print('Kindly Contact',i[7])
        output.clear_output(wait = True)
    toggle.on_click(on_button_clicked)
        
        
#X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X
        
    
    #CLEAR
    toggle = widgets.Button(description='CLEAR')
    output = widgets.Output()
    display(toggle, output)
    def on_button_clicked(b):
        with output:
            output.clear_output()
    toggle.on_click(on_button_clicked)
    
    
#X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X

