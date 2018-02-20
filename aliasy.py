#!/usr/bin/env python

from sys import argv
from subprocess import call

class Cli:
    def __init__(self, dbname):
        self.commands = []
        self.dbname = dbname

    def save(self, command):
        with open(self.dbname, 'a') as f:
            f.write(' '.join(command) + '\n')

    def match(self, alias):
        with open(self.dbname, 'r') as f:
            for line in f:
                if line.split(' ')[0] == alias:
                    return line[:-1].split(' ')[1:]
        return None

    def evaluate(self):
        if len(argv) == 1:
            print('Usage:\n  aliasy alias [command]')
            return

        if len(argv) == 2:
            command = self.match(argv[1])
            if command: return call(command)
            return None

        self.save(argv[1:])

if __name__ == '__main__':
    Cli('db').evaluate()
