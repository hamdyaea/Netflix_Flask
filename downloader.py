#!/usr/bin/env python3
# Developer : Hamdy Abou El Anein
# hamdy.aea@protonmail.com

import requests
import json
import datetime


current_date = datetime.date.today()
current_date = current_date.strftime("%d-%m-%Y")

def main():
    
    url = "https://unogs-unogs-v1.p.rapidapi.com/aaapi.cgi"

    querystring = {"q":"get:new7:CH","p":"1","t":"ns","st":"adv"}

    headers = {
    'x-rapidapi-host': "unogs-unogs-v1.p.rapidapi.com",
    'x-rapidapi-key': "YOUR-KEY-HERE"
    }

    data = requests.request("GET", url, headers=headers, params=querystring)
    data = data.text
    
    #ListNewRaw = data.decode("utf-8")
    ListNewJson = json.loads(data)
    total = ListNewJson["ITEMS"]
    totalcount =  ListNewJson["COUNT"]
    movielist = []
    for i in total:
        topaste = str("    Date : ")+str(i["unogsdate"])+str("     Title : ")+str(i["title"])
        movielist.append(topaste)
    
    datef = open("/home/hamdyaea/mysite/update.txt",'w')
    datef.write(str(current_date))
    datef.close()
    
    countf = open("/home/hamdyaea/mysite/counter.txt",'w')
    countf.write(str(totalcount))
    countf.close()
    
    movief = open("/home/hamdyaea/mysite/movies.txt","w")
    movief.write("")
    movief.close()
    
   
    for i in movielist:
        movief = open("/home/hamdyaea/mysite/movies.txt","a")
        movief.write(str(i))
        movief.write("\n")
        movief.close()        
        
    

main()
