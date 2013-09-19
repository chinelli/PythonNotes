#!/usr/bin/env python

'''
Created on 19/set/2013

@author: proto
'''

#  Once passed, never reinitialize with =

class MutablePassing:
    def __init__(self,arg1):
        self.arg1=arg1
    def printArg1(self):
        print self.arg1
    def modifyArg1(self):
        self.arg1.__init__(['IN_CLASS_REPLACE'])
        
if __name__ == '__main__':
    
    argument=['Item1']
    instance=MutablePassing(argument)
    instance.printArg1()
    
    argument.append('ITEM2')
    instance.printArg1()
    
    instance.modifyArg1()
    print argument

    argument.__init__(['REPLACE'])
    instance.printArg1()
    
    
    

