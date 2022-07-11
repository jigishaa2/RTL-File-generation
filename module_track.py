from os import listdir
#from os import join
from pdb import set_trace as breakpoint
import re
import os, glob
import sys
import random
import shutil
from shutil import copyfile

'''
def wire(lines):
    for index4,line in enumerate(lines):
        if 'reg' in line:
            if '=' in line:
                line = line.split('=')[0]
                linevalue = line.split()
                    #breakpoint()
                if 'reg' == linevalue[0]:
                        #breakpoint()
                    if len(linevalue) > 3 or '][' in line:
                        validreg = []
                        #breakpoint()
                        regsitors = []
                            #if '=' in linevalue:
                            #    regsitors.append(linevalue[1].replace(',','').replace(';',''))
                        for item in linevalue:                                 
                            if '[' in item:
                                item1 = item.replace('[','').replace(']','').replace(';','').split(':')
                                for items in item1:
                                    if items == '0':
                                        continue
                                    else:
                                        try:number = eval(items)
                                        except: continue
                                    validreg.append('[' + str(number) + ':0]')
                            elif ',' in item or ';' in item:
                                regsitors.append(item.replace(',','').replace(';',''))
                                    
                        validreg = ''.join(validreg)
                        if validreg == '':
                            validreg = str(2)
                        for linevaluex in regsitors:
                            Validreg.append(linevaluex + ' ' + validreg)
                        validreg = []
                    elif len(linevalue)> 2:
                            #breakpoint()
                        l1 = linevalue[1].replace('0','')
                        l2 = l1.replace('[','')
                        l3 = l2.replace(']','')
                        l4 = l3.replace(':','')
                        try:Valid.append(linevalue[2].replace(',','').replace(';','') + ' ' + str(2**(int(l4)+1)))
                        except: continue
                        Validreg.append(linevalue[2].replace(',','').replace(';','') + ' ' + linevalue[1])
                    else:
                        Valid.append(linevalue[1].replace(';','') + ' ' + str(2))
                        Validreg.append(linevalue[1].replace(';','') + ' ' + str(2))
            if 'logic' in line and ('input' not in line and 'output' not in line):
                linevalue = line.split()
                    #breakpoint()
                if 'logic' == linevalue[0]:
                        #breakpoint()
                    if len(linevalue) > 3 or '][' in line:
                        validreg = []
                        for item in linevalue: 
                            if '[' in item:
                                item1 = item.replace('[','').replace(']','').split(':')
                                for items in item1:
                                    if items == '0':
                                        continue
                                    else:
                                        try:number = eval(items)
                                        except: continue
                                    validreg.append('[' + str(number) + ':0]')
                            validreg = ''.join(validreg)
                            Validreg.append(linevalue[2] + ' ' + validreg)
                            validreg = []
                        elif len(linevalue)> 2:
                            #breakpoint()
                            l1 = linevalue[1].replace('0','')
                            l2 = l1.replace('[','')
                            l3 = l2.replace(']','')
                            l4 = l3.replace(':','')
                            try:Valid.append(linevalue[2].replace(',','').replace(';','') + ' ' + str(2**(int(l4)+1)))
                            except: continue
                            Validreg.append(linevalue[2].replace(',','').replace(';','') + ' ' + linevalue[1])
                        else:
                            Valid.append(linevalue[1].replace(',','').replace(';','') + ' ' + str(2**0))
                if 'output' in line:
                    linevalue = line.split()
                    #breakpoint()
                    if 'output' == linevalue[0]:
                        #breakpoint()
                        if len(linevalue) > 3 or '][' in line:
                            validreg = []
                            for item in linevalue: 
                                if '[' in item:
                                    item1 = item.replace('[','').replace(']','').split(':')
                                    for items in item1:
                                        if items == '0':
                                            continue
                                        else:
                                           try:number = eval(items)
                                           except: continue
                                    validreg.append('[' + str(number) + ':0]')
                            validreg = ''.join(validreg)
                            Validreg.append(linevalue[2] + ' ' + validreg)
                            validreg = []
                        elif len(linevalue)> 2:
                            #breakpoint()
                            l1 = linevalue[1].replace('0','')
                            l2 = l1.replace('[','')
                            l3 = l2.replace(']','')
                            l4 = l3.replace(':','')
                            try:Valid.append(linevalue[2].replace(',','').replace(';','') + ' ' + str(2**(int(l4)+1)))
                            except: continue
                            Validreg.append(linevalue[2].replace(',','').replace(';','') + ' ' + linevalue[1])
                        else:
                            Valid.append(linevalue[1].replace(',','').replace(';','') + ' ' + str(2**0))

            for reg in Validreg:
                Register.append(reg.split()[0])
            for index4,line in enumerate(lines):
                if ' = ' in line:
                    line1 = line.split()
                    for index1, things in enumerate(line1):
                        if '=' == things:
                            if line1[index1+1] in linespec:
                                linespec.append(line1[index1-1])
                    #for specreg in linespec:
                        
                elif ' <= ' in line:
                    line1 = line.split()
                    for index1, things in enumerate(line1):
                        if '<=' == things:
                            if line1[index1+1] in linespec:
                                linespec.append(line1[index1-1])
                    #for specreg in linespec:
                        
    return Valid, Validreg
'''
def connectup(IPO, IP3, lines):
    breakpoint()
    module = []
    connect = []
    for line in lines:
        line1 = line.replace('\n','').replace('/','').split()
        if line1 == []:
            continue
        if IPO in line1 and IPO not in line1[0]:
            module.append(line1[0])
            if IP3 in line1[0]:
                connect.append(IP3 + ' ' + IP0)

    return module, connect

