#!/usr/bin/env python3
# Developer : Hamdy Abou El Anein
# hamdy.aea@protonmail.com

import requests
import json
import datetime
import sys


current_date = datetime.date.today()
current_date = current_date.strftime("%d-%m-%Y")


def reloader():
    username = "hamdyaea"
    api_token = "XXXXXX"
    domain_name = "hamdyaea.pythonanywhere.com"

    response = requests.post('https://www.pythonanywhere.com/api/v0/user/{username}/webapps/{domain_name}/reload/'.format(username=username, domain_name=domain_name),headers={'Authorization': 'Token {token}'.format(token=api_token)})
    if response.status_code == 200:
        print('reloaded OK')
    else:
        print('Got unexpected status code {}: {!r}'.format(response.status_code, response.content))


def main():

    url = "https://unogs-unogs-v1.p.rapidapi.com/aaapi.cgi"

    querystring = {"q": "get:new7:CH", "p": "1", "t": "ns", "st": "adv"}

    headers = {
        "x-rapidapi-host": "unogs-unogs-v1.p.rapidapi.com",
        "x-rapidapi-key": "XXX",
    }

    data = requests.request("GET", url, headers=headers, params=querystring)
    data = data.text

    # ListNewRaw = data.decode("utf-8")
    ListNewJson = json.loads(data)
    total = ListNewJson["ITEMS"]
    totalcount = ListNewJson["COUNT"]


    movielist = []
    movielist.append("<br><br>Developer : Hamdy Abou El Anein  -  hamdy.aea@protonmail.com<br>")
    #print(total)
    for i in total:
        topaste = (str("<strong>     Title : </strong>")+ str(i["title"])+str("<strong>     Rating : </strong>")+str(i["rating"])+str("<strong>     Type : </strong>")+str(i["type"])+str("<strong>     Released : </strong>")+str(i["released"])+str("<strong>     Runtime : </strong>")+str(i["runtime"])+str("<br>")+str(i["synopsis"])+str("<br><img src=")+str(i["image"])+str(">")+str("<br><hr><br>"))
        movielist.append(topaste)
    datef = open("/home/hamdyaea/mysite/update.txt", "w")
    datef.write(str(current_date))
    datef.close()

    countf = open("/home/hamdyaea/mysite/counter.txt", "w")
    countf.write(str(totalcount))
    countf.close()

    movief = open("/home/hamdyaea/mysite/movies.txt", "w")
    movief.write("")
    movief.close()

    for i in movielist:
        movief = open("/home/hamdyaea/mysite/movies.txt", "a")
        movief.write(str(i))
        movief.write("\n")
        movief.close()


main()
reloader()
