HackerSpace Stuff
=================
(un)useful stuff that should not be missing in any hackerspace.

RemoteCmd
---------
Map remote control keys to custom commands. On first usage generates a
`.remotecmd.json` file and fills it with new keys pressed.

Depends on: `expect`, `lirc`

Light
-----
Turn __on__ and __off__ a light connected to parallel port.

    ./light.py [on|off]

Depends on: `python-parallel`

Before running:

    # TODO: insert command to init port and add user to group

YouComment
----------
__[NSFW]__ Print random comments from an _adult entertainment_ site.

    $ cowsay `./youcomment.py`
     _________________
    < she's beutiful! >
     -----------------
            \   ^__^
             \  (oo)\_______
                (__)\       )\/\
                    ||----w |
                    ||     ||

FromChan
--------
__[NSFW]__ Show random images from 4chan.

    ./fromchan.py [image_time] [slide [time]] [board1 [weight1] board2 [weight2] ...]

__WARNING:__ the default board is __/b/__

Depends on: `feh`

Toggle Screen
-------------

Set dpms mode on and off for screens. 


---

![BeerWare logo](https://upload.wikimedia.org/wikipedia/commons/thumb/d/d5/BeerWare_Logo.svg/116px-BeerWare_Logo.svg.png)