def connectdown(IPO, IP3, lines):
    breakpoint()
    module = []
    connect = []
    for line in lines:
        line1 = line.replace('\n','').replace('/','').split()
        if line1 == []:
            continue
        if IPO in line1[0]:
            for index, items in enumerate(line1):
                if index == 0:
                    continue
                else:
                    module.append(items)
            if IP3 in line1:
                connect.append(IPO + ' ' + IP3)

    return module, connect

def connectline(IPO, IP3 , lines):
    connect = []
    for line in lines:
        line1 = line.replace('\n','').replace('/','').split()
        if IPO in line1 and IP3 in line1 and IPO not in line1[0]:
            connect.append(IPO + ' ' + line1[0] + ' ' + IP3)                

    return connect

def copyfiles(mypath, newpath, justpath, filelist, filelist1):
    for folder in justpath:
        anotherpath = newpath + folder + '/'
        onlyfiles1 = [f for f in listdir(anotherpath) if os.path.isfile(''.join([anotherpath,f]))]
        justpath1 = [f for f in listdir(anotherpath) if not os.path.isfile(''.join([anotherpath,f]))]
        print(onlyfiles1)
        print(justpath1)
        #breakpoint()
        for files in onlyfiles1:
            source = anotherpath + files
            destination = mypath + Newdir + files
            if '.v' in files or '.sv' in files:
                filelist.append(files + '\n')
                filelist1.append(files)
                try:shutil.copyfile(source, destination)
                except:print('file exist')
        copyfiles(mypath, anotherpath, justpath1, filelist, filelist1)

 


mypath = 'RTL/'
f = listdir(mypath)
print(f)


onlyfiles = [f for f in listdir(mypath) if os.path.isfile(''.join([mypath,f]))]
justpath = [f for f in listdir(mypath) if not os.path.isfile(''.join([mypath,f]))]
print(onlyfiles)
print(justpath)

#def Module_Track():
#onlyfiles1 = []
#for f in listdir(mypath):
#    if os.path.isfile(''.join([mypath,f])):
#        onlyfiles1.append(f)

#print(onlyfiles1)
#breakpoint()
Newdir = 'All_RTL/'
Newpath = os.path.join(mypath, Newdir)
try:os.mkdir(Newpath) 
except:print('path exsit')


filelist = []
filelist1 = []
copyfiles(mypath, mypath, justpath, filelist, filelist1)

#breakpoint()
fileobject = open("RTL/All_RTL/RTLFiles.txt", "w+")
fileobject.writelines(filelist)
fileobject.close()


#breakpoint()
modulelist = []
modulelist1 = []
#breakpoint()
for i, items in enumerate(filelist1):
    itempath = "RTL/All_RTL/RTLFiles_" + str(i) + ".txt"
    fileobject = open(itempath,"w+")
    fileobject.write(items)
    fileobject.close()


    with open(mypath + Newdir + items) as fl:
        #breakpoint()
        lines = fl.readlines()
        fl.close()                
    for index4,line in enumerate(lines):
        if 'module' in line and 'endmodule' not in line and 'module' == line.split()[0]:
            themodule = line.split()[1]
            themodule1 = themodule.split('(')[0]
            modulelist.append(themodule1)
            modulelist1.append(items + ' ' + themodule1)



