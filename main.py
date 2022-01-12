#!/usr/bin/env python3
# Developer : Hamdy Abou El Anein
# hamdy.aea@protonmail.com

from flask import Flask, render_template, escape

app = Flask(__name__)

@app.route("/")
def main():
    with open('/home/hamdyaea/mysite/movies.txt') as f:
        movielist = f.readlines()
        movielist.reverse()  
    with open("/home/hamdyaea/mysite/update.txt") as f:
        update_date = f.readlines()
    dateup = update_date[0]
    
    with open("/home/hamdyaea/mysite/counter.txt") as f:
        totalcount = f.readlines()
    totalcount = totalcount[0]
    print(totalcount)
    return render_template("index.html",totalcount=totalcount,movielist=movielist,dateup=dateup)



