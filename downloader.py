#!/usr/bin/env python3
# Developer : Hamdy Abou El Anein
# hamdy.aea@protonmail.com

import requests
import json
import datetime
import sys


current_date = datetime.date.today()
current_date = current_date.strftime("%d-%m-%Y")


def reload():
    username = "hamdyaea"
    token = "46e780ca68e2c38ff7548a9e76e907b51013d02d"

    response = requests.get(
        "https://www.pythonanywhere.com/api/v0/user/{username}/reload/".format(
            username=username
        ),
        headers={"Authorization": "Token {token}".format(token=token)},
    )


def main():

    url = "https://unogs-unogs-v1.p.rapidapi.com/aaapi.cgi"

    querystring = {"q": "get:new7:CH", "p": "1", "t": "ns", "st": "adv"}

    headers = {
        "x-rapidapi-host": "unogs-unogs-v1.p.rapidapi.com",
        "x-rapidapi-key": "a1296b58a5msh0d1514001b88f9ep1afbcajsncfb2e503e33b",
    }

    data = requests.request("GET", url, headers=headers, params=querystring)
    data = data.text

    # ListNewRaw = data.decode("utf-8")
    ListNewJson = json.loads(data)
    total = ListNewJson["ITEMS"]
    totalcount = ListNewJson["COUNT"]
    movielist = []
    for i in total:
        topaste = (str("    Date : ")+ str(i["unogsdate"])+ str("     Title : ")+ str(i["title"])+str("     Rating : ")+str(i["rating"])+str("     Type : ")+str(i["type"])+str("     Released : ")+str(i["released"])+str("     Runtime : ")+str(i["runtime"]))
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
reload()
