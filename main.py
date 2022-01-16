#!/usr/bin/env python3
# Developer : Hamdy Abou El Anein
# hamdy.aea@protonmail.com

from flask import Flask, render_template, escape
import logging
import socket
from logging.handlers import SysLogHandler
import sys

# Prepare logging to papertrail
syslog = SysLogHandler(address=('logs3.papertrailapp.com', 21249))
format = '%(asctime)s NetflixNewsApp: %(message)s'
formatter = logging.Formatter(format, datefmt='%b %d %H:%M:%S')
syslog.setFormatter(formatter)

logger = logging.getLogger()
logger.addHandler(syslog)
logger.setLevel(logging.INFO)

def my_handler(type, value, tb):
  logger.exception('Uncaught exception: {0}'.format(str(value)))

# Install exception handler
sys.excepthook = my_handler


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
    #print(totalcount)
    logger,info('Netflix app is running...')
    return render_template("index.html",totalcount=totalcount,movielist=movielist,dateup=dateup)



