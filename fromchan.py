#!/usr/bin/env python3

##show random images from 4chan
##usage: fromchan_w <display_time> [slide <off_time>] <board1> <chance_to_show1(integer, default is 50 if omitted)> <board2> ...
##or fromchan_w help to show help text

from lxml.html import parse
from urllib.request import urlopen, urlretrieve
from random import choice, randint
from sys import argv
from subprocess import call
from time import sleep
from threading import Thread

help_msg="usage:\n\t "+argv[0]+" <display_time> [slide <off_time>] <board1> <chance_to_show1(integer, default is 50 if omitted)> <board2> ...\n\tor:"+argv[0]+" help to show this message :)\n"

ERROR = "http://sys.4chan.org/image/error/404/rid.php"
DISPLAY = "DISPLAY=:0 "  # X display for running via ssh
MONITOR = "-g 1024x768+1024+0"  # to run on secondary monitor

TIME = 3.5  # showing time
SLIDE = False
SLIDE_TIME = 0

## argument parsing
args = argv[1:]

if "help" in args:
    print(help_msg)
    exit()

try:
    TIME = int(args[0])
    args = args[1:]
except (ValueError, IndexError):
    pass
##
try:
    if args[0]=='slide':
        SLIDE = True
        args = args[1:]
        SLIDE_TIME = int(args[0])
        args = args[1:]
except (ValueError, IndexError):
    pass

##

BOARDS = args or ['b']


##determine whether an argument is a number or not
def is_number(str):
    try:
        int(str)
        return True
    except ValueError:
        return False

probs={}
l=len(BOARDS)
i=0

##creating dictionary probs[<board>]=<chance>
while(i<l):
    try:
        if (not is_number(BOARDS[i])) and is_number(BOARDS[i+1]):
            probs[BOARDS[i]]=int(BOARDS[i+1])
            i+=1
        elif (not is_number(BOARDS[i])) and (not is_number(BOARDS[i+1])):
            probs[BOARDS[i]]=50
    except IndexError:
        probs[BOARDS[i]]=50
    i+=1


##choosing a board wisely-randomly
def notSoRandomBoard():
    tot = sum(probs.values())
    target=randint(1,tot)
    index=0
    for b,p in probs.items():
        if index+p >= target:
            return b
        else:
            index+=p


def grep():
    board=notSoRandomBoard()
    urls = []
    try:
        pag = choice([""]+[str(i) for i in range(2,11)])
        with urlopen("http://boards.4chan.org/" + board + "/" + pag) as strm:
            urls += parse(strm).xpath("//a[@class='fileThumb']/@href")
        return "http:" + choice([u for u in urls if not (u.endswith(".webm") or u.endswith(".gif"))])
    except:
        return ERROR


def download(url):
    path = '/tmp/%s' % url.split('/')[-1]
    urlretrieve(url, path)
    return path


def show(path):
    call(DISPLAY + "feh -Z -x " + MONITOR + " -B black " + path + " -D " + str(TIME) + " --cycle-once", shell=True)
    call('rm %s' % path, shell=True)


FIFO = []


class Downloader(Thread):
    def run(self):
        while True:
            if len(FIFO) < 10:
                FIFO.append(download(grep()))


try:
    if SLIDE:
        Downloader().start()
        while True:
            if FIFO:
                show(FIFO.pop(0))
                sleep(SLIDE_TIME)
    else:
        show(download(grep()))
except KeyboardInterrupt:
    pass
