#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- coding: latin-1 -*-
# -*- coding: euc-kr -*-

#Google Image Scraping Code
#Author: bariscankurtkaya
#Github: https://github.com/bariscankurtkaya
#Date: 29.09.2020

#LIBRARIES
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *
import re
import requests
import os
from bs4 import BeautifulSoup
import urllib.request as urllib2
import http.cookiejar
import json
import time
#LIBRARIES

#Geting desktop location
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
#If you use Linux
#desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop') 

class SearchPatent():

    def get_soup(self,url,header): #Opening URL function
        return BeautifulSoup(urllib2.urlopen(urllib2.Request(url,headers=header)),'html.parser')

    def __init__(self): #Interface function
        
        #Interface
        self.root = tk.Tk()
        self.root.configure(bg='light salmon')
        self.root.geometry('400x150') 

        #Labels
        self.pathLabel = tk.Label(self.root, text="Which  subject do you want to create data base:", bg="light salmon")
        self.progress=Progressbar(self.root,orient=HORIZONTAL,length=100,mode='determinate')

        #Textareas
        self.e0 = tk.Entry(self.root)

        #Buttons
        self.button = tk.Button(self.root,text="DOWNLOAD",command=self.createURL,bg="RoyalBlue2", fg="white")


        #Create labels and Textareas
        self.pathLabel.pack()
        self.e0.pack(fill=tk.X)

        #Create Buttons
        self.button.pack(padx=20,pady=20)

        #Interface Loop
        self.progress.pack(fill=tk.X)
        self.root.mainloop()


    def createURL(self): #Creating the URL and Downloading Images function

        #Creating URL
        query =(self.e0.get()).replace(" ","+")
        query= query.split()
        query='+'.join(query)
        url="https://www.google.co.in/search?q="+query+"&source=lnms&tbm=isch"
        print (url)
        header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}
        soup = self.get_soup(url,header)
        b=0
        #Scraping HTML and get Image
        for a in soup.find_all("a",{"class":"wXeWr"}):
            try:
                b+=1
                response = requests.get(str(a.find("img")['data-src']))
                file = open(query+str(b)+".jpg", "xb")
                print(b)
                file.write(response.content)
                file.close()
                self.progress['value'] = b
                self.root.update_idletasks()
                
            except Exception:
                continue     
        

        ###Show popup###
        top = Toplevel(bg="light salmon")
        top.title("FINISHED")
        top.geometry('400x160')
        msg = tk.Label(top, text="YOUR DATA BASE IS READY!",bg="light salmon",font=('Arial', 11, 'bold'))
        msg.pack(fill=tk.X, pady=20)
 
        button = tk.Button(top, text="Please shutdown and turn back.",bg="RoyalBlue2",fg="white", command=top.destroy)
        button.pack(padx=20, pady=20)
        ###Show popup end###


app=SearchPatent()

