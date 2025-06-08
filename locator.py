import os
import subprocess
import logging
import sys

class Locator:
    def __init__(self):
        self.cmd = 'plocate' if self.__check_has_plocate() else None
        self.limit = 5

    def set_limit(self, limit):
        try:
            new_limit = int(limit)
            if new_limit > 0:
                self.limit = new_limit
            else:
                self.limit = 5 # Default to 5 if invalid
            print(('set limit to '+str(self.limit)))
        except ValueError:
            self.limit = 5 # Default to 5 if not a number
            print(('Invalid limit value, setting to default: '+str(self.limit)))

    def __check_has_plocate(self):
        try:
            subprocess.check_call(['which', 'plocate'])
            return True
        except:
            return False

    def run(self, pattern):
        if self.cmd == None:
            raise RuntimeError('command plocate not found')
        else:
            cmd = [self.cmd, '-i', '-l', str(self.limit)]
            args = pattern.split(' ')
            if args[0] == 'r':
                cmd.extend(args[1:])
            else:
                cmd.extend(args)
            print(('----->'+str(cmd)))
            output = subprocess.check_output(cmd)
            return output.splitlines()
