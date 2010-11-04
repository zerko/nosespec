import logging
import inspect
import re

from nose.plugins import Plugin

NAMES_RE = re.compile('[Tt]est')

RED='\033[22;31m'
GREEN = '\033[22;32m'
WHITE = '\033[01;37m'

class Message(object):
    def __init__(self, text,color):
        self.text = "%s%s%s" % (color,text,WHITE)
        
    def __str__(self):
        return self.text

class SpecPlugin(Plugin):
    messages = {}
    def addSuccess(self,test):
        self.messages[self.spec_name].append(Message(test.address()[-1].split('.')[-1], GREEN))

    def addFailure(self,test,err):
        self.messages[self.spec_name].append(Message(test.address()[-1].split('.')[-1], RED))

    def startContext(self, context):
        if inspect.ismodule(context):
            self.spec_name = False
            return

        self.spec_name = str(context).split('.')[-1] 
        self.messages[self.spec_name] = list()

    def setOutputStream(self, stream):
        self.stream = stream
        return stream


    def finalize(self,result):
        self.stream.writeln("-------")
        for key,value in self.messages.iteritems():
            self.writeln(key)
            for x in value:
                self.writeln(' -%s' % x)

    def writeln(self,value):
        self.stream.writeln(self._clean(value))

    def _clean(self, value):
        return NAMES_RE.sub('',value).replace('_',' ')
