#!/usr/bin/env python3
import subprocess as sp
import json

JSON = '.remotecmd.json'


class RemoteCmd(object):
    def __init__(self):
        self.bindings = {}
        self.load()

    def load(self):
        try:
            with open(JSON) as infile:
                self.bindings = json.load(infile)
        except IOError:
            pass  # file not yet generated
        except ValueError:
            print('WRONG JSON!')

    def run(self):
        try:
            while True:
                proc = sp.Popen(['unbuffer', 'irw'], stdout = sp.PIPE)
                l = proc.stdout.readline().decode()
                proc.kill()
                key = l.split(' ')[2]
                if key:
                    self.load()
                    if key in self.bindings.keys():
                        cmd = self.bindings[key]
                        if cmd:
                            print('pressed: %s' % key)
                            sp.call(cmd, shell=True)
                    else:
                        self.new_key(key)
        except KeyboardInterrupt:
            pass

    def new_key(self, key):
        self.bindings[key] = ''
        print('new key pressed: %s' % key)

        with open(JSON, 'w') as outfile:
            json.dump(self.bindings, outfile, sort_keys=True, indent=4)


if __name__ == '__main__':
    t = RemoteCmd()
    t.run()
