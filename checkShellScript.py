#!/usr/bin/env python

## Author Aditya Naidu
## $Id$

import re
import sys
import os.path

## Add elements to checkList2 for additional checks
checkList2 = []

reexpDA1 = re.compile("(\s+\$@|\$@\s+)")
checkList2.append((reexpDA1, " Need to double quote $@\n"))

reexpDA2 = re.compile("(\s+\$\*|\$\*\s+)")
checkList2.append((reexpDA2, " Need to double quote $*\n"))

reexpRD = re.compile("2>&1\s+>")    
checkList2.append(
     (reexpRD, " > should be before 2>&1 like \"> logFile 2>&1\"\n"))

reexpAD = re.compile("\$[a-zA-Z0-9]+=") 
checkList2.append((reexpAD, " $<var> being assigned a value. Remove $\n"))

reexpDD = re.compile("\s+\[.*&&.*\]")	
checkList2.append((reexpDD, " && in [ ] not allowed\n"))

reexpUE = re.compile("^\s*echo\s+\$\([A-Za-z0-9]+\)\s*$")
checkList2.append((reexpUE, " echo not required\n"))

reexpTQ = re.compile("\".*~.*\"")	
checkList2.append((reexpTQ, " Remove double quotes around Tilde\n"))

reexpDo = re.compile("[a-zA-Z0-9\}]+\s+do[$\s]")
checkList2.append((reexpDo, " Missing a ; before do\n")) 

reexpDone = re.compile("[a-zA-Z0-9\}]+\s+done")
checkList2.append((reexpDone, " Missing a ; before done\n"))

reexpVA = re.compile("(\s+=[^=]|=[^=]\s+)")
checkList2.append((reexpVA, " Space in variable assignments\n"))

def usage():
    print "Usage: %s <space separated script files list>" % sys.argv[0]
    print "Eg. %s script1 script2 script3" % sys.argv[0]
    sys.exit(1)

def parseFiles(files):

    for fl in files:

        if os.path.isfile(fl) == False:
            print "File %s doesn't exists" % fl
            continue
     
        with open(fl, "r") as f:
            content = f.readlines()
        
        if 'bash' not in content[0] \
             or content[0].startswith('#!') == False:
            print "%s is missing a proper #! line\n" % fl   

        checkFile(content, fl)

def checkFile(content, fileName):

    lNum = 0

    for ln in content:
        lNum+=1
        subLns = ln.split('|') #treat lines with pipes as multiple lines
        for aTuple in checkList2:
            for asubLn in subLns:
                if aTuple[0].search(asubLn):
                    print "%s:%d %s" % (fileName, lNum, asubLn),  
                    print aTuple[1]
 
if __name__ == "__main__":
    if len(sys.argv) == 1 or sys.argv[1] == "-h":
        usage()

    parseFiles(sys.argv[1:])    