#breakpoint()
#moduleconnection = []
# with open('spec.txt') as fl:
#     linespecs = fl.readlines()
#     for linespe in linespecs:
#         linespec = ''.join(linespe.replace('\n',''))
breakpoint()
Allconnection = []
fileobject = open("RTL/rtl2/All_RTL/moduleconnection.txt", "w+")
for i, items in enumerate(filelist1):
    modulelist2 = []
    modulelist3 = modulelist
    modulelist4 = modulelist1
    check = 0
    comment = 0
    itempath = "RTL/All_RTL/RTLFiles_" + str(i) + ".txt"
    Assignment1 = []
    #fileobject = open(itempath,"w")
    with open(mypath + Newdir + items) as fl:
        #breakpoint()
        lines = fl.readlines()
        fl.close()
    #fileobject.write(items + '\n')  
    #breakpoint() 
    newmodule = 0
    newmodule1 = 0   
    for index4,line in enumerate(lines):
        linevalue = line.split()
        #if linespec in line: #and ('reg' in linevalue or 'wire' in linevalue or 'output' in linevalue):
        #    print(line)
        #    breakpoint()
        #    moduleo = themodule1
        if 'module' in line and 'endmodule' not in line and 'module' == line.split()[0]:
            modulelist2 = []
            Assignment = []
            check = 1
            themodule = line.split()[1]
            themodule1 = themodule.split('(')[0]
            modulelist2.append(themodule1 + ' ')
            print(modulelist2)
            continue
        if 'endmodule' in line:
            check = 0
            print(modulelist2)
            moduleconnection = ''.join(modulelist2)
            ConnectionAssignment = ''.join(Assignment)
            fileobject.write(moduleconnection + '/' + ConnectionAssignment + '\n')

        #if 'or1k_marocchino_ctrl' in line:
        #    print(line)
        #    breakpoint()

            #fileobject.write()
        if check == 1:
            if linespec in line and ('reg' in linevalue or 'wire' in linevalue or 'output' in linevalue):
                print(line)
                breakpoint()
                moduleo = themodule1
            if linevalue != []:
                if '//' in linevalue[0]:
                    continue
                if '/*' in linevalue and '*/' in linevalue:
                    comment = 0
                    continue
                if '/*' in linevalue[0] and '*/' in linevalue[len(linevalue)-1]:
                    comment = 0
                    print(line,comment)
                elif '/*' in linevalue[0]: 
                    comment = 1
                    print(line,comment)
                    continue
                elif '*/' in linevalue[len(linevalue)-1] or '*/' in linevalue:
                    comment = 0
                    print(line,comment)
                    continue
                
                if comment == 1:
                    continue
                if '.' in linevalue[0] and ';' not in linevalue[len(linevalue)-1]:
                    #breakpoint()
                    if len(linevalue) > 1:
                        Assignment1.append(linevalue[0].replace('.','') + ' ' + linevalue[1].replace(',','').replace('(','').replace(')','').replace(';','') + '\n')
                    elif '*' in linevalue[0]:
                        continue
                    else:
                        linevalue1 = linevalue[0].split('(')
                        Assignment1.append(linevalue1[0].replace('.','') + ' ' +linevalue1[1].replace(',','').replace('(','').replace(')','').replace(';','')+ '\n')


            
            for index, modules in enumerate(modulelist3):
                if modules in linevalue or modules in line.replace(' ','').replace('\n',''):
                    #breakpoint()
                    if (modules + '(') in linevalue or '(' in lines[index4 + 1] or (modules in linevalue and '(' in linevalue):
                        newmodule = newmodule + 1
                        #breakpoint()
                        #flx = open('Wire/' +  )
                        #fileobject.write(modulelist4[index].split()[0] + '\n')
                        modulelist2.append(modules + ' ')
                        #modulelist3.pop(index)
                        #modulelist4.pop(index)
                        currentmodule = modules
                        #breakpoint()
                        break
        if newmodule1 < newmodule and ');' in line:
            #breakpoint()
            newmodule1 = newmodule
            wires = []
            for thins in Assignment1:
                if thins == '\n':
                    continue
                else:
                    wires.append(thins)
            Allconnection.append(themodule + ' ' +currentmodule + '.v\n')
            flx = open('Wire/' + themodule + ' ' +currentmodule + '.v','w+')
            flx.writelines(wires)
            flx.close()
            Assignment1 = []

fl = open('Wire/allconnection.v', 'w+')
fl.writelines(Allconnection)
fl.close()

print('------------------3PIP---------------------')
breakpoint()
#fileobject.writelines(moduleconnection)
fileobject.close()

with open('3PIP.txt') as fl:
    lines = fl.readlines()
    IP3 = lines[0].replace('\n','')
    IPO = lines[1].replace('\n','')
fl.close()

IPO = moduleo

with open("RTL/rtl2/All_RTL/moduleconnection.txt") as fl1:
    linex = fl1.readlines()
fl1.close()

ConnectLine = []
ConnectUP = []
ConnectDown = []
moduleup1 = []
moduleup2 = []
moduledown1 = []
moduledown2 = []
moduleup3 = []
moduledonw3 = []
ConnectLine = connectline(IPO, IP3, linex)
moduleup2, connectup1 = connectup(IPO, IP3, linex)
moduledown2, connectdown1 = connectdown(IPO, IP3, linex)
done = 0
breakpoint()

while moduleup1 != moduleup2 or done == 0:
    for item in moduleup2:
        if item not in moduleup1:
            moduleup1.append(item)
    for item in moduleup2:
        moduleup3, connectup1 = connectup(item, IP3, linex)
        for item1 in moduleup3:
            ConnectLine = connectline(item1, IP3, linex)
    if ConnectLine != []:
        done = 1

while moduledown1 != moduledown2 or done == 0:
    for item in moduleup2:
        if item not in moduleup1:
            moduleup1.append(item)
    for item in moduleup2:
        moduledown3, connectdown1 = connectdown(IPO, IP3, linex)   
        for item1 in moduledown3:
            ConnectLine = connectline(item1, IP3, linex)
         
    
    #ConnectLine = connectline(IPO, IP3, linex)
    if ConnectLine != []:   
        done = 1

flx = open('Wire/' + 'connect.v','w+')
flx.writelines(ConnectLine)
flx.close()








