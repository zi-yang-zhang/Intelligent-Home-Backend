__author__ = 'robertzhang'


class Command:
    def __init__(self, command):
        self.code = command

    def __str__(self):
        print self.code