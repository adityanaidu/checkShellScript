#!/usr/bin/env python

## Author Aditya Naidu
## $Id$

import re
import sys

## Add elements to checkList2 for additional checks
checkList2 = []

reexpDA = re.compile("\s*$@\s*")
checkList2.append((reexpDA, " Need to double quote $@\n"))

reexpRD = re.compile("2>&1\s+>")    
checkList2.append((reexpRD, " Need to have > before 2>&1 like \"> logFile 2>&1\"\n"))

reexpAD = re.compile("\$[a-zA-Z0-9]+=") 
checkList2.append((reexpAD, " $var being assigned a value. Remove $\n"))

reexpDD = re.compile("\s+\[.*&&.*\]")	
checkList2.append((reexpDD, " && in [ ] not allowed\n"))

reexpUE = re.compile("^\s*echo\s+\$\([A-Za-z0-9]+\)\s*$")
checkList2.append((reexpUE, " echo not required\n"))

reexpTQ = re.compile("\".*~.*\"")	
checkList2.append((reexpTQ, " Remove double quotes around Tilde\n"))

reexpDo = re.compile("[a-zA-Z0-9\}]+\s+do[$\s]")
checkList2.append((reexpDo, " Missing a ; before do?\n")) 

reexpDone = re.compile("[a-zA-Z0-9\}]+\s+done")
checkList2.append((reexpDone, " Missing a ; before done\n"))

reexpVA = re.compile("(\s+=|=\s+)")
checkList2.append((reexpVA, "Space in variable assignments\n"))

def parseFiles(files):

    for fl in files:
     
        lNum = 0
        with open(fl, "r") as f:
            content = f.readlines()
        
        if '#!/bin/bash' not in content[0] \
             and '#!/usr/bin/env bash' not in content[0] \
             and '#!/bin/sh' not in content[0] \
             and '#!/usr/bin/env sh' not in content[0]:
            continue
     
        for ln in content:
            lNum+=1
        
            for aTuple in checkList2:
                if aTuple[0].search(ln):
                    print fl, lNum, ln,
                    print aTuple[1]

 
if __name__ == "__main__":
    parseFiles(sys.argv[1:])    
