#!/usr/bin/env python3
# getting a *totally safe* image link from the internet (4chan/b/)
# by mr.fuji and others(tm)

from lxml.html import parse
from urllib.request import urlopen
from random import choice
from sys import argv
from subprocess import call

ERROR = "http://sys.4chan.org/image/error/404/rid.php"
DISPLAY = "DISPLAY=:0 "  # X display for running via ssh
MONITOR = ""  # "-g 1024x768+1024+0"  to run on secondary monitor
TIME = "3.5"  # showing time

board = (choice(argv[1:]) if argv[1:] else 'b')
urls = []
try:
    pag = choice([""]+[str(i) for i in range(2,11)])
    with urlopen("http://boards.4chan.org/" + board + "/" + pag) as strm:
        urls += parse(strm).xpath("//a[@class='fileThumb']/@href")
    url = "http:" + choice([u for u in urls if not (u.endswith(".webm") or u.endswith(".gif"))])
except:
    url = ERROR

call(DISPLAY + "feh -Z -x " + MONITOR + " -B black " + url + " & (PID=$! && sleep " + TIME + " && kill $PID)", shell=True)
