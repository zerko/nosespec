import logging
import inspect
import re

from nose.plugins import Plugin

NAMES_RE = re.compile('[Tt]est')

class SpecPlugin(Plugin):
    messages = {}
    def addSuccess(self,test):
        self.messages[self.spec_name].append(test.address()[-1].split('.')[-1])

    

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
