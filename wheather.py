'''
*****************************************************************************
@filename   : wheather.py
@author     : Ajay Prajapati
@teamLead   : Akash Kamble,Rajesh Dommaraju
@details    : It scraps the current temperature and next three day max and min 
              temperature.
@license    : SpanIdea Systems Pvt. Ltd. All rights reserved.
*****************************************************************************
'''
from tkinter import*
from bs4 import BeautifulSoup
import requests
import io
from PIL import Image,ImageTk
from urllib.request import urlopen
from urllib.request import urlretrieve
import time
import logging
import datetime
#install these modules in your system
#tkinter is Python GUI library and is used for front end design
#Beautifulsoup library is used for web scraping
#request library is used to get response from requested URL 



root=Tk()
#creating objecvt of tkinter
root.geometry("400x400")
#defining geometry of window

root.title("Wheather_India")

root.resizable(width=False, height=False)
label=Label(root,bg='black')
label.place(relheight=0.2,relwidth=0.2)

# window resizing is false

# setting the back ground image
background_image=PhotoImage(file='cloud.png')
background_label=Label(root,image=background_image)
background_label.place(x=0,y=0,relwidth=1,relheight=1)

def get_filename_datetime():
    # for getting file name of log file
    now = datetime.datetime.now()
    return "file-"+now.strftime("%Y-%m-%d %H:%M:%S")+".log"
name=get_filename_datetime()
#basic configuration for logging
logging.basicConfig(filename=name, level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s',datefmt='%d/%m/%Y %I:%M:%S %p',filemode="w+")


def get_wheather(city):
    '''function to get temperature deatils of city'''
       
    city_name=city  #Assiging name of city  to city_name
    url="http://www.timeanddate.com/weather/india/{0}".format(city_name)
    r=requests.get(url)
    print(r)
    
    data=r.text
    #getting source code of url
    l=list() #creating a list to hold temperature of necxt three days
    soup=BeautifulSoup(data,'lxml')
    images=[]
    m=[]
    
    images=soup.find_all('img')
    for image in images:
        m.append(image.get('src'))
    
     
    try:
        url_display='https:'+ m[2]
        print(url_display)
        urlretrieve(url_display,"local-filename.png")
    except:
        logging.info(v.set("THere is problem in city name1"))

   
 
    
          
    
    if f1.current_temp_check==1:
        #this block will execute if current temperature is selected
        try:
            
            current_temp=soup.find("div",{"class":"h2"})
            current_max_min_temp=soup.find_all("span")[2]
            v.set("Current Temperature of {0} is {1} \n Max and Min Temp{2} \n \n".format(city_name,current_temp.text, current_max_min_temp.text))
            img=PhotoImage(file="local-filename.png") 
            
            
            get_wheather.label1=Label(bottom_frame,image='',)
            get_wheather.label1.config(image=img)
            get_wheather.label1.image=img
            get_wheather.label1.place(relwidth=0.8,relheight=0.5,relx=0.1,rely=0.08)



#setting labels text with current tempearture

        except:
    
#if city name is not entered properly it will show the below exception
            
               logging.info(v.set("Please check your Indian city name \n \n \n \n"))
               
        
    else:
        try:
        #this block will execute if next three day temperature is selected
            img=PhotoImage(file="output-onlinejpgtools.png") 
            
            
            get_wheather.label1=Label(bottom_frame,image='',)
            get_wheather.label1.config(image=img)
            get_wheather.label1.image=img
            get_wheather.label1.place(relwidth=0.8,relheight=0.5,relx=0.1,rely=0.08)

           
            table=soup.find_all('table')
 
#The above line will return three table out of which we are selecting third table.
#then we are travesing through each row,for each row corresponding each cell
#is being travesed.Each cell's <p> tag is collected in list l.

            stat_table=table[2]
            for row in stat_table.find_all("tr"):
                for cell in row.find_all('td'):
                    for temp in cell.find_all('p'):
                        l.append(temp.get_text())
#Here we are reading list having date on index 2,3 and 4.
            logging.info(v.set("Max and Min Temp. of next three days \n {0} \n {1} \n {2}".format(l[2],l[3],l[4])))
        except:
            logging.info(v.set("Please check  your Indian city name \n \n \n"))


#Event defination
def f1(event):
    """Assign the value 1 to current_temp_check if current temp is selected"""
    f1.current_temp_check=1
   
   
        
def f2(event):
    """Assign the value 0 to current_temp_check if current temp is selected"""
    f1.current_temp_check=0              


#creating frame0 which will display Welcome message
frame0=Frame(root,bg='light pink')
frame0.place(relheight=0.1,relwidth=0.8,relx=.1,rely=.01 )
label_title=Label(frame0,text="Welcome! Check City Temperature",font=('arial', 10, 'bold'),fg='blue')
label_title.place(relheight=0.8,relwidth=1)

#creating  frame which will display entry box 
frame=Frame(root,bg='pink')
frame.place(relheight=0.2,relwidth=0.8,relx=.1,rely=.1)

#Embedding entry widget into frame
entry=Entry(frame)
entry.place(relheight=0.22,relwidth=0.5,height=15,width=15,relx=0.05,rely=0.27)

#placing button in frame
button=Button(frame,text="Get Whether",command=lambda: get_wheather(entry.get()))
button.place(relheight=0.4,relwidth=0.3,relx=0.65,rely=0.28)

#code for Radiobutton and genearting a event based on radio button click
rb1=Radiobutton(frame,text="Current Wheather",value=1)
rb1.place(relheight=0.2,relwidth=0.5)
rb1.bind('<Button-1>', f1)


#Radio button coorresponding to selecting time duration
rb2=Radiobutton(frame,text="Next three days",value=2)
rb2.place(relheight=0.2,relwidth=0.5,relx=0.5)
rb2.bind('<Button-1>', f2)


#parsing of source code
#This is bottom frame which will display temperature
bottom_frame=Frame(root,bg='pink')
bottom_frame.place(relheight=0.55,relwidth=0.8,relx=.1,rely=0.3,y=10)
v=StringVar()

label=Label(bottom_frame,textvariable=v,bg='pink')

label.pack(side='bottom')
root.mainloop()
