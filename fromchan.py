#!/usr/bin/env python3

from lxml.html import parse
from urllib.request import urlopen
from random import choice
from sys import argv
from subprocess import call
from time import sleep

ERROR = "http://sys.4chan.org/image/error/404/rid.php"
DISPLAY = "DISPLAY=:0 "  # X display for running via ssh
MONITOR = ""  # "-g 1024x768+1024+0"  to run on secondary monitor

TIME = 3.5  # showing time
SLIDE = False
SLIDE_TIME = 5

## argument parsing
args = argv[1:]
try:
    TIME = int(args[0])
    args = args[1:]
except (ValueError, IndexError):
    pass
#
try:
    if args[0]=='slide':
        SLIDE = True
        args = args[1:]
        SLIDE_TIME = int(args[0])
        args = args[1:]
except (ValueError, IndexError):
    pass
BOARDS = args
##


def grep():
    board = (choice(BOARDS) if BOARDS else 'b')
    urls = []
    try:
        pag = choice([""]+[str(i) for i in range(2,11)])
        with urlopen("http://boards.4chan.org/" + board + "/" + pag) as strm:
            urls += parse(strm).xpath("//a[@class='fileThumb']/@href")
        return "http:" + choice([u for u in urls if not (u.endswith(".webm") or u.endswith(".gif"))])
    except:
        return ERROR


def show(url):
    call(DISPLAY + "feh -Z -x " + MONITOR + " -B black " + url + " -D " + str(TIME) + " --cycle-once", shell=True)

try:
    if SLIDE:
        while True:
            show(grep())
            sleep(SLIDE_TIME - TIME)
    else:
        show(grep())
except KeyboardInterrupt:
    pass
