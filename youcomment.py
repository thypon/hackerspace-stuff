#!/usr/bin/env python3

from lxml.html import parse
from urllib.request import urlopen
from random import choice

with urlopen("http://www.youporn.com/random/video/") as strm:
    print(choice(parse(strm).xpath("//p[@class='message']/text()")))
